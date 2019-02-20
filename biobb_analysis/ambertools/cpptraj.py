#!/usr/bin/env python3

"""Module containing the Cpptraj class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.ambertools.common import *

class Cpptraj():
    """Wrapper of the Ambertools Cpptraj module.
    Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files.
    The parameter names and defaults are the same as
    the ones in the official Cpptraj manual: https://amber-md.github.io/cpptraj/CPPTRAJ.xhtml

    Args:
        input_instructions_path (str): Path of the instructions file.
        properties (dic):
            | - **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
    """

    def __init__(self, input_instructions_path, properties=None, **kwargs):
        properties = properties or {}

        # check if input_instructions_path = None (test) and create .in for test purposes

        # Properties specific for BB
        self.input_instructions_path = input_instructions_path

        self.cpptraj_path = properties.get('cpptraj_path', 'cpptraj')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')


    def launch(self):
        """Launches the execution of the Ambertools cpptraj module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        output_instructions_path = self.input_instructions_path
        check_in_path(output_instructions_path, self)

        # run command line
        cmd = [self.cpptraj_path, '-i', output_instructions_path]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the Ambertools cpptraj module.")
    parser.add_argument('--config', required=False, help='Configuration file')

    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    parser.add_argument('--input_instructions_path', required=True, help='Path of the instructions file.')

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    Cpptraj(input_instructions_path=args.input_instructions_path, properties=properties).launch()

if __name__ == '__main__':
    main()
