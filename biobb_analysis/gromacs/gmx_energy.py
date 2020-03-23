#!/usr/bin/env python3

"""Module containing the GMX Energy class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.gromacs.common import *


class GMXEnergy():
    """Extracts energy components from a given GROMACS energy file.
    Wrapper of the `GROMACS energy <http://manual.gromacs.org/current/onlinehelp/gmx-energy.html>`_ module.

    Args:
        input_energy_path (str): Path to the input EDR file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/energy.edr>`_. Accepted formats: edr.
        output_xvg_path (str): Path to the XVG output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_energy.xvg>`_. Accepted formats: xvg.
        properties (dic):
            * **xvg** (*str*) - ("none") XVG plot formatting. Values: xmgrace, xmgr, none.
            * **terms** (*list*) - (["Potential"]) Energy terms. Values: Angle, Proper-Dih., Improper-Dih., LJ-14, Coulomb-14, LJ-(SR), Coulomb-(SR), Coul.-recip., Position-Rest., Potential, Kinetic-En., Total-Energy, Temperature, Pressure,  Constr.-rmsd, Box-X, Box-Y,  Box-Z, Volume, Density, pV, Enthalpy, Vir-XX, Vir-XY, Vir-XZ, Vir-YX, Vir-YY, Vir-YZ, Vir-ZX, Vir-ZY, Vir-ZZ, Pres-XX, Pres-XY, Pres-XZ, Pres-YX, Pres-YY,  Pres-YZ, Pres-ZX, Pres-ZY, Pres-ZZ, #Surf*SurfTen, Box-Vel-XX, Box-Vel-YY, Box-Vel-ZZ, Mu-X, Mu-Y, Mu-Z, T-Protein, T-non-Protein, Lamb-Protein, Lamb-non-Protein.
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

    def __init__(self, input_energy_path, output_xvg_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_energy_path": input_energy_path }, 
            "out": { "output_xvg_path": output_xvg_path } 
        }

        # Properties specific for BB
        self.instructions_file = get_default_value('instructions_file')
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
    def launch(self):
        """Launches the execution of the GROMACS energy module."""

        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        # Restart
        if self.restart:
            output_file_list = [self.io_dict["out"]["output_xvg_path"]]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # copy inputs to container
        container_io_dict = fu.copy_to_container(self.container_path, self.container_volume_path, self.io_dict)

        # create instructions file
        self.create_instructions_file()

        # if container execution, copy intructions file to container
        if self.container_path:
            copy_instructions_file_to_container(self.instructions_file, container_io_dict['unique_dir'])

        cmd = [self.gmx_path, 'energy',
               '-f', container_io_dict["in"]["input_energy_path"],
               '-o', container_io_dict["out"]["output_xvg_path"],
               '-xvg', self.xvg,
               '<', self.instructions_file]

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

        if self.remove_tmp:
            remove_tmp_files([PurePath(self.instructions_file).parent], self.remove_tmp, out_log)

        return returncode

def main():
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
    GMXEnergy(input_energy_path=args.input_energy_path, output_xvg_path=args.output_xvg_path, 
              properties=properties).launch()

if __name__ == '__main__':
    main()
