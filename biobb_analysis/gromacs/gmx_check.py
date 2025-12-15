#!/usr/bin/env python3

"""Module containing the GMX Check class and the command line interface."""

from typing import Optional

from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger

from biobb_analysis.gromacs.common import (
    check_energy_path,
    check_index_path,
    check_input_path,
    check_out_log_path,
    check_traj_path,
    get_binary_path,
    is_valid_boolean,
    is_valid_float,
)


class GMXCheck(BiobbObject):
    """
    | biobb_analysis GMXCheck
    | Wrapper of the GROMACS check module for comparing and validating GROMACS files.
    | `GROMACS check <http://manual.gromacs.org/current/onlinehelp/gmx-check.html>`_ reads, analyzes and compares run input, trajectory and energy files reporting potential differences and inconsistencies.

    Args:
        input_structure_path (str) (Optional): Path to the first GROMACS run input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_structure_2_path (str) (Optional): Path to the second GROMACS run input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_traj_path (str) (Optional): Path to the first GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_traj_2_path (str) (Optional): Path to the second GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_energy_path (str) (Optional): Path to the first GROMACS energy file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/energy.edr>`_. Accepted formats: edr (edam:format_2330).
        input_energy_2_path (str) (Optional): Path to the second GROMACS energy file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/energy.edr>`_. Accepted formats: edr (edam:format_2330).
        structure_check_path (str) (Optional): Path to the structure file to analyze for internal consistency. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_index_path (str) (Optional): Path to the GROMACS index file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx>`_. Accepted formats: ndx (edam:format_2033).
        output_log_path (str): Path to the text file storing the gmx check console output. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_check.log>`_. Accepted formats: txt (edam:format_2330), log (edam:format_2330), out (edam:format_2330).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **vdwfac** (*float*) - (0.8) Fraction of the sum of Van der Waals radii used as warning cutoff.
            * **bonlo** (*float*) - (0.4) Minimum fraction of the sum of Van der Waals radii for bonded atoms.
            * **bonhi** (*float*) - (0.7) Maximum fraction of the sum of Van der Waals radii for bonded atoms.
            * **relative_tolerance** (*float*) - (0.001) Relative tolerance for comparing real values.
            * **absolute_tolerance** (*float*) - (0.001) Absolute tolerance, useful when sums are close to zero.
            * **rmsd** (*bool*) - (False) Print RMSD for coordinates, velocities and forces.
            * **compare_ab** (*bool*) - (False) Compare the A and B topologies from a single input file.
            * **last_energy_term** (*str*) - (None) Last energy term to compare.
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

            from biobb_analysis.gromacs.gmx_check import gmx_check
            prop = {}
            gmx_check(
                input_structure_path='/path/to/myTopology.tpr',
                input_structure_2_path='/path/to/myTopologyCopy.tpr',
                output_log_path='/path/to/check.log',
                properties=prop
            )

    Info:
        * wrapped_software:
            * name: GROMACS check
            * version: >=2024.5
            * license: LGPL 2.1
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(
        self,
        input_structure_path=None,
        input_structure_2_path=None,
        input_traj_path=None,
        input_traj_2_path=None,
        input_energy_path=None,
        input_energy_2_path=None,
        structure_check_path=None,
        input_index_path=None,
        output_log_path=None,
        properties=None,
        **kwargs,
    ) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {
                "input_structure_path": input_structure_path,
                "input_structure_2_path": input_structure_2_path,
                "input_traj_path": input_traj_path,
                "input_traj_2_path": input_traj_2_path,
                "input_energy_path": input_energy_path,
                "input_energy_2_path": input_energy_2_path,
                "structure_check_path": structure_check_path,
                "input_index_path": input_index_path,
            },
            "out": {"output_log_path": output_log_path},
        }

        # Properties specific for BB
        self.vdwfac = properties.get("vdwfac")
        self.bonlo = properties.get("bonlo")
        self.bonhi = properties.get("bonhi")
        self.relative_tolerance = properties.get("relative_tolerance")
        self.absolute_tolerance = properties.get("absolute_tolerance")
        self.rmsd = properties.get("rmsd", False)
        self.compare_ab = properties.get("compare_ab", False)
        self.last_energy_term = properties.get("last_energy_term")
        self.properties = properties

        # Properties common in all GROMACS BB
        self.binary_path = get_binary_path(properties, "binary_path")

        # Check the properties
        self.check_init(properties)

    def _validate_float_property(self, prop_name, default_value=None):
        """Validates a float property and converts it to string."""
        value = self.properties.get(prop_name, default_value)
        if value is None:
            return None

        if not is_valid_float(value):
            fu.log(
                f"{self.__class__.__name__}: Incorrect {prop_name} provided, exiting",
                self.out_log,
            )
            raise SystemExit(f"{self.__class__.__name__}: Incorrect {prop_name} provided")
        return str(value)

    def _validate_boolean_property(self, prop_name, default_value=False):
        """Validates a boolean property."""
        value = self.properties.get(prop_name, default_value)
        if not is_valid_boolean(value):
            fu.log(
                f"{self.__class__.__name__}: Incorrect {prop_name} provided, exiting",
                self.out_log,
            )
            raise SystemExit(f"{self.__class__.__name__}: Incorrect {prop_name} provided")
        return value

    def check_data_params(self, out_log, err_log):
        """Checks all the input/output paths and parameters"""
        input_values = [
            self.io_dict["in"].get("input_structure_path"),
            self.io_dict["in"].get("input_structure_2_path"),
            self.io_dict["in"].get("input_traj_path"),
            self.io_dict["in"].get("input_traj_2_path"),
            self.io_dict["in"].get("input_energy_path"),
            self.io_dict["in"].get("input_energy_2_path"),
            self.io_dict["in"].get("structure_check_path"),
            self.io_dict["in"].get("input_index_path"),
        ]

        if not any(input_values):
            fu.log(
                f"{self.__class__.__name__}: No input files provided, exiting",
                out_log,
            )
            raise SystemExit(f"{self.__class__.__name__}: No input files provided")

        if self.io_dict["in"].get("input_structure_path"):
            self.io_dict["in"]["input_structure_path"] = check_input_path(
                self.io_dict["in"]["input_structure_path"], out_log, self.__class__.__name__
            )

        if self.io_dict["in"].get("input_structure_2_path"):
            self.io_dict["in"]["input_structure_2_path"] = check_input_path(
                self.io_dict["in"]["input_structure_2_path"], out_log, self.__class__.__name__
            )

        if self.io_dict["in"].get("input_traj_path"):
            self.io_dict["in"]["input_traj_path"] = check_traj_path(
                self.io_dict["in"]["input_traj_path"], out_log, self.__class__.__name__
            )

        if self.io_dict["in"].get("input_traj_2_path"):
            self.io_dict["in"]["input_traj_2_path"] = check_traj_path(
                self.io_dict["in"]["input_traj_2_path"], out_log, self.__class__.__name__
            )

        if self.io_dict["in"].get("input_energy_path"):
            self.io_dict["in"]["input_energy_path"] = check_energy_path(
                self.io_dict["in"]["input_energy_path"], out_log, self.__class__.__name__
            )

        if self.io_dict["in"].get("input_energy_2_path"):
            self.io_dict["in"]["input_energy_2_path"] = check_energy_path(
                self.io_dict["in"]["input_energy_2_path"], out_log, self.__class__.__name__
            )

        if self.io_dict["in"].get("structure_check_path"):
            self.io_dict["in"]["structure_check_path"] = check_input_path(
                self.io_dict["in"]["structure_check_path"], out_log, self.__class__.__name__
            )

        if self.io_dict["in"].get("input_index_path"):
            self.io_dict["in"]["input_index_path"] = check_index_path(
                self.io_dict["in"]["input_index_path"], out_log, self.__class__.__name__
            )

        if not self.io_dict["out"].get("output_log_path"):
            fu.log(
                f"{self.__class__.__name__}: No output log path provided, exiting",
                out_log,
            )
            raise SystemExit(f"{self.__class__.__name__}: No output log path provided")
        self.io_dict["out"]["output_log_path"] = check_out_log_path(
            self.io_dict["out"]["output_log_path"], out_log, self.__class__.__name__
        )

        self.vdwfac = self._validate_float_property("vdwfac", self.vdwfac)
        self.bonlo = self._validate_float_property("bonlo", self.bonlo)
        self.bonhi = self._validate_float_property("bonhi", self.bonhi)
        self.relative_tolerance = self._validate_float_property(
            "relative_tolerance", self.relative_tolerance
        )
        self.absolute_tolerance = self._validate_float_property(
            "absolute_tolerance", self.absolute_tolerance
        )
        self.rmsd = self._validate_boolean_property("rmsd", self.rmsd)
        self.compare_ab = self._validate_boolean_property("compare_ab", self.compare_ab)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`GMXCheck <gromacs.gmx_check.GMXCheck>` object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        self.cmd = [self.binary_path, "check"]

        if self.stage_io_dict["in"].get("input_traj_path"):
            self.cmd.extend(["-f", self.stage_io_dict["in"]["input_traj_path"]])

        if self.stage_io_dict["in"].get("input_traj_2_path"):
            self.cmd.extend(["-f2", self.stage_io_dict["in"]["input_traj_2_path"]])

        if self.stage_io_dict["in"].get("input_structure_path"):
            self.cmd.extend(["-s1", self.stage_io_dict["in"]["input_structure_path"]])

        if self.stage_io_dict["in"].get("input_structure_2_path"):
            self.cmd.extend(["-s2", self.stage_io_dict["in"]["input_structure_2_path"]])

        if self.stage_io_dict["in"].get("structure_check_path"):
            self.cmd.extend(["-c", self.stage_io_dict["in"]["structure_check_path"]])

        if self.stage_io_dict["in"].get("input_energy_path"):
            self.cmd.extend(["-e", self.stage_io_dict["in"]["input_energy_path"]])

        if self.stage_io_dict["in"].get("input_energy_2_path"):
            self.cmd.extend(["-e2", self.stage_io_dict["in"]["input_energy_2_path"]])

        if self.stage_io_dict["in"].get("input_index_path"):
            self.cmd.extend(["-n", self.stage_io_dict["in"]["input_index_path"]])

        if self.vdwfac is not None:
            self.cmd.extend(["-vdwfac", self.vdwfac])

        if self.bonlo is not None:
            self.cmd.extend(["-bonlo", self.bonlo])

        if self.bonhi is not None:
            self.cmd.extend(["-bonhi", self.bonhi])

        if self.relative_tolerance is not None:
            self.cmd.extend(["-tol", self.relative_tolerance])

        if self.absolute_tolerance is not None:
            self.cmd.extend(["-abstol", self.absolute_tolerance])

        if self.rmsd:
            self.cmd.append("-rmsd")

        if self.compare_ab:
            self.cmd.append("-ab")

        if self.last_energy_term:
            self.cmd.extend(["-lastener", self.last_energy_term])

        self.cmd.extend(
            [">", self.stage_io_dict["out"]["output_log_path"]],
        )

        # Run Biobb block
        self.run_biobb()
        # Copy files to host
        self.copy_to_host()
        self.remove_tmp_files()
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def gmx_check(
    input_structure_path: Optional[str] = None,
    input_structure_2_path: Optional[str] = None,
    input_traj_path: Optional[str] = None,
    input_traj_2_path: Optional[str] = None,
    input_energy_path: Optional[str] = None,
    input_energy_2_path: Optional[str] = None,
    structure_check_path: Optional[str] = None,
    input_index_path: Optional[str] = None,
    output_log_path: Optional[str] = None,
    properties: Optional[dict] = None,
    **kwargs,
) -> int:
    """Create the :class:`GMXCheck <gromacs.gmx_check.GMXCheck>` class and
    execute the :meth:`launch() <gromacs.gmx_check.GMXCheck.launch>` method."""
    return GMXCheck(**dict(locals())).launch()


gmx_check.__doc__ = GMXCheck.__doc__
main = GMXCheck.get_main(
    gmx_check,
    "Checks and compares GROMACS topology, trajectory or energy files.",
)

if __name__ == "__main__":
    main()
