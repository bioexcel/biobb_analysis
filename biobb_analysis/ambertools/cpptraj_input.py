#!/usr/bin/env python3

"""Module containing the Cpptraj Input class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_analysis.ambertools.common import *


class CpptrajInput(BiobbObject):
    """
    | biobb_analysis CpptrajInput
    | Wrapper of the Ambertools Cpptraj module for performing multiple analysis and trajectory operations of a given trajectory.
    | Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files. The parameter names and defaults are the same as the ones in the official `Cpptraj manual <https://amber-md.github.io/cpptraj/CPPTRAJ.xhtml>`_.

    Args:
        input_instructions_path (str): Path of the instructions file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.in>`_. Accepted formats: in (edam:format_2033).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **binary_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_analysis.ambertools.cpptraj_input import cpptraj_input
            prop = { }
            cpptraj_input(input_instructions_path='/path/to/myInstructions.in', 
                            properties=prop)

    Info:
        * wrapped_software:
            * name: Ambertools Cpptraj
            * version: >=20.0
            * license: GNU
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
            
    """

    def __init__(self, input_instructions_path=None, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Properties specific for BB
        self.input_instructions_path = input_instructions_path
        self.input_top_path = kwargs.get('input_top_path')
        self.input_traj_path = kwargs.get('input_traj_path')
        self.output_cpptraj_path = kwargs.get('output_cpptraj_path')
        self.properties = properties
        self.binary_path = properties.get('binary_path', 'cpptraj')

        # Check the properties
        self.check_properties(properties)

    def create_instrucions_file(self):
        """ Creates an input file using paths provideed in the configuration file (only used for test purposes) """
        instructions_list = []
        output_instructions_path = fu.create_name(prefix=self.prefix, step=self.step, name=get_default_value("instructions_file"))

        instructions_list.append('parm ' + self.input_top_path)
        instructions_list.append('trajin ' + self.input_traj_path)
        instructions_list.append('trajout ' + self.output_cpptraj_path + ' ' + get_default_value("format"))

        with open(output_instructions_path, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return output_instructions_path

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`CpptrajInput <ambertools.cpptraj_input.CpptrajInput>` ambertools.cpptraj_input.CpptrajInput object."""
        
        # Get local loggers from launchlogger decorator

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        output_instructions_path = self.create_instrucions_file() if not self.input_instructions_path else self.input_instructions_path
        check_in_path(output_instructions_path, self.out_log, self.__class__.__name__)

        # create cmd and launch execution
        self.cmd = [self.binary_path, '-i', output_instructions_path]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        return self.return_code

def cpptraj_input(input_instructions_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`CpptrajInput <ambertools.cpptraj_input.CpptrajInput>` class and
    execute the :meth:`launch() <ambertools.cpptraj_input.CpptrajInput.launch>` method."""

    return CpptrajInput(input_instructions_path=input_instructions_path,
                        properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Performs multiple analysis and trajectory operations of a given trajectory.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_instructions_path', required=True, help='Path of the instructions file.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    #Specific call of each building block
    cpptraj_input(input_instructions_path=args.input_instructions_path, 
                properties=properties)

if __name__ == '__main__':
    main()