#!/usr/bin/env python3

"""Module containing the GMX Rms class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools.file_utils import launchlogger
from biobb_analysis.gromacs.common import *


class GMXRms(BiobbObject):
    """
    | biobb_analysis GMXRms
    | Wrapper of the GROMACS rms module for performing a Root Mean Square deviation (RMSd) analysis from a given GROMACS compatible trajectory.
    | `GROMACS rms <http://manual.gromacs.org/current/onlinehelp/gmx-rms.html>`_ compares two structures by computing the root mean square deviation (RMSD), the size-independent rho similarity parameter (rho) or the scaled rho (rhosc).

    Args:
        input_structure_path (str): Path to the input structure file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_traj_path (str): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_index_path (str) (Optional): Path to the GROMACS index file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx>`_. Accepted formats: ndx (edam:format_2033).
        output_xvg_path (str): Path to the XVG output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_rms.xvg>`_. Accepted formats: xvg (edam:format_2030).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **xvg** (*str*) - ("none") XVG plot formatting. Values: xmgrace, xmgr, none.
            * **selection** (*str*) - ("System") Group where the rms will be performed. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups), DNA (all DNA atoms), RNA (all RNA atoms), Protein_DNA (all Protein-DNA complex atoms), Protein_RNA (all Protein-RNA complex atoms), Protein_DNA_RNA (all Protein-DNA-RNA complex atoms), DNA_RNA (all DNA-RNA complex atoms).
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

            from biobb_analysis.gromacs.gmx_rms import gmx_rms
            prop = { 
                'xvg': 'xmgr', 
                'selection': 'Water_and_ions' 
            }
            gmx_rms(input_structure_path='/path/to/myStructure.tpr', 
                    input_traj_path='/path/to/myTrajectory.trr', 
                    output_xvg_path='/path/to/newXVG.xvg', 
                    input_index_path='/path/to/myIndex.ndx', 
                    properties=prop)

    Info:
        * wrapped_software:
            * name: GROMACS rms
            * version: >=2019.1
            * license: LGPL 2.1
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
            
    """

    def __init__(self, input_structure_path, input_traj_path,  output_xvg_path, 
                input_index_path=None, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = { 
            "in": { "input_structure_path": input_structure_path, "input_traj_path": input_traj_path, "input_index_path": input_index_path }, 
            "out": { "output_xvg_path": output_xvg_path } 
        }

        # Properties specific for BB
        self.xvg = properties.get('xvg', "none")
        self.selection = properties.get('selection', "System")
        self.properties = properties

        # Properties common in all GROMACS BB
        self.binary_path = get_binary_path(properties, 'binary_path')

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_structure_path"] = check_input_path(self.io_dict["in"]["input_structure_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_traj_path"] = check_traj_path(self.io_dict["in"]["input_traj_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_index_path"] = check_index_path(self.io_dict["in"]["input_index_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_xvg_path"] = check_out_xvg_path(self.io_dict["out"]["output_xvg_path"], out_log, self.__class__.__name__)
        self.xvg = get_xvg(self.properties, out_log, self.__class__.__name__)
        if not self.io_dict["in"]["input_index_path"]:
            self.selection = get_selection(self.properties, out_log, self.__class__.__name__)
        else:
            self.selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'selection', out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`GMXRms <gromacs.gmx_rms.GMXRms>` gromacs.gmx_rms.GMXRms object."""

        # standard input
        self.io_dict['in']['stdin_file_path'] = fu.create_stdin_file(f'{self.selection} {self.selection}')

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        self.cmd = [self.binary_path, 'rms',
               '-s', self.stage_io_dict["in"]["input_structure_path"],
               '-f', self.stage_io_dict["in"]["input_traj_path"],
               '-o', self.stage_io_dict["out"]["output_xvg_path"],
               '-xvg', self.xvg]

        if self.stage_io_dict["in"]["input_index_path"]:
            self.cmd.extend(['-n', self.stage_io_dict["in"]["input_index_path"]])

        # Add stdin input file
        self.cmd.append('<')
        self.cmd.append(self.stage_io_dict["in"]["stdin_file_path"])

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()
       
        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            self.io_dict['in'].get("stdin_file_path")
        ])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code

def gmx_rms(input_structure_path: str, input_traj_path: str, output_xvg_path: str, input_index_path: str = None, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`GMXRms <gromacs.gmx_rms.GMXRms>` class and
    execute the :meth:`launch() <gromacs.gmx_rms.GMXRms.launch>` method."""

    return GMXRms(input_structure_path=input_structure_path, 
                    input_traj_path = input_traj_path,
                    output_xvg_path=output_xvg_path,
                    input_index_path=input_index_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Performs a Root Mean Square deviation (RMSd) analysis from a given GROMACS compatible trajectory.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_structure_path', required=True, help='Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.')
    required_args.add_argument('--input_traj_path', required=True, help='Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.')
    parser.add_argument('--input_index_path', required=False, help="Path to the GROMACS index file. Accepted formats: ndx.")
    required_args.add_argument('--output_xvg_path', required=True, help='Path to the XVG output file. Accepted formats: xvg.')


    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    #Specific call of each building block
    gmx_rms(input_structure_path=args.input_structure_path, 
            input_traj_path=args.input_traj_path, 
            output_xvg_path=args.output_xvg_path, 
            input_index_path=args.input_index_path, 
            properties=properties)

if __name__ == '__main__':
    main()
