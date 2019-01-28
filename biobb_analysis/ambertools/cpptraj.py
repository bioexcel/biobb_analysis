#!/usr/bin/env python3

"""Module containing the Cpptraj class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper

class Cpptraj():
    """Wrapper of the Ambertools Cpptraj module.
    Cpptraj (the successor to ptraj) is the main program in Amber for processing coordinate trajectories and data files.
    The parameter names and defaults are the same as
    the ones in the official Cpptraj manual: https://amber-md.github.io/cpptraj/CPPTRAJ.xhtml

    Args:
        input_top_path (str): Path to the input Amber structure or topology file.
        input_traj_path (str): Path to the input Amber trajectory to be processed.
        output_cpptraj_path (str): Path to the output processed Amber trajectory or to the output dat file containing the analysis results.
        properties (dic):
            | - **input_instructions_path** (*str*) - (None) Path of the input file.
            | - **output_instructions_path** (*str*) - ("instructions.in") Name of the instructions file to be created.
            | - **input_instructions** (*dict*) - (defaults dict) Input options specification. (Used if *input_file_path* is None)
            | - **analysis** (*str*) - ("rms") Default options for the input instructions file. Valid values: rms, undefined
            | - **format** (*str*) - ("netcdf") Format for convert. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib
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
        self.output_instructions_path = properties.get('output_instructions_path', 'instructions.in')
        self.input_instructions_path = properties.get('input_instructions_path', None)
        self.instructions = {k: str(v) for k, v in properties.get('input_instructions', dict()).items()}

        self.cpptraj_path = properties.get('cpptraj_path', 'cpptraj')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

    def create_instrucions_file(self):
        """Creates an input file using the properties file settings"""
        instructions_list = []
        self.output_instructions_path = fu.create_name(prefix=self.prefix, step=self.step, name=self.output_instructions_path)
        # analysis type
        analysis = self.instructions.get('analysis', 'rms')
        rms = (analysis.strip().lower() == 'rms')
        convert = (analysis.strip().lower() == 'convert')

        #parm
        instructions_list.append('parm '+self.input_top_path+' '+self.instructions.pop('parm', ''))

        #trajin
        instructions_list.append('trajin '+self.input_traj_path+' '+self.instructions.pop('trajin', ''))

        if rms:
            instructions_list.append('rms '+''.join(self.instructions.get('trajout_parameters', ''))+' out '+self.output_cpptraj_path)

        if convert:
            format = self.instructions.get('format', 'netcdf')
            instructions_list.append('trajout '+self.output_cpptraj_path+' '+format)


        with open(self.output_instructions_path, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return self.output_instructions_path

    def launch(self):
        """Launches the execution of the Ambertools cpptraj module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        self.output_instructions_path = self.create_instrucions_file() if not self.input_instructions_path else self.input_instructions_path

        cmd = [self.cpptraj_path, '-i', self.output_instructions_path]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        tmp_files = [self.output_instructions_path]
        removed_files = [f for f in tmp_files if fu.rm(f)]
        fu.log('Removed: %s' % str(removed_files), out_log, self.global_log)
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the Ambertools cpptraj module.")
    parser.add_argument('--config', required=True)
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    #Specific args of each building block
    parser.add_argument('--input_top_path', required=True)
    parser.add_argument('--input_traj_path', required=True)
    parser.add_argument('--output_cpptraj_path', required=True)

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    Cpptraj(input_top_path=args.input_top_path, input_traj_path=args.input_traj_path, output_cpptraj_path=args.output_cpptraj_path, properties=properties).launch()

if __name__ == '__main__':
    main()
