#!/usr/bin/env python3

"""Module containing the Cpptraj Rgyr class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.ambertools.common import *


class Rgyr():
    """Wrapper of the Ambertools Cpptraj module. Calculating Rgyr analysis.
    Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files.
    The parameter names and defaults are the same as
    the ones in the official Cpptraj manual: https://amber-md.github.io/cpptraj/CPPTRAJ.xhtml

   Args:
        input_top_path (str): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
        input_traj_path (str): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
        output_cpptraj_path (str): Path to the output analysis.
        properties (dic):
            * **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
                * **start** (*int*) - (1) Starting frame for slicing
                * **end** (*int*) - (-1) Ending frame for slicing
                * **step** (*int*) - (1) Step for slicing
                * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
            * **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
    """

    def __init__(self, input_top_path, input_traj_path,
                 output_cpptraj_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_top_path = input_top_path
        self.input_traj_path = input_traj_path
        self.output_cpptraj_path = output_cpptraj_path

        # Properties specific for BB
        self.instructions_file = get_default_value('instructions_file')
        self.properties = properties
        self.cpptraj_path = get_binary_path(properties, 'cpptraj_path')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

        # Check the properties
        fu.check_properties(self, properties)

    def check_data_params(self):
        """ Checks all the input/output paths and parameters """
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)
        self.input_top_path, self.input_top_path_orig = check_top_path(self.input_top_path, out_log, self.__class__.__name__)
        self.input_traj_path = check_traj_path(self.input_traj_path, out_log, self.__class__.__name__)
        self.output_cpptraj_path = check_out_path(self.output_cpptraj_path, out_log, self.__class__.__name__)
        self.in_parameters = get_parameters(self.properties, 'in_parameters', self.__class__.__name__, out_log)

    def create_instructions_file(self):
        """Creates an input file using the properties file settings"""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)
        instructions_list = []
        self.instructions_file = os.path.join(fu.create_unique_dir(), self.instructions_file)
        fu.create_name(prefix=self.prefix, step=self.step, name=self.instructions_file)

        # parm
        instructions_list.append('parm ' + self.input_top_path)

        # trajin
        in_params = get_in_parameters(self.in_parameters, out_log)
        instructions_list.append('trajin ' + self.input_traj_path + ' ' + in_params)

        # Set up
        instructions_list += setup_structure(self)

        # mask
        mask = self.in_parameters.get('mask', '')
        if mask:
            strip_mask = get_negative_mask(mask, out_log)
            instructions_list.append('strip ' + strip_mask)

        # output
        instructions_list.append('radgyr time 1 out ' + self.output_cpptraj_path)

        # create .in file
        with open(self.instructions_file, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return self.instructions_file

    def launch(self):
        """Launches the execution of the Ambertools cpptraj module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        # check input/output paths and parameters
        self.check_data_params()

        # create instructions file
        self.create_instructions_file() 

        # run command line
        cmd = [self.cpptraj_path, '-i', self.instructions_file]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        remove_tmp_files([os.path.dirname(self.instructions_file)], out_log, self.input_top_path_orig, self.input_top_path)
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper of the Ambertools Cpptraj module. Calculating Rgyr analysis.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_top_path', required=True, help='Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.')
    required_args.add_argument('--input_traj_path', required=True, help='Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.')
    required_args.add_argument('--output_cpptraj_path', required=True, help='Path to the output analysis.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    # Specific call of each building block
    Rgyr(input_top_path=args.input_top_path, input_traj_path=args.input_traj_path, output_cpptraj_path=args.output_cpptraj_path, properties=properties).launch()

if __name__ == '__main__':
    main()