#!/usr/bin/env python3

"""Module containing the Cpptraj Input class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.ambertools.common import *

class CpptrajInput():
    """Wrapper of the Ambertools Cpptraj module. Performing any Cpptraj operation from a given instructions file.
    Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files.
    The parameter names and defaults are the same as
    the ones in the official Cpptraj manual: https://amber-md.github.io/cpptraj/CPPTRAJ.xhtml

    Args:
        input_instructions_path (str): Path of the instructions file.
        properties (dic):
            * **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
    """

    def __init__(self, input_instructions_path=None, properties=None, **kwargs):
        properties = properties or {}

        # Properties specific for BB
        self.input_instructions_path = input_instructions_path
        self.input_top_path = kwargs.get('input_top_path')
        self.input_traj_path = kwargs.get('input_traj_path')
        self.output_cpptraj_path = kwargs.get('output_cpptraj_path')
        self.cpptraj_path = properties.get('cpptraj_path', 'cpptraj')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

        # Check the properties
        fu.check_properties(self, properties)

    def create_instrucions_file(self):
        """ Creates an input file using paths provideed in the configuration file (only used for test purposes) """
        instructions_list = []
        output_instructions_path = fu.create_name(prefix=self.prefix, step=self.step, name=get_default_value("instructions_file"))

        instructions_list.append('parm ' + self.input_top_path)
        instructions_list.append('trajin ' + self.input_traj_path)
        instructions_list.append('trajout ' + self.output_cpptraj_path + ' ' + get_default_value("format"))

        with open(output_instructions_path, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return output_instructions_path

    def launch(self):
        """Launches the execution of the Ambertools cpptraj module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        output_instructions_path = self.create_instrucions_file() if not self.input_instructions_path else self.input_instructions_path
        check_in_path(output_instructions_path, out_log, self.__class__.__name__)

        # run command line
        cmd = [self.cpptraj_path, '-i', output_instructions_path]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper of the Ambertools Cpptraj module. Performing any Cpptraj operation from a given instructions file.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_instructions_path', required=True, help='Path of the instructions file.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    CpptrajInput(input_instructions_path=args.input_instructions_path, properties=properties).launch()

if __name__ == '__main__':
    main()
