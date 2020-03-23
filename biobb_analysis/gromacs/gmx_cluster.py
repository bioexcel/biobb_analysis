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
    Wrapper class for the `GROMACS cluster <http://manual.gromacs.org/current/onlinehelp/gmx-cluster.html>`_ module.

    Args:
        input_structure_path (str): Path to the input structure file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr, gro, g96, pdb, brk, ent.
        input_traj_path (str): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
        input_index_path (str) (Optional): Path to the GROMACS index file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx>`_. Accepted formats: ndx.
        output_pdb_path (str): Path to the output cluster file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_cluster.pdb>`_. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
        properties (dic):
            * **fit_selection** (*str*) - ("System") Group where the fitting will be performed. If **input_index_path** provided, check the file for the accepted values. Values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
            * **output_selection** (*str*) - ("System") Group that is going to be written in the output trajectory. If **input_index_path** provided, check the file for the accepted values. Values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
            * **dista** (*bool*) - (False) Use RMSD of distances instead of RMS deviation.
            * **method** (*str*) - ("linkage") Method for cluster determination. Values: linkage, jarvis-patrick, monte-carlo, diagonalization, gromos.
            * **cutoff** (*float*) - (0.1) RMSD cut-off (nm) for two structures to be neighbor.
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

    def __init__(self, input_structure_path, input_traj_path, output_pdb_path, input_index_path=None, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_structure_path": input_structure_path, "input_traj_path": input_traj_path, "input_index_path": input_index_path }, 
            "out": { "output_pdb_path": output_pdb_path } 
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

        # Internal parameters
        self.xvg_path = fu.create_name(prefix=self.prefix, step=self.step, name=properties.get('xvg_path', 'rmsd-dist.xvg'))
        self.xpm_path = fu.create_name(prefix=self.prefix, step=self.step, name=properties.get('xpm_path', 'rmsd-clust.xpm'))
        self.log_path = fu.create_name(prefix=self.prefix, step=self.step, name=properties.get('log_path', 'cluster.log'))

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_structure_path"] = check_input_path(self.io_dict["in"]["input_structure_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_traj_path"] = check_traj_path(self.io_dict["in"]["input_traj_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_index_path"] = check_index_path(self.io_dict["in"]["input_index_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_pdb_path"] = check_out_pdb_path(self.io_dict["out"]["output_pdb_path"], out_log, self.__class__.__name__)
        if not self.io_dict["in"]["input_index_path"]:
            self.fit_selection = get_image_selection(self.properties, 'fit_selection', out_log, self.__class__.__name__)
            self.output_selection = get_image_selection(self.properties, 'output_selection', out_log, self.__class__.__name__)
        else:
            self.fit_selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'fit_selection', out_log, self.__class__.__name__)
            self.output_selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'output_selection', out_log, self.__class__.__name__)
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
            output_file_list = [self.io_dict["out"]["output_pdb_path"]]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # copy inputs to container
        container_io_dict = fu.copy_to_container(self.container_path, self.container_volume_path, self.io_dict)

        # if container execution, add container_volume_path to log, xvg & xpm (because docker doesn't allow to write teses files out of the /tmp folder)
        if self.container_path:
            self.log_path = str(PurePath(self.container_volume_path).joinpath(self.log_path))
            self.xvg_path = str(PurePath(self.container_volume_path).joinpath(self.xvg_path))
            self.xpm_path = str(PurePath(self.container_volume_path).joinpath(self.xpm_path))

        cmd = ['echo', '\"' + self.fit_selection + '\" \"' + self.output_selection + '\"', '|',
               self.gmx_path, 'cluster',
               '-g', self.log_path,
               '-dist', self.xvg_path,
               '-o', self.xpm_path,
               '-s', container_io_dict["in"]["input_structure_path"],
               '-f', container_io_dict["in"]["input_traj_path"],
               '-cl', container_io_dict["out"]["output_pdb_path"],
               '-cutoff', str(self.cutoff),
               '-method', self.method]

        if container_io_dict["in"]["input_index_path"]:
            cmd.extend(['-n', container_io_dict["in"]["input_index_path"]])

        if self.dista:
            cmd.append('-dista')

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
    parser = argparse.ArgumentParser(description="Creates cluster structures from a given GROMACS compatible trajectory.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_structure_path', required=True, help='Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.')
    required_args.add_argument('--input_traj_path', required=True, help='Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.')
    parser.add_argument('--input_index_path', required=False, help="Path to the GROMACS index file. Accepted formats: ndx.")
    required_args.add_argument('--output_pdb_path', required=True, help='Path to the output cluster file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    #Specific call of each building block
    GMXCluster(input_structure_path=args.input_structure_path, input_traj_path=args.input_traj_path, 
               output_pdb_path=args.output_pdb_path, input_index_path=args.input_index_path, 
               properties=properties).launch()

if __name__ == '__main__':
    main()
