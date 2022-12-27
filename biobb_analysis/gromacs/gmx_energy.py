#!/usr/bin/env python3

"""Module containing the GMX Energy class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_analysis.gromacs.common import *


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
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('gromacs/gromacs:2022.2') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
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
            * version: >=2019.1
            * license: LGPL 2.1
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_energy_path, output_xvg_path,
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = { 
            "in": { "input_energy_path": input_energy_path }, 
            "out": { "output_xvg_path": output_xvg_path } 
        }

        # Properties specific for BB
        self.xvg = properties.get('xvg', "none")
        self.terms = properties.get('terms', ["Potential"])
        self.instructions_file = get_default_value('instructions_file')
        self.properties = properties

        # Properties common in all GROMACS BB
        self.binary_path = get_binary_path(properties, 'binary_path')

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_energy_path"] = check_energy_path(self.io_dict["in"]["input_energy_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_xvg_path"] = check_out_xvg_path(self.io_dict["out"]["output_xvg_path"], out_log, self.__class__.__name__)
        self.xvg = get_xvg(self.properties, out_log, self.__class__.__name__)
        self.terms = get_terms(self.properties, out_log, self.__class__.__name__)

    def create_instructions_file(self):
        """Creates an input file using the properties file settings"""
        instructions_list = []
        # different path if container execution or not
        if self.container_path:
            self.instructions_file = str(PurePath(self.container_volume_path).joinpath(self.instructions_file))
        else:
            self.instructions_file = str(PurePath(fu.create_unique_dir()).joinpath(self.instructions_file))
        #self.instructions_file = str(PurePath(fu.create_unique_dir()).joinpath(self.instructions_file))
        fu.create_name(prefix=self.prefix, step=self.step, name=self.instructions_file)

        for t in self.terms:
            instructions_list.append(t)

        # create instructions file
        with open(self.instructions_file, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return self.instructions_file

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`GMXEnergy <gromacs.gmx_energy.GMXEnergy>` gromacs.gmx_energy.GMXEnergy object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        # create instructions file
        self.create_instructions_file()

        # if container execution, copy intructions file to container
        if self.container_path:
            copy_instructions_file_to_container(self.instructions_file, self.stage_io_dict.get("unique_dir"))

        self.cmd = [self.binary_path, 'energy',
               '-f', self.stage_io_dict["in"]["input_energy_path"],
               '-o', self.stage_io_dict["out"]["output_xvg_path"],
               '-xvg', self.xvg,
               '<', self.instructions_file]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            str(PurePath(self.instructions_file).parent)
        ])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code

def gmx_energy(input_energy_path: str, output_xvg_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`GMXEnergy <gromacs.gmx_energy.GMXEnergy>` class and
    execute the :meth:`launch() <gromacs.gmx_energy.GMXEnergy.launch>` method."""

    return GMXEnergy(input_energy_path=input_energy_path, 
                    output_xvg_path=output_xvg_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Extracts energy components from a given GROMACS energy file.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_energy_path', required=True, help='Path to the input EDR file. Accepted formats: edr.')
    required_args.add_argument('--output_xvg_path', required=True, help='Path to the XVG output file. Accepted formats: xvg.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    #Specific call of each building block
    gmx_energy(input_energy_path=args.input_energy_path, 
                output_xvg_path=args.output_xvg_path, 
                properties=properties)

if __name__ == '__main__':
    main()
