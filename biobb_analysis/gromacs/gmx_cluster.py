#!/usr/bin/env python3

"""Module containing the GMX Cluster class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_analysis.gromacs.common import *


class GMXCluster(BiobbObject):
    """
    | biobb_analysis GMXCluster
    | Wrapper of the GROMACS cluster module for clustering structures from a given GROMACS compatible trajectory.
    | `GROMACS cluster <http://manual.gromacs.org/current/onlinehelp/gmx-cluster.html>`_ can cluster structures using several different methods. Distances between structures can be determined from a trajectory. RMS deviation after fitting or RMS deviation of atom-pair distances can be used to define the distance between structures.

    Args:
        input_structure_path (str): Path to the input structure file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_traj_path (str): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_index_path (str) (Optional): Path to the GROMACS index file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx>`_. Accepted formats: ndx (edam:format_2033).
        output_pdb_path (str): Path to the output cluster file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_cluster.pdb>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **fit_selection** (*str*) - ("System") Group where the fitting will be performed. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups).
            * **output_selection** (*str*) - ("System") Group that is going to be written in the output trajectory. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups).
            * **dista** (*bool*) - (False) Use RMSD of distances instead of RMS deviation.
            * **method** (*str*) - ("linkage") Method for cluster determination. Values: linkage (Add a structure to a cluster when its distance to any element of the cluster is less than cutoff), jarvis-patrick (Add a structure to a cluster when this structure and a structure in the cluster have each other as neighbors and they have a least P neighbors in common), monte-carlo (Reorder the RMSD matrix using Monte Carlo such that the order of the frames is using the smallest possible increments), diagonalization (Diagonalize the RMSD matrix), gromos (Count number of neighbors using cut-off and take structure with largest number of neighbors with all its neighbors as cluster and eliminate it from the pool of clusters).
            * **cutoff** (*float*) - (0.1) [0~10|0.1] RMSD cut-off (nm) for two structures to be neighbor.
            * **binary_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('gromacs/gromacs:2022.2') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_analysis.gromacs.gmx_cluster import gmx_cluster
            prop = { 
                'fit_selection': 'System', 
                'output_selection': 'System', 
                'method': 'linkage' 
            }
            gmx_cluster(input_structure_path='/path/to/myStructure.tpr', 
                        input_traj_path='/path/to/myTrajectory.trr', 
                        input_index_path='/path/to/myIndex.ndx', 
                        output_pdb_path='/path/to/newStructure.pdb', 
                        properties=prop)

    Info:
        * wrapped_software:
            * name: GROMACS cluster
            * version: >=2019.1
            * license: LGPL 2.1
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_structure_path, input_traj_path, output_pdb_path, 
                input_index_path=None, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = { 
            "in": { "input_structure_path": input_structure_path, "input_traj_path": input_traj_path, "input_index_path": input_index_path }, 
            "out": { "output_pdb_path": output_pdb_path } 
        }

        # Properties specific for BB
        self.fit_selection = properties.get('fit_selection', "System")
        self.output_selection = properties.get('output_selection', "System")
        self.method = properties.get('method', "linkage")
        self.dista = properties.get('dista', False)
        self.cutoff = properties.get('cutoff', 0.1)
        self.properties = properties

        # Properties common in all GROMACS BB
        self.binary_path = get_binary_path(properties, 'binary_path')
        
        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

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
    def launch(self) -> int:
        """Execute the :class:`GMXCluster <gromacs.gmx_cluster.GMXCluster>` gromacs.gmx_cluster.GMXCluster object."""

        # standard input
        self.io_dict['in']['stdin_file_path'] = fu.create_stdin_file(f'{self.fit_selection} {self.output_selection}')

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        # if container execution, add container_volume_path to log, xvg & xpm (because docker doesn't allow to write teses files out of the /tmp folder)
        if self.container_path:
            self.log_path = str(PurePath(self.container_volume_path).joinpath(self.log_path))
            self.xvg_path = str(PurePath(self.container_volume_path).joinpath(self.xvg_path))
            self.xpm_path = str(PurePath(self.container_volume_path).joinpath(self.xpm_path))

        self.cmd = [self.binary_path, 'cluster',
               '-g', self.log_path,
               '-dist', self.xvg_path,
               '-o', self.xpm_path,
               '-s', self.stage_io_dict["in"]["input_structure_path"],
               '-f', self.stage_io_dict["in"]["input_traj_path"],
               '-cl', self.stage_io_dict["out"]["output_pdb_path"],
               '-cutoff', str(self.cutoff),
               '-method', self.method]

        if self.stage_io_dict["in"]["input_index_path"]:
            self.cmd.extend(['-n', self.stage_io_dict["in"]["input_index_path"]])

        if self.dista:
            self.cmd.append('-dista')

        # Add stdin input file
        self.cmd.append('<')
        self.cmd.append(self.stage_io_dict["in"]["stdin_file_path"])

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            self.io_dict['in'].get("stdin_file_path"),
            'rmsd-clust.xpm', 
            'rmsd-dist.xvg', 
            'cluster.log'
        ])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code

def gmx_cluster(input_structure_path: str, input_traj_path: str, output_pdb_path: str, input_index_path: str = None, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`GMXCluster <gromacs.gmx_cluster.GMXCluster>` class and
    execute the :meth:`launch() <gromacs.gmx_cluster.GMXCluster.launch>` method."""

    return GMXCluster(input_structure_path=input_structure_path, 
                    input_traj_path=input_traj_path, 
                    output_pdb_path=output_pdb_path,
                    input_index_path=input_index_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
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
    gmx_cluster(input_structure_path=args.input_structure_path, 
                input_traj_path=args.input_traj_path, 
                output_pdb_path=args.output_pdb_path, 
                input_index_path=args.input_index_path, 
                properties=properties)

if __name__ == '__main__':
    main()
