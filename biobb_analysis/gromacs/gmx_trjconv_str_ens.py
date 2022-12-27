#!/usr/bin/env python3

"""Module containing the GMX TrjConvStr class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_analysis.gromacs.common import *


class GMXTrjConvStrEns(BiobbObject):
    """
    | biobb_analysis GMXTrjConvStrEns
    | Wrapper of the GROMACS trjconv module for extracting an ensemble of frames containing a selection of atoms from GROMACS compatible trajectory files.
    | GROMACS trjconv module can convert trajectory files in many ways. See the `GROMACS trjconv <http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-trjconv.html>`_ official documentation for further information.

    Args:
        input_traj_path (str): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_top_path (str): Path to the GROMACS input topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_index_path (str) (Optional): Path to the GROMACS index file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx>`_. Accepted formats: ndx (edam:format_2033).
        output_str_ens_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_trjconv.str.ens.zip>`_. Accepted formats: zip (edam:format_3987).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **selection** (*str*) - ("System") Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups), DNA (all DNA atoms), RNA (all RNA atoms), Protein_DNA (all Protein-DNA complex atoms), Protein_RNA (all Protein-RNA complex atoms), Protein_DNA_RNA (all Protein-DNA-RNA complex atoms), DNA_RNA (all DNA-RNA complex atoms).
            * **skip** (*int*) - (1) [0~10000|1] Only write every nr-th frame.
            * **start** (*int*) - (0) [0~10000|1] Time of first frame to read from trajectory (default unit ps).
            * **end** (*int*) - (0) [0~10000|1] Time of last frame to read from trajectory (default unit ps).
            * **dt** (*int*) - (0) [0~10000|1] Only write frame when t MOD dt = first time (ps).
            * **output_name** (*str*) - ("output") File name for ensemble of output files.
            * **output_type** (*str*) - ("pdb") File type for ensemble of output files. Values: gro (Contains a molecular structure in Gromos87 format), g96 (Can be a GROMOS-96 initial/final configuration file or a coordinate trajectory file or a combination of both), pdb (Molecular structure files in the protein databank file format).
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

            from biobb_analysis.gromacs.gmx_trjconv_str_ens import gmx_trjconv_str_ens
            prop = { 
                'selection': 'System', 
                'start': 0, 
                'end': 10, 
                'dt': 1 
            }
            gmx_trjconv_str_ens(input_traj_path='/path/to/myStructure.trr', 
                                input_top_path='/path/to/myTopology.tpr', 
                                output_str_ens_path='/path/to/newStructureEnsemble.zip', 
                                input_index_path='/path/to/myIndex.ndx', 
                                properties=prop)

    Info:
        * wrapped_software:
            * name: GROMACS trjconv
            * version: >=2019.1
            * license: LGPL 2.1
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
            
    """

    def __init__(self, input_traj_path, input_top_path, output_str_ens_path, 
                input_index_path=None, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = { 
            "in": { "input_traj_path": input_traj_path, "input_top_path": input_top_path, "input_index_path": input_index_path }, 
            "out": { "output_str_ens_path": output_str_ens_path } 
        }

        # Properties specific for BB
        self.selection = properties.get('selection', "System")
        self.skip = properties.get('skip', 1)
        self.start = properties.get('start', 0)
        self.end = properties.get('end', 0)
        self.dt = properties.get('dt', 0)
        self.output_name = properties.get('output_name', "output")
        self.output_type = properties.get('output_type', "pdb")
        self.properties = properties

        # Properties common in all GROMACS BB
        self.binary_path = get_binary_path(properties, 'binary_path')

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_traj_path"] = check_traj_path(self.io_dict["in"]["input_traj_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_top_path"] = check_input_path(self.io_dict["in"]["input_top_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_index_path"] = check_index_path(self.io_dict["in"]["input_index_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_str_ens_path"] = check_out_str_ens_path(self.io_dict["out"]["output_str_ens_path"], out_log, self.__class__.__name__)
        if not self.io_dict["in"]["input_index_path"]:
            self.selection = get_selection(self.properties, out_log, self.__class__.__name__)
        else:
            self.selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'selection', out_log, self.__class__.__name__)
        self.skip = get_skip(self.properties, out_log, self.__class__.__name__)
        self.start = get_start(self.properties, out_log, self.__class__.__name__)
        self.end = get_end(self.properties, out_log, self.__class__.__name__)
        self.dt = get_dt(self.properties, out_log, self.__class__.__name__)
        self.output_name = self.properties.get('output_name', 'output')
        self.output_type = get_ot_str_ens(self.properties, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`GMXTrjConvStrEns <gromacs.gmx_trjconv_str_ens.GMXTrjConvStrEns>` gromacs.gmx_trjconv_str_ens.GMXTrjConvStrEns object."""

        # standard input
        self.io_dict['in']['stdin_file_path'] = fu.create_stdin_file(f'{self.selection}')

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        # if container execution, output to container_volume_path, else to unique_dir
        if self.container_path:
            output = self.container_volume_path + '/' + self.output_name + '.' + self.output_type
        else:
            output = self.stage_io_dict.get("unique_dir") + '/' + self.output_name + '.' + self.output_type

        self.cmd = [self.binary_path, 'trjconv',
               '-f', self.stage_io_dict["in"]["input_traj_path"],
               '-s', self.stage_io_dict["in"]["input_top_path"],
               '-skip', self.skip,
               '-b', self.start,
               '-dt', self.dt,
               '-sep',
               '-o', output]

        # checking 'end' gromacs 'bug'
        if not str(self.end) =="0":
            self.cmd.append('-e')
            self.cmd.append(self.end)

        if self.stage_io_dict["in"]["input_index_path"]:
            self.cmd.extend(['-n', self.stage_io_dict["in"]["input_index_path"]])

        # Add stdin input file
        self.cmd.append('<')
        self.cmd.append(self.stage_io_dict["in"]["stdin_file_path"])

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        if self.container_path:
            process_output_trjconv_str_ens(self.stage_io_dict['unique_dir'], 
                                           self.io_dict["out"]["output_str_ens_path"],
                                           self.stage_io_dict.get("unique_dir"), 
                                           self.output_name + '*', self.out_log)
        else:
            process_output_trjconv_str_ens(self.stage_io_dict.get("unique_dir"), 
                                           self.stage_io_dict["out"]["output_str_ens_path"],
                                           self.io_dict["out"]["output_str_ens_path"], 
                                           'output*.pdb', self.out_log)

        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            self.io_dict['in'].get("stdin_file_path")
        ])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code

def gmx_trjconv_str_ens(input_traj_path: str, input_top_path: str, output_str_ens_path: str, input_index_path: str = None, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`GMXTrjConvStrEns <gromacs.gmx_trjconv_str_ens.GMXTrjConvStrEns>` class and
    execute the :meth:`launch() <gromacs.gmx_trjconv_str_ens.GMXTrjConvStrEns.launch>` method."""

    return GMXTrjConvStrEns(input_traj_path=input_traj_path, 
                    input_top_path = input_top_path,
                    output_str_ens_path=output_str_ens_path,
                    input_index_path=input_index_path,
                    properties=properties).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Extracts an ensemble of frames containing a selection of atoms from GROMACS compatible trajectory files.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_traj_path', required=True, help='Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.')
    required_args.add_argument('--input_top_path', required=True, help='Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.')
    parser.add_argument('--input_index_path', required=False, help="Path to the GROMACS index file. Accepted formats: ndx.")
    required_args.add_argument('--output_str_ens_path', required=True, help='Path to the output file. Accepted formats: zip.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    gmx_trjconv_str_ens(input_traj_path=args.input_traj_path, 
                        input_top_path=args.input_top_path, 
                        output_str_ens_path=args.output_str_ens_path,
                        input_index_path=args.input_index_path, 
                        properties=properties)


if __name__ == '__main__':
    main()
