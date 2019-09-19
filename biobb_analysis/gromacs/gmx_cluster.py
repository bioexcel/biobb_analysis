#!/usr/bin/env python3

"""Module containing the GMX Cluster class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.gromacs.common import *


class GMXCluster():
    """Creates cluster structures from a given GROMACS compatible trajectory.
    Wrapper class for the GROMACS cluster (http://manual.gromacs.org/current/onlinehelp/gmx-cluster.html) module.

    Args:
        input_structure_path (str): Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
        input_traj_path (str): Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
        input_index_path (str): Path to the GROMACS index file. Accepted formats: ndx.
        output_pdb_path (str): Path to the output cluster file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
        properties (dic):
            * **fit_selection** (*str*) - ("System") - Group where the fitting will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
            * **output_selection** (*str*) - ("System") Group that is going to be written in the output trajectory. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
            * **dista** (*bool*) - (False) Use RMSD of distances instead of RMS deviation.
            * **method** (*str*) - ("linkage") Method for cluster determination. Values: linkage, jarvis-patrick, monte-carlo, diagonalization, gromos.
            * **cutoff** (*float*) - (0.1) RMSD cut-off (nm) for two structures to be neighbor.
            * **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """

    def __init__(self, input_structure_path, input_traj_path, output_pdb_path, input_index_path=None, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_structure_path = input_structure_path
        self.input_traj_path = input_traj_path
        self.input_index_path = input_index_path
        self.output_pdb_path = output_pdb_path

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
        self.input_structure_path = check_input_path(self.input_structure_path, out_log, self.__class__.__name__)
        self.input_traj_path = check_traj_path(self.input_traj_path, out_log, self.__class__.__name__)
        self.input_index_path = check_index_path(self.input_index_path, out_log, self.__class__.__name__)
        self.output_pdb_path = check_out_pdb_path(self.output_pdb_path, out_log, self.__class__.__name__)
        if not self.input_index_path:
            self.fit_selection = get_image_selection(self.properties, 'fit_selection', out_log, self.__class__.__name__)
            self.output_selection = get_image_selection(self.properties, 'output_selection', out_log, self.__class__.__name__)
        else:
            self.fit_selection = get_selection_index_file(self.properties, self.input_index_path, 'fit_selection', out_log, self.__class__.__name__)
            self.output_selection = get_selection_index_file(self.properties, self.input_index_path, 'output_selection', out_log, self.__class__.__name__)
        self.dista = get_dista(self.properties, out_log, self.__class__.__name__)
        self.method = get_method(self.properties, out_log, self.__class__.__name__)
        self.cutoff = get_cutoff(self.properties, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self):
        """Launches the execution of the GROMACS rms module."""

        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        if self.restart:
            output_file_list = [self.output_pdb_path]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        cmd = ['echo', '\"' + self.fit_selection + '\" \"' + self.output_selection + '\"', '|',
               self.gmx_path, 'cluster',
               '-s', self.input_structure_path,
               '-f', self.input_traj_path,
               '-cl', self.output_pdb_path,
               '-cutoff', str(self.cutoff),
               '-method', self.method]

        if self.input_index_path:
            cmd.extend(['-n', self.input_index_path])

        if self.dista:
            cmd.append('-dista')

        return cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()

def main():
    parser = argparse.ArgumentParser(description="Creates cluster structures from a given GROMACS compatible trajectory.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_structure_path', required=True, help='Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.')
    required_args.add_argument('--input_traj_path', required=True, help='Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.')
    parser.add_argument('--input_index_path', required=False, help="Path to the GROMACS index file. Accepted formats: ndx.")
    required_args.add_argument('--output_pdb_path', required=True, help='Path to the output cluster file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    GMXCluster(input_structure_path=args.input_structure_path, input_traj_path=args.input_traj_path, output_pdb_path=args.output_pdb_path, input_index_path=args.input_index_path, properties=properties).launch()

if __name__ == '__main__':
    main()
