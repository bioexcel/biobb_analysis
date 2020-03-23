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
    Wrapper of the `GROMACS trjconv <http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-trjconv.html>`_ module.

    Args:
        input_structure_path (str): Path to the input structure file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
        input_top_path (str): Path to the GROMACS input topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr, gro, g96, pdb, brk, ent.
        input_index_path (str) (Optional): Path to the GROMACS index file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx>`_. Accepted formats: ndx.
        output_str_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_trjconv.str.pdb>`_. Accepted formats: xtc, trr, gro, g96, pdb, tng.
        properties (dic):
            * **selection** (*str*) - ("System") Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values. Values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
            * **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('gromacs/gromacs:latest') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.
    """

    def __init__(self, input_structure_path, input_top_path, output_str_path, input_index_path=None, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_structure_path": input_structure_path, "input_top_path": input_top_path, "input_index_path": input_index_path }, 
            "out": { "output_str_path": output_str_path } 
        }

        # Properties specific for BB
        self.properties = properties

        # Properties common in all GROMACS BB
        self.gmx_path = get_binary_path(properties, 'gmx_path')

        # container Specific
        self.container_path = properties.get('container_path')
        self.container_image = properties.get('container_image', 'gromacs/gromacs:latest')
        self.container_volume_path = properties.get('container_volume_path', '/tmp')
        self.container_working_dir = properties.get('container_working_dir')
        self.container_user_id = properties.get('container_user_id')
        self.container_shell_path = properties.get('container_shell_path', '/bin/bash')

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
        self.io_dict["in"]["input_structure_path"] = check_traj_path(self.io_dict["in"]["input_structure_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_top_path"] = check_input_path(self.io_dict["in"]["input_top_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_index_path"] = check_index_path(self.io_dict["in"]["input_index_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_str_path"] = check_out_traj_path(self.io_dict["out"]["output_str_path"], out_log, self.__class__.__name__)
        if not self.io_dict["in"]["input_index_path"]:
            self.selection = get_selection(self.properties, out_log, self.__class__.__name__)
        else:
            self.selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'selection', out_log, self.__class__.__name__)

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
            output_file_list = [self.io_dict["out"]["output_str_path"]]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # copy inputs to container
        container_io_dict = fu.copy_to_container(self.container_path, self.container_volume_path, self.io_dict)

        cmd = ['echo', '\"'+self.selection+'\"', '|',
               self.gmx_path, 'trjconv',
               '-f', container_io_dict["in"]["input_structure_path"],
               '-s', container_io_dict["in"]["input_top_path"],
               '-o', container_io_dict["out"]["output_str_path"]]

        if container_io_dict["in"]["input_index_path"]:
            cmd.extend(['-n', container_io_dict["in"]["input_index_path"]])

        # create cmd and launch execution
        cmd = fu.create_cmd_line(cmd, container_path=self.container_path, 
                                 host_volume=container_io_dict.get("unique_dir"), 
                                 container_volume=self.container_volume_path, 
                                 container_working_dir=self.container_working_dir, 
                                 container_user_uid=self.container_user_id, 
                                 container_image=self.container_image, 
                                 container_shell_path=self.container_shell_path, 
                                 out_log=out_log, global_log=self.global_log)
        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()

        # copy output(s) to output(s) path(s) in case of container execution
        fu.copy_to_host(self.container_path, container_io_dict, self.io_dict)

        # if container execution, remove temporary folder
        if self.container_path:
            remove_tmp_files([container_io_dict['unique_dir']], self.remove_tmp, out_log)

        return returncode

def main():
    parser = argparse.ArgumentParser(description="Converts between GROMACS compatible structure file formats and/or extracts a selection of atoms.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_structure_path', required=True, help='Path to the input structure file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.')
    required_args.add_argument('--input_top_path', required=True, help='Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.')
    parser.add_argument('--input_index_path', required=False, help="Path to the GROMACS index file. Accepted formats: ndx.")
    required_args.add_argument('--output_str_path', required=True, help='Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    #Specific call of each building block
    GMXTrjConvStr(input_structure_path=args.input_structure_path, input_top_path=args.input_top_path, 
                  output_str_path=args.output_str_path, input_index_path=args.input_index_path, 
                  properties=properties).launch()

if __name__ == '__main__':
    main()
