#!/usr/bin/env python3

"""Module containing the Cpptraj Image class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_analysis.ambertools.common import *


class CpptrajImage(BiobbObject):
    """
    | biobb_analysis CpptrajImage
    | Wrapper of the Ambertools Cpptraj module for correcting periodicity (image) from a given cpptraj trajectory file.
    | Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files. The parameter names and defaults are the same as the ones in the official `Cpptraj manual <https://amber-md.github.io/cpptraj/CPPTRAJ.xhtml>`_.

    Args:
        input_top_path (str): Path to the input structure or topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top>`_. Accepted formats: top (edam:format_3881), pdb (edam:format_1476), prmtop (edam:format_3881), parmtop (edam:format_3881), zip (edam:format_3987).
        input_traj_path (str): Path to the input trajectory to be processed.  File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd>`_. Accepted formats: mdcrd (edam:format_3878), crd (edam:format_3878), cdf (edam:format_3650), netcdf (edam:format_3650), nc (edam:format_3650), restart (edam:format_3886), ncrestart (edam:format_3886), restartnc (edam:format_3886), dcd (edam:format_3878), charmm (edam:format_3887), cor (edam:format_2033), pdb (edam:format_1476), mol2 (edam:format_3816), trr (edam:format_3910), gro (edam:format_2033), binpos (edam:format_3885), xtc (edam:format_3875), cif (edam:format_1477), arc (edam:format_2333), sqm (edam:format_2033), sdf (edam:format_3814), conflib (edam:format_2033).
        output_cpptraj_path (str): Path to the output processed trajectory. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.image.netcdf>`_. Accepted formats: mdcrd (edam:format_3878), crd (edam:format_3878), netcdf (edam:format_3650), nc (edam:format_3650), rst7 (edam:format_3886), ncrst (edam:format_2033), dcd (edam:format_3878), pdb (edam:format_1476), mol2 (edam:format_3816), binpos (edam:format_3885), trr (edam:format_3910), xtc (edam:format_3875), sqm (edam:format_2033).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **start** (*int*) - (1) [1~100000|1] Starting frame for slicing.
            * **end** (*int*) - (-1) [-1~100000|1] Ending frame for slicing.
            * **steps** (*int*) - (1) [1~100000|1] Step for slicing.
            * **mask** (*str*) - ("all-atoms") Mask definition. Values: c-alpha (All c-alpha atoms; protein only), backbone (Backbone atoms), all-atoms (All system atoms), heavy-atoms (System heavy atoms; not hydrogen), side-chain (All not backbone atoms), solute (All system atoms except solvent atoms), ions (All ion molecules), solvent (All solvent atoms).
            * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd (AMBER trajectory format), cdf (Format used by netCDF software library for writing and reading chromatography-MS data files), nc (Format used by netCDF software library for writing and reading chromatography-MS data files), netcdf (Format used by netCDF software library for writing and reading chromatography-MS data files), restart (AMBER coordinate/restart file with 6 coordinates per line), ncrestart (AMBER coordinate/restart file with 6 coordinates per line), restartnc (AMBER coordinate/restart file with 6 coordinates per line), dcd (AMBER trajectory format), charmm (Format of CHARMM Residue Topology Files (RTF)), cor (Charmm COR), pdb (Protein Data Bank format), mol2 (Complete and portable representation of a SYBYL molecule), trr (Trajectory of a simulation experiment used by GROMACS), gro (GROMACS structure), binpos (Translation of the ASCII atom coordinate format to binary code), xtc (Portable binary format for trajectories produced by GROMACS package), cif (Entry format of PDB database in mmCIF format), arc (Tinker ARC), sqm (SQM Input), sdf (One of a family of chemical-data file formats developed by MDL Information Systems), conflib (LMOD Conflib).
            * **binary_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('afandiadib/ambertools:serial') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_analysis.ambertools.cpptraj_image import cpptraj_image
            prop = { 
                'start': 1, 
                'end': -1, 
                'steps': 1, 
                'mask': 'c-alpha', 
                'format': 'netcdf' 
            }
            cpptraj_image(input_top_path='/path/to/myTopology.top', 
                        input_traj_path='/path/to/myTrajectory.dcd', 
                        output_cpptraj_path='/path/to/newTrajectory.netcdf', 
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

    def __init__(self, input_top_path, input_traj_path, output_cpptraj_path, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = { 
            "in": { "input_top_path": input_top_path, "input_traj_path": input_traj_path }, 
            "out": { "output_cpptraj_path": output_cpptraj_path } 
        }

        # Properties specific for BB
        self.instructions_file = get_default_value('instructions_file')
        self.start = properties.get('start', 1)
        self.end = properties.get('end', -1)
        self.steps =  properties.get('steps', 1)
        self.mask = properties.get('mask', 'all-atoms')
        self.format = properties.get('format', 'netcdf')
        self.properties = properties
        self.binary_path = get_binary_path(properties, 'binary_path')

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_top_path"], self.input_top_path_orig = check_top_path(self.io_dict["in"]["input_top_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_traj_path"] = check_traj_path(self.io_dict["in"]["input_traj_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_cpptraj_path"] = check_out_path(self.io_dict["out"]["output_cpptraj_path"], out_log, self.__class__.__name__)
        self.in_parameters = { 'start': self.start, 'end': self.end, 'step': self.steps, 'mask': self.mask }
        self.out_parameters = { 'format': self.format }

    def create_instructions_file(self, container_io_dict, out_log, err_log):
        """Creates an input file using the properties file settings"""
        instructions_list = []
        # different path if container execution or not
        if self.container_path:
            self.instructions_file = str(PurePath(self.container_volume_path).joinpath(self.instructions_file))
        else:
            self.instructions_file = str(PurePath(fu.create_unique_dir()).joinpath(self.instructions_file))
        fu.create_name(prefix=self.prefix, step=self.step, name=self.instructions_file)

        # parm
        instructions_list.append('parm ' + container_io_dict["in"]["input_top_path"])

        # trajin
        in_params = get_in_parameters(self.in_parameters, out_log)
        instructions_list.append('trajin ' + container_io_dict["in"]["input_traj_path"] + ' ' + in_params)

        # image
        mask_atoms = get_mask('heavy-atoms', out_log)
        instructions_list.append('center ' + mask_atoms + ' origin')
        instructions_list.append('autoimage')
        instructions_list.append('rms first ' + mask_atoms)

        # mask
        mask = self.in_parameters.get('mask', '')
        if mask:
            strip_mask = get_negative_mask(mask, out_log)
            instructions_list.append('strip ' + strip_mask)

        # trajout
        out_params = get_out_parameters(self.out_parameters, out_log)
        instructions_list.append('trajout ' + container_io_dict["out"]["output_cpptraj_path"] + ' ' + out_params)

        # create .in file
        with open(self.instructions_file, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return self.instructions_file

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`CpptrajImage <ambertools.cpptraj_image.CpptrajImage>` ambertools.cpptraj_image.CpptrajImage object."""
        
        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        # create instructions file
        self.create_instructions_file(self.stage_io_dict, self.out_log, self.err_log) 

        # if container execution, copy intructions file to container
        if self.container_path:
            copy_instructions_file_to_container(self.instructions_file, self.stage_io_dict['unique_dir'])

        # create cmd and launch execution
        self.cmd = [self.binary_path, '-i', self.instructions_file]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # remove temporary folder(s)
        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            PurePath(self.instructions_file).parent
        ])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code

def cpptraj_image(input_top_path: str, input_traj_path: str, output_cpptraj_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`CpptrajImage <ambertools.cpptraj_image.CpptrajImage>` class and
    execute the :meth:`launch() <ambertools.cpptraj_image.CpptrajImage.launch>` method."""

    return CpptrajImage(input_top_path=input_top_path, 
                    input_traj_path=input_traj_path, 
                    output_cpptraj_path=output_cpptraj_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Corrects periodicity (image) from a given cpptraj trajectory file.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_top_path', required=True, help='Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.')
    required_args.add_argument('--input_traj_path', required=True, help='Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.')
    required_args.add_argument('--output_cpptraj_path', required=True, help='Path to the output processed trajectory.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    cpptraj_image(input_top_path=args.input_top_path, 
                input_traj_path=args.input_traj_path, 
                output_cpptraj_path=args.output_cpptraj_path, 
                properties=properties)

if __name__ == '__main__':
    main()