#!/usr/bin/env python3

"""Module containing the GMX TrjConvStr class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.gromacs.common import *


class GMXTrjConvStr():
    """Converts between GROMACS compatible structure file formats and/or extracts a selection of atoms.
    Wrapper of the GROMACS trjconv (http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-trjconv.html) module.

    Args:
        input_structure_path (str): Path to the input structure file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
        input_top_path (str): Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
        input_index_path (str): Path to the GROMACS index file. Accepted formats: ndx.
        output_str_path (str): Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.
        properties (dic):
            * **selection** (*str*) - ("System") Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
            * **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """

    def __init__(self, input_structure_path, input_top_path, output_str_path, input_index_path=None, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_structure_path = input_structure_path
        self.input_top_path = input_top_path
        self.input_index_path = input_index_path
        self.output_str_path = output_str_path

        # Properties specific for BB
        self.properties = properties

        # Properties common in all GROMACS BB
        self.gmx_path = get_binary_path(properties, 'gmx_path')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.input_structure_path = check_traj_path(self.input_structure_path, out_log, self.__class__.__name__)
        self.input_top_path = check_input_path(self.input_top_path, out_log, self.__class__.__name__)
        self.input_index_path = check_index_path(self.input_index_path, out_log, self.__class__.__name__)
        self.output_str_path = check_out_traj_path(self.output_str_path, out_log, self.__class__.__name__)
        if not self.input_index_path:
            self.selection = get_selection(self.properties, out_log, self.__class__.__name__)
        else:
            self.selection = get_selection_index_file(self.properties, self.input_index_path, 'selection', out_log, self.__class__.__name__)

    @launchlogger
    def launch(self):
        """Launches the execution of the GROMACS rgyr module."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        # Restart
        if self.restart:
            output_file_list = [self.output_str_path]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        cmd = ['echo', '\"'+self.selection+'\"', '|',
               self.gmx_path, 'trjconv',
               '-f', self.input_structure_path,
               '-s', self.input_top_path,
               '-o', self.output_str_path]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Converts between GROMACS compatible structure file formats and/or extracts a selection of atoms.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_structure_path', required=True, help='Path to the input structure file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.')
    required_args.add_argument('--input_top_path', required=True, help='Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.')
    parser.add_argument('--input_index_path', required=False, help="Path to the GROMACS index file. Accepted formats: ndx.")
    required_args.add_argument('--output_str_path', required=True, help='Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    GMXTrjConvStr(input_structure_path=args.input_structure_path, input_top_path=args.input_top_path, output_str_path=args.output_str_path, input_index_path=args.input_index_path, properties=properties).launch()

if __name__ == '__main__':
    main()
