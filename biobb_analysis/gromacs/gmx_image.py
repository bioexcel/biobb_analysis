#!/usr/bin/env python3

"""Module containing the GMX TrjConvStr class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu
from biobb_analysis.gromacs.common import get_image_selection, get_selection_index_file, get_pbc, get_center, get_ur, get_fit


class GMXImage(BiobbObject):
    """
    | biobb_analysis GMXImage
    | Wrapper of the GROMACS trjconv module for correcting periodicity (image) from a given GROMACS compatible trajectory file.
    | GROMACS trjconv module can convert trajectory files in many ways. See the `GROMACS trjconv <http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-trjconv.html>`_ official documentation for further information.

    Args:
        input_traj_path (str): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_top_path (str): Path to the GROMACS input topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_index_path (str) (Optional): Path to the GROMACS index file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx>`_. Accepted formats: ndx (edam:format_2033).
        output_traj_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_image.xtc>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **fit_selection** (*str*) - ("System") Group where the fitting will be performed. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups), DNA (all DNA atoms), RNA (all RNA atoms), Protein_DNA (all Protein-DNA complex atoms), Protein_RNA (all Protein-RNA complex atoms), Protein_DNA_RNA (all Protein-DNA-RNA complex atoms), DNA_RNA (all DNA-RNA complex atoms).
            * **center_selection** (*str*) - ("System") Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups), DNA (all DNA atoms), RNA (all RNA atoms), Protein_DNA (all Protein-DNA complex atoms), Protein_RNA (all Protein-RNA complex atoms), Protein_DNA_RNA (all Protein-DNA-RNA complex atoms), DNA_RNA (all DNA-RNA complex atoms).
            * **cluster_selection** (*str*) - ("System") Group assigned to be the cluster, onto which all atoms are wrapped around the box, such that they are closest to the center of mass of the cluster, which is iteratively updated. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups), DNA (all DNA atoms), RNA (all RNA atoms), Protein_DNA (all Protein-DNA complex atoms), Protein_RNA (all Protein-RNA complex atoms), Protein_DNA_RNA (all Protein-DNA-RNA complex atoms), DNA_RNA (all DNA-RNA complex atoms).
            * **output_selection** (*str*) - ("System") Group that is going to be written in the output trajectory. If **input_index_path** provided, check the file for the accepted values. Values: System (all atoms in the system), Protein (all protein atoms), Protein-H (protein atoms excluding hydrogens), C-alpha (C-alpha atoms), Backbone (protein backbone atoms: N; C-alpha and C), MainChain (protein main chain atoms: N; C-alpha; C and O; including oxygens in C-terminus), MainChain+Cb (protein main chain atoms including C-beta), MainChain+H (protein main chain atoms including backbone amide hydrogens and hydrogens on the N-terminus), SideChain (protein side chain atoms: that is all atoms except N; C-alpha; C; O; backbone amide hydrogens and oxygens in C-terminus and hydrogens on the N-terminus), SideChain-H (protein side chain atoms excluding all hydrogens), Prot-Masses (protein atoms excluding dummy masses), non-Protein (all non-protein atoms), Water (water molecules), SOL (water molecules), non-Water (anything not covered by the Water group), Ion (any name matching an Ion entry in residuetypes.dat), NA (all NA atoms), CL (all CL atoms), Water_and_ions (combination of the Water and Ions groups), DNA (all DNA atoms), RNA (all RNA atoms), Protein_DNA (all Protein-DNA complex atoms), Protein_RNA (all Protein-RNA complex atoms), Protein_DNA_RNA (all Protein-DNA-RNA complex atoms), DNA_RNA (all DNA-RNA complex atoms).
            * **pbc** (*str*) - ("mol") PBC treatment (see help text for full description). Values: none (No PBC treatment), mol (Puts the center of mass of molecules in the box), res (Puts the center of mass of residues in the box), atom (Puts all the atoms in the box), nojump (Checks if atoms jump across the box and then puts them back), cluster (Clusters all the atoms in the selected index such that they are all closest to the center of mass of the cluster which is iteratively updated), whole (Only makes broken molecules whole).
            * **center** (*bool*) - (True) Center atoms in box.
            * **ur** (*str*) - ("compact") Unit-cell representation. Values: rect (It's the ordinary brick shape), tric (It's the triclinic unit cell), compact (Puts all atoms at the closest distance from the center of the box).
            * **fit** (*str*) - ("none") Fit molecule to ref structure in the structure file. Values: none, rot+trans, rotxy+transxy, translation, transxy, progressive.
            * **binary_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('gromacs/gromacs:2022.2') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_analysis.gromacs.gmx_image import gmx_image
            prop = {
                'fit_selection': 'System',
                'center_selection': 'Water_and_ions',
                'output_selection': 'System',
                'pbc': 'mol'
            }
            gmx_image(input_traj_path='/path/to/myTrajectory.trr',
                        input_top_path='/path/to/myTopology.tpr',
                        output_traj_path='/path/to/newTrajectory.xtc',
                        input_index_path='/path/to/myIndex.ndx',
                        properties=prop)

    Info:
        * wrapped_software:
            * name: GROMACS trjconv
            * version: >=2024.5
            * license: LGPL 2.1
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_traj_path: str, input_top_path: str, output_traj_path: str,
                 input_index_path: Optional[str] = None, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

        # Properties common in all GROMACS BB

    def prepare(self):
        """ Checks all the input/output paths and parameters """
        if not self.io_dict["in"]["input_index_path"]:
            if self.fit != 'none':
                self.fit_selection = get_image_selection(self.properties, 'fit_selection', self.out_log, self.__class__.__name__)
            if self.fit != 'none' or self.center:
                self.center_selection = get_image_selection(self.properties, 'center_selection', self.out_log, self.__class__.__name__)
            if self.pbc == 'cluster':
                self.cluster_selection = get_image_selection(self.properties, 'cluster_selection', self.out_log, self.__class__.__name__)
            self.output_selection = get_image_selection(self.properties, 'output_selection', self.out_log, self.__class__.__name__)
        else:
            self.fit_selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'fit_selection', self.out_log, self.__class__.__name__)
            self.center_selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'center_selection', self.out_log, self.__class__.__name__)
            if self.pbc == 'cluster':
                self.cluster_selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'cluster_selection', self.out_log, self.__class__.__name__)
            self.output_selection = get_selection_index_file(self.properties, self.io_dict["in"]["input_index_path"], 'output_selection', self.out_log, self.__class__.__name__)
        self.pbc = get_pbc(self.properties, self.out_log, self.__class__.__name__)
        self.center = get_center(self.properties, self.out_log, self.__class__.__name__)
        self.ur = get_ur(self.properties, self.out_log, self.__class__.__name__)
        self.fit = get_fit(self.properties, self.out_log, self.__class__.__name__)
        # If fitting provided, echo fit_selection
        if self.fit == 'none':
            if self.center:
                selections = self.center_selection + ' ' + self.output_selection
            elif self.pbc == 'cluster':
                selections = self.cluster_selection + ' ' + self.output_selection
            else:
                selections = self.output_selection
        else:
            if self.center:
                selections = self.fit_selection + ' ' + self.center_selection + ' ' + self.output_selection
            else:
                selections = self.fit_selection + ' ' + self.output_selection
        # standard input
        self.io_dict['in']['stdin_file_path'] = fu.create_stdin_file(f'{selections}')

    def run(self) -> None:
        """Execute the :class:`GMXImage <gromacs.gmx_image.GMXImage>` object."""

        self.cmd = [self.binary_path, 'trjconv',
                    '-f', self.stage_io_dict["in"]["input_traj_path"],
                    '-s', self.stage_io_dict["in"]["input_top_path"],
                    '-fit', self.fit,
                    '-o', self.stage_io_dict["out"]["output_traj_path"]]

        if self.stage_io_dict["in"].get("input_index_path"):
            self.cmd.extend(['-n', self.stage_io_dict["in"]["input_index_path"]])

        self.cmd.append('-center' if self.center else '-nocenter')

        # Unit-cell representation, PBC treatment is incompatible with fitting
        if self.fit == 'none':
            self.cmd.append('-pbc')
            self.cmd.append(self.pbc)
            self.cmd.append('-ur')
            self.cmd.append(self.ur)

        # Add stdin input file
        self.cmd.append('<')
        self.cmd.append(self.stage_io_dict["in"]["stdin_file_path"])

        # Run Biobb block
        self.run_biobb()
        # Remove temporal files
        self.tmp_files.append(self.io_dict['in'].get("stdin_file_path", ""))


gmx_image = launcher(GMXImage)

if __name__ == '__main__':
    GMXImage.main()
