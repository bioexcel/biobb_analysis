#!/usr/bin/env python3

"""Module containing the GMX Rmsf class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_analysis.gromacs.common import get_selection_index_file, get_xvg, get_selection


class GMXRmsf(BiobbObject):
    """
    | biobb_analysis GMXRmsf
    | Wrapper of the GROMACS rmsf module for performing a Root Mean Square Fluctuation (RMSF) analysis from a given GROMACS compatible trajectory.
    | `GROMACS rmsf <http://manual.gromacs.org/current/onlinehelp/gmx-rmsf.html>`_ computes the root mean square fluctuation (RMSF) of the atomic positions over the trajectory.

    Args:
        input_structure_path (str): Path to the input structure file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_traj_path (str): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_index_path (str) (Optional): Path to the GROMACS index file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx>`_. Accepted formats: ndx (edam:format_2033).
        output_xvg_path (str): Path to the XVG output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_rms.xvg>`_. Accepted formats: xvg (edam:format_2030).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **xvg** (*str*) - ("none") XVG plot formatting. Values: xmgrace, xmgr, none.
            * **selection** (*str*) - ("System") Group where the rmsf will be performed. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups), DNA (all DNA atoms), RNA (all RNA atoms), Protein_DNA (all Protein-DNA complex atoms), Protein_RNA (all Protein-RNA complex atoms), Protein_DNA_RNA (all Protein-DNA-RNA complex atoms), DNA_RNA (all DNA-RNA complex atoms).
            * **binary_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('gromacs/gromacs:2022.2') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_analysis.gromacs.gmx_rmsf import gmx_rmsf
            prop = {
                'xvg': 'xmgr',
                'selection': 'Water_and_ions'
            }
            gmx_rmsf(input_structure_path='/path/to/myStructure.tpr',
                    input_traj_path='/path/to/myTrajectory.trr',
                    output_xvg_path='/path/to/newXVG.xvg',
                    input_index_path='/path/to/myIndex.ndx',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: GROMACS rmsf
            * version: >=2024.5
            * license: LGPL 2.1
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_structure_path, input_traj_path, output_xvg_path,
                 input_index_path=None, properties=None, **kwargs) -> None:
        super().__init__(**locals())

        # Properties common in all GROMACS BB

    def prepare(self):
        """ Checks all the input/output paths and parameters """
        self.xvg = get_xvg(self.properties, self.out_log, self.__class__.__name__)
        if not self.io_dict["in"]["input_index_path"]:
            self.selection = get_selection(self.properties, self.out_log, self.__class__.__name__)
        else:
            self.selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'selection', self.out_log, self.__class__.__name__)
        # standard input
        self.io_dict['in']['stdin_file_path'] = fu.create_stdin_file(f'{self.selection} {self.selection}')

    def run(self) -> None:
        """Execute the :class:`GMXRmsf <gromacs.gmx_rmsf.GMXRmsf>` object."""

        self.cmd = [self.binary_path, 'rmsf',
                    '-s', self.stage_io_dict["in"]["input_structure_path"],
                    '-f', self.stage_io_dict["in"]["input_traj_path"],
                    '-o', self.stage_io_dict["out"]["output_xvg_path"],
                    '-xvg', self.xvg]

        if self.stage_io_dict["in"].get("input_index_path"):
            self.cmd.extend(['-n', self.stage_io_dict["in"]["input_index_path"]])

        # Add stdin input file
        self.cmd.append('<')
        self.cmd.append(self.stage_io_dict["in"]["stdin_file_path"])

        # Run Biobb block
        self.run_biobb()

        self.tmp_files.append(self.io_dict['in'].get("stdin_file_path", ""))


def gmx_rmsf(input_structure_path: str, input_traj_path: str, output_xvg_path: str, input_index_path: Optional[str] = None, properties: Optional[dict] = None, **kwargs) -> int:
    """Create the :class:`GMXRmsf <gromacs.gmx_rmsf.GMXRmsf>` class and
    execute the :meth:`launch() <gromacs.gmx_rmsf.GMXRmsf.launch>` method."""
    return GMXRmsf(**dict(locals())).launch()


gmx_rmsf.__doc__ = GMXRmsf.__doc__
main = GMXRmsf.get_main(gmx_rmsf, "Performs a Root Mean Square fluctuation (RMSF) analysis from a given GROMACS compatible trajectory.")

if __name__ == '__main__':
    main()
