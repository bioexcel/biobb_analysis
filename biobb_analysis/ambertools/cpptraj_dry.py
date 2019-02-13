#!/usr/bin/env python3

"""Module containing the Cpptraj Dry class and the command line interface."""
import argparse
from ast import literal_eval
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.ambertools.common import get_in_parameters
from biobb_analysis.ambertools.common import get_mask
from biobb_analysis.ambertools.common import get_negative_mask
from biobb_analysis.ambertools.common import get_out_parameters

class Dry():
    """Wrapper of the Ambertools Cpptraj Dry module.
    Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files.
    The parameter names and defaults are the same as
    the ones in the official Cpptraj manual: https://amber-md.github.io/cpptraj/CPPTRAJ.xhtml

    Args:
        input_top_path (str): Path to the input structure or topology file.
        input_traj_path (str): Path to the input trajectory to be processed.
        output_cpptraj_path (str): Path to the output processed trajectory.
        properties (dic):
            | - **instructions_file** (*str*) - ("instructions.in") Name of the instructions file to be created. 
            | - **input_instructions** (*dict*) - (defaults dict) Input options specification.
                | - **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
                    | - **start** (*int*) - (1) Starting frame for slicing
                    | - **end** (*int*) - (-1) Ending frame for slicing
                    | - **step** (*int*) - (1) Step for slicing
                | - **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
                | - **out_parameters** (*dict*) - (None) Parameters for output trajectory.
                    | - **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
            | - **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
    """

    def __init__(self, input_top_path, input_traj_path,
                 output_cpptraj_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_top_path = input_top_path
        self.input_traj_path = input_traj_path
        self.output_cpptraj_path = output_cpptraj_path

        # Properties specific for BB
        # posar 'instructions.in' en funció global
        self.instructions_file = properties.get('instructions_file', 'instructions.in')
        self.instructions = {k: str(v) for k, v in properties.get('input_instructions', dict()).items()}

        # posar 'cpptraj' en funció global
        self.cpptraj_path = properties.get('cpptraj_path', 'cpptraj')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

    def create_instructions_file(self):
        """Creates an input file using the properties file settings"""
        instructions_list = []
        self.instructions_file = fu.create_name(prefix=self.prefix, step=self.step, name=self.instructions_file)

        # parm
        instructions_list.append('parm ' + self.input_top_path + ' ' + self.instructions.pop('parm', ''))

        # trajin
        in_parameters = self.instructions.get('in_parameters', '')
        in_params = get_in_parameters(in_parameters, self)
        instructions_list.append('trajin ' + self.input_traj_path + ' ' + in_params)

        # dry
        mask_dry1 = get_negative_mask('solute', self)
        instructions_list.append('strip ' + mask_dry1)
        mask_dry2 = get_mask('heavy-atoms', self)
        instructions_list.append('strip ' + mask_dry2)

        # mask
        mask = self.instructions.get('mask', '')
        if mask:
            strip_mask = get_negative_mask(mask, self)
            instructions_list.append('strip ' + strip_mask)

        # trajout
        out_parameters = self.instructions.get('out_parameters', '')
        out_params = get_out_parameters(out_parameters, self)
        instructions_list.append('trajout ' + self.output_cpptraj_path + ' ' + out_params)

        # create .in file
        with open(self.instructions_file, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return self.instructions_file

    def launch(self):
        """Launches the execution of the Ambertools cpptraj module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        # create instructions file
        self.create_instructions_file() 

        # run command line
        cmd = [self.cpptraj_path, '-i', self.instructions_file]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        tmp_files = [self.instructions_file]
        removed_files = [f for f in tmp_files if fu.rm(f)]
        fu.log('Removed: %s' % str(removed_files), out_log, self.global_log)
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the Ambertools cpptraj module.")
    parser.add_argument('--config', required=True, help='Configuration file')
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    # Specific args of each building block
    parser.add_argument('--input_top_path', required=True, help='Path to the input Amber structure or topology file.')
    parser.add_argument('--input_traj_path', required=True, help='Path to the input Amber trajectory to be processed.')
    parser.add_argument('--output_cpptraj_path', required=True, help='Path to the output processed Amber trajectory or to the output dat file containing the analysis results.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    # Specific call of each building block
    Dry(input_top_path=args.input_top_path, input_traj_path=args.input_traj_path, output_cpptraj_path=args.output_cpptraj_path, properties=properties).launch()

if __name__ == '__main__':
    main()