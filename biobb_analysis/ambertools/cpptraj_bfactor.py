#!/usr/bin/env python3

"""Module containing the Cpptraj Bfactor class and the command line interface."""

from typing import Optional
from pathlib import PurePath
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger
from biobb_analysis.ambertools.common import get_default_value, check_top_path, check_traj_path, check_out_path, get_binary_path, get_in_parameters, setup_structure, get_negative_mask, get_mask, get_reference


class CpptrajBfactor(BiobbObject):
    """
    | biobb_analysis CpptrajBfactor
    | Wrapper of the Ambertools Cpptraj module for calculating the Bfactor fluctuations of a given cpptraj compatible trajectory.
    | Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files. The parameter names and defaults are the same as the ones in the official `Cpptraj manual <https://raw.githubusercontent.com/Amber-MD/cpptraj/master/doc/CpptrajManual.pdf>`_.

    Args:
        input_top_path (str): Path to the input structure or topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top>`_. Accepted formats: top (edam:format_3881), pdb (edam:format_1476), prmtop (edam:format_3881), parmtop (edam:format_3881), zip (edam:format_3987).
        input_traj_path (str): Path to the input trajectory to be processed. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd>`_. Accepted formats: mdcrd (edam:format_3878), crd (edam:format_3878), cdf (edam:format_3650), netcdf (edam:format_3650), nc (edam:format_3650), restart (edam:format_3886), ncrestart (edam:format_3886), restartnc (edam:format_3886), dcd (edam:format_3878), charmm (edam:format_3887), cor (edam:format_2033), pdb (edam:format_1476), mol2 (edam:format_3816), trr (edam:format_3910), gro (edam:format_2033), binpos (edam:format_3885), xtc (edam:format_3875), cif (edam:format_1477), arc (edam:format_2333), sqm (edam:format_2033), sdf (edam:format_3814), conflib (edam:format_2033).
        input_exp_path (str) (Optional): Path to the experimental reference file (required if reference = experimental). File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/experimental.1e5t.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_cpptraj_path (str): Path to the output processed analysis. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.bfactor.first.dat>`_. Accepted formats: dat (edam:format_1637), agr (edam:format_2033), xmgr (edam:format_2033), gnu (edam:format_2033).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **start** (*int*) - (1) [1~100000|1] Starting frame for slicing
            * **end** (*int*) - (-1) [-1~100000|1] Ending frame for slicing
            * **steps** (*int*) - (1) [1~100000|1] Step for slicing
            * **mask** (*str*) - ("all-atoms") Mask definition. Values: c-alpha (All c-alpha atoms; protein only), backbone (Backbone atoms), all-atoms (All system atoms), heavy-atoms (System heavy atoms; not hydrogen), side-chain (All not backbone atoms), solute (All system atoms except solvent atoms), ions (All ion molecules), solvent (All solvent atoms), AnyAmberFromatMask (Amber atom selection syntax like `@*`).
            * **reference** (*str*) - ("first") Reference definition. Values: first (Use the first trajectory frame as reference), average (Use the average of all trajectory frames as reference), experimental (Use the experimental structure as reference).
            * **binary_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('afandiadib/ambertools:serial') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_analysis.ambertools.cpptraj_bfactor import cpptraj_bfactor
            prop = {
                'start': 1,
                'end': -1,
                'steps': 1,
                'mask': 'c-alpha',
                'reference': 'first'
            }
            cpptraj_bfactor(input_top_path='/path/to/myTopology.top',
                            input_traj_path='/path/to/myTrajectory.dcd',
                            output_cpptraj_path='/path/to/newAnalysis.dat',
                            input_exp_path= '/path/to/myExpStructure.pdb',
                            properties=prop)

    Info:
        * wrapped_software:
            * name: Ambertools Cpptraj
            * version: >=22.5
            * license: GNU
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_top_path, input_traj_path, output_cpptraj_path,
                 input_exp_path=None, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_top_path": input_top_path,
                   "input_traj_path": input_traj_path,
                   "input_exp_path": input_exp_path},
            "out": {"output_cpptraj_path": output_cpptraj_path}
        }

        # Properties specific for BB
        self.instructions_file = get_default_value('instructions_file')
        self.start = properties.get('start', 1)
        self.end = properties.get('end', -1)
        self.steps = properties.get('steps', 1)
        self.mask = properties.get('mask', 'all-atoms')
        self.reference = properties.get('reference', 'first')
        self.properties = properties
        self.binary_path = get_binary_path(properties, 'binary_path')

        # Check the properties
        self.check_init(properties)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_top_path"], self.input_top_path_orig = check_top_path(self.io_dict["in"]["input_top_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_traj_path"] = check_traj_path(self.io_dict["in"]["input_traj_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_cpptraj_path"] = check_out_path(self.io_dict["out"]["output_cpptraj_path"], out_log, self.__class__.__name__)
        self.in_parameters = {'start': self.start, 'end': self.end, 'step': self.steps, 'mask': self.mask, 'reference': self.reference}

    def create_instructions_file(self, container_io_dict, out_log, err_log):
        """Creates an input file using the properties file settings"""
        instructions_list = []
        # Different path if container execution or not
        if self.container_path:
            self.instructions_file = str(PurePath(self.container_volume_path).joinpath(self.instructions_file))
        else:
            self.instructions_file = self.create_tmp_file(self.instructions_file)

        # parm
        instructions_list.append('parm ' + container_io_dict["in"]["input_top_path"])

        # trajin
        in_params = get_in_parameters(self.in_parameters, out_log)
        instructions_list.append('trajin ' + container_io_dict["in"]["input_traj_path"] + ' ' + in_params)

        # Set up
        instructions_list += setup_structure(self)

        # mask
        mask = self.in_parameters.get('mask', '')
        ref_mask = ''
        if mask:
            strip_mask = get_negative_mask(mask, out_log)
            ref_mask = get_mask(mask, out_log)
            instructions_list.append('strip ' + strip_mask)

        # reference
        reference = self.in_parameters.get('reference', '')
        inp_exp_pth = None
        if "input_exp_path" in container_io_dict["in"]:
            inp_exp_pth = container_io_dict["in"]["input_exp_path"]
        instructions_list += get_reference(reference, container_io_dict["out"]["output_cpptraj_path"], inp_exp_pth, ref_mask, False, self.__class__.__name__, out_log)
        instructions_list.append('atomicfluct out ' + container_io_dict["out"]["output_cpptraj_path"] + ' byres bfactor')

        # create .in file
        with open(self.instructions_file, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return self.instructions_file

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`CpptrajBfactor <ambertools.cpptraj_bfactor.CpptrajBfactor>` object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Create instructions file
        self.create_instructions_file(self.stage_io_dict, self.out_log, self.err_log)

        # Create cmd and launch execution
        self.cmd = [self.binary_path, '-i', self.instructions_file]

        # Run Biobb block
        self.run_biobb()
        # Copy files to host
        self.copy_to_host()
        # Remove temporary folder
        self.remove_tmp_files()
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def cpptraj_bfactor(input_top_path: str,
                    input_traj_path: str,
                    output_cpptraj_path: str,
                    input_exp_path: Optional[str] = None,
                    properties: Optional[dict] = None, **kwargs) -> int:
    """Execute the :class:`CpptrajBfactor <ambertools.cpptraj_bfactor.CpptrajBfactor>` class and
    execute the :meth:`launch() <ambertools.cpptraj_bfactor.CpptrajBfactor.launch>` method."""
    return CpptrajBfactor(**dict(locals())).launch()


cpptraj_bfactor.__doc__ = CpptrajBfactor.__doc__
main = CpptrajBfactor.get_main(
    cpptraj_bfactor,
    "Calculates the Bfactor fluctuations of a given cpptraj compatible trajectory."
)

if __name__ == '__main__':
    main()
