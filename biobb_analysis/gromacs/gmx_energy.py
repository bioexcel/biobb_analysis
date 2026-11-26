#!/usr/bin/env python3

"""Module containing the GMX Energy class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu

from biobb_analysis.gromacs.common import (
    get_default_value,
    get_terms,
    get_xvg,
)


class GMXEnergy(BiobbObject):
    """
    | biobb_analysis GMXEnergy
    | Wrapper of the GROMACS energy module for extracting energy components from a given GROMACS energy file.
    | `GROMACS energy <http://manual.gromacs.org/current/onlinehelp/gmx-energy.html>`_ extracts energy components from an energy file. The user is prompted to interactively select the desired energy terms.

    Args:
        input_energy_path (str): Path to the input EDR file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/energy.edr>`_. Accepted formats: edr (edam:format_2330).
        output_xvg_path (str): Path to the XVG output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_energy.xvg>`_. Accepted formats: xvg (edam:format_2030).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **xvg** (*str*) - ("none") XVG plot formatting. Values: xmgrace, xmgr, none.
            * **terms** (*list*) - (["Potential"]) Energy terms. Values: Angle, Proper-Dih., Improper-Dih., LJ-14, Coulomb-14, LJ-\(SR\), Coulomb-\(SR\), Coul.-recip., Position-Rest., Potential, Kinetic-En., Total-Energy, Temperature, Pressure,  Constr.-rmsd, Box-X, Box-Y,  Box-Z, Volume, Density, pV, Enthalpy, Vir-XX, Vir-XY, Vir-XZ, Vir-YX, Vir-YY, Vir-YZ, Vir-ZX, Vir-ZY, Vir-ZZ, Pres-XX, Pres-XY, Pres-XZ, Pres-YX, Pres-YY,  Pres-YZ, Pres-ZX, Pres-ZY, Pres-ZZ, #Surf*SurfTen, Box-Vel-XX, Box-Vel-YY, Box-Vel-ZZ, Mu-X, Mu-Y, Mu-Z, T-Protein, T-non-Protein, Lamb-Protein, Lamb-non-Protein.
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

            from biobb_analysis.gromacs.gmx_energy import gmx_energy
            prop = {
                'xvg': 'xmgr',
                'terms': ['Potential', 'Pressure']
            }
            gmx_energy(input_energy_path='/path/to/myEnergyFile.edr',
                        output_xvg_path='/path/to/newXVG.xvg',
                        properties=prop)

    Info:
        * wrapped_software:
            * name: GROMACS energy
            * version: >=2024.5
            * license: LGPL 2.1
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(
        self, input_energy_path: str, output_xvg_path: str, properties: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**locals())

        # Properties specific for BB
        self.terms = fu.str_to_list(self.terms)
        self.instructions_file = get_default_value("instructions_file")

        # Properties common in all GROMACS BB

    def prepare(self):
        """Checks all the input/output paths and parameters"""
        self.xvg = get_xvg(self.properties, self.out_log, self.__class__.__name__)
        self.terms = get_terms(self.terms, self.out_log, self.__class__.__name__)

    def create_instructions_file(self):
        """Creates an input file using the properties file settings"""
        instructions_list = []
        # Instructions file in the sandbox, and its path for the command (inside the container if any)
        self.instructions_file = self.create_tmp_file(self.instructions_file)
        self.instructions_file_path = self.staged_path(self.instructions_file)

        for t in self.terms:
            instructions_list.append(t)

        # create instructions file
        with open(self.instructions_file, "w") as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + "\n")

        return self.instructions_file_path

    def run(self) -> None:
        """Execute the :class:`GMXEnergy <gromacs.gmx_energy.GMXEnergy>` object."""

        # create instructions file
        self.create_instructions_file()

        self.cmd = [
            self.binary_path,
            "energy",
            "-f",
            self.stage_io_dict["in"]["input_energy_path"],
            "-o",
            self.stage_io_dict["out"]["output_xvg_path"],
            "-xvg",
            self.xvg,
            "<",
            self.instructions_file_path,
        ]

        # Run Biobb block
        self.run_biobb()


gmx_energy = launcher(GMXEnergy)

if __name__ == "__main__":
    GMXEnergy.main()
