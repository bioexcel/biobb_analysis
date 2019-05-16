#!/usr/bin/env python3

"""Module containing the GMX Energy class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.gromacs.common import *


class GMXEnergy():
    """Wrapper of the GROMACS energy (http://manual.gromacs.org/current/onlinehelp/gmx-energy.html) module.

    Args:
        input_energy_path (str): Path to the input EDR file.
        output_xvg_path (str): Path to the XVG output file.
        properties (dic):
            * **xvg** (*str*) - ("none") XVG plot formatting: xmgrace, xmgr, none.
            * **terms** (*list*) - (["Potential"]) Energy terms. Select one or more from: Angle, Proper-Dih., Improper-Dih., LJ-14, Coulomb-14, LJ-(SR), Coulomb-(SR), Coul.-recip., Position-Rest., Potential, Kinetic-En., Total-Energy, Temperature, Pressure,  Constr.-rmsd, Box-X, Box-Y,  Box-Z, Volume, Density, pV, Enthalpy, Vir-XX, Vir-XY, Vir-XZ, Vir-YX, Vir-YY, Vir-YZ, Vir-ZX, Vir-ZY, Vir-ZZ, Pres-XX, Pres-XY, Pres-XZ, Pres-YX, Pres-YY,  Pres-YZ, Pres-ZX, Pres-ZY, Pres-ZZ, #Surf*SurfTen, Box-Vel-XX, Box-Vel-YY, Box-Vel-ZZ, Mu-X, Mu-Y, Mu-Z, T-Protein, T-non-Protein, Lamb-Protein, Lamb-non-Protein
            * **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
    """

    def __init__(self, input_energy_path, output_xvg_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_energy_path = input_energy_path
        self.output_xvg_path = output_xvg_path

        # Properties specific for BB
        self.instructions_file = get_default_value('instructions_file')
        self.properties = properties

        # Properties common in all GROMACS BB
        self.gmx_path = get_binary_path(properties, 'gmx_path')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

        # Check the properties
        fu.check_properties(self, properties)

    def check_data_params(self):
        """ Checks all the input/output paths and parameters """
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)
        self.input_energy_path = check_energy_path(self.input_energy_path, out_log, self.__class__.__name__)
        self.output_xvg_path = check_out_xvg_path(self.output_xvg_path, out_log, self.__class__.__name__)
        self.xvg = get_xvg(self.properties, out_log, self.__class__.__name__)
        self.terms = get_terms(self.properties, out_log, self.__class__.__name__)

    def create_instructions_file(self):
        """Creates an input file using the properties file settings"""
        instructions_list = []
        self.instructions_file = os.path.join(fu.create_unique_dir(), self.instructions_file)
        fu.create_name(prefix=self.prefix, step=self.step, name=self.instructions_file)

        for t in self.terms:
            instructions_list.append(t)

        # create instructions file
        with open(self.instructions_file, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return self.instructions_file

    def launch(self):
        """Launches the execution of the GROMACS energy module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        # check input/output paths and parameters
        self.check_data_params()

        # create instructions file
        self.create_instructions_file() 

        cmd = [self.gmx_path, 'energy',
               '-f', self.input_energy_path,
               '-o', self.output_xvg_path,
               '-xvg', self.xvg,
               '<', self.instructions_file]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        remove_tmp_files([os.path.dirname(self.instructions_file)], out_log)
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the GROMACS energy module.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_energy_path', required=True, help='Path to the input EDR file.')
    required_args.add_argument('--output_xvg_path', required=True, help='Path to the XVG output file.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    GMXEnergy(input_energy_path=args.input_energy_path, output_xvg_path=args.output_xvg_path, properties=properties).launch()

if __name__ == '__main__':
    main()
