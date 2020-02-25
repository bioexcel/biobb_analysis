#!/usr/bin/env python3

"""Module containing the Cpptraj Input class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.ambertools.common import *


class CpptrajInput():
    """Performs multiple analysis and trajectory operations of a given trajectory.
    Wrapper of the Ambertools Cpptraj module.
    Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files.
    The parameter names and defaults are the same as the ones in the official `Cpptraj manual <https://amber-md.github.io/cpptraj/CPPTRAJ.xhtml>`_.

    Args:
        input_instructions_path (str): Path of the instructions file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.in>`_.
        properties (dic):
            * **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """

    def __init__(self, input_instructions_path=None, properties=None, **kwargs):
        properties = properties or {}

        # Properties specific for BB
        self.input_instructions_path = input_instructions_path
        self.input_top_path = kwargs.get('input_top_path')
        self.input_traj_path = kwargs.get('input_traj_path')
        self.output_cpptraj_path = kwargs.get('output_cpptraj_path')
        self.properties = properties
        self.cpptraj_path = properties.get('cpptraj_path', 'cpptraj')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

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
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # Check the properties
        fu.check_properties(self, self.properties)

        output_instructions_path = self.create_instrucions_file() if not self.input_instructions_path else self.input_instructions_path
        check_in_path(output_instructions_path, out_log, self.__class__.__name__)

        # run command line
        cmd = [self.cpptraj_path, '-i', output_instructions_path]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Performs multiple analysis and trajectory operations of a given trajectory.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_instructions_path', required=True, help='Path of the instructions file.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    #Specific call of each building block
    CpptrajInput(input_instructions_path=args.input_instructions_path, properties=properties).launch()

if __name__ == '__main__':
    main()