#!/usr/bin/env python3

"""Module containing the Cpptraj Mask class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_common.tools import file_utils as fu
from biobb_analysis.ambertools.common import CpptrajBase, get_in_parameters, get_negative_mask


class CpptrajMask(CpptrajBase):
    """
    | biobb_analysis CpptrajMask
    | Wrapper of the Ambertools Cpptraj module for extracting a selection of atoms from a given cpptraj compatible trajectory.
    | Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files. The parameter names and defaults are the same as the ones in the official `Cpptraj manual <https://raw.githubusercontent.com/Amber-MD/cpptraj/master/doc/CpptrajManual.pdf>`_.

    Args:
        input_top_path (str): Path to the input structure or topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top>`_. Accepted formats: top (edam:format_3881), pdb (edam:format_1476), prmtop (edam:format_3881), parmtop (edam:format_3881), zip (edam:format_3987).
        input_traj_path (str): Path to the input trajectory to be processed.  File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd>`_. Accepted formats: mdcrd (edam:format_3878), crd (edam:format_3878), cdf (edam:format_3650), netcdf (edam:format_3650), nc (edam:format_3650), restart (edam:format_3886), ncrestart (edam:format_3886), restartnc (edam:format_3886), dcd (edam:format_3878), charmm (edam:format_3887), cor (edam:format_2033), pdb (edam:format_1476), mol2 (edam:format_3816), trr (edam:format_3910), gro (edam:format_2033), binpos (edam:format_3885), xtc (edam:format_3875), cif (edam:format_1477), arc (edam:format_2333), sqm (edam:format_2033), sdf (edam:format_3814), conflib (edam:format_2033).
        output_cpptraj_path (str): Path to the output processed trajectory. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.mask.netcdf>`_. Accepted formats: mdcrd (edam:format_3878), crd (edam:format_3878), netcdf (edam:format_3650), nc (edam:format_3650), rst7 (edam:format_3886), ncrst (edam:format_2033), dcd (edam:format_3878), pdb (edam:format_1476), mol2 (edam:format_3816), binpos (edam:format_3885), trr (edam:format_3910), xtc (edam:format_3875), sqm (edam:format_2033).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **start** (*int*) - (1) [1~100000|1] Starting frame for slicing.
            * **end** (*int*) - (-1) [-1~100000|1] Ending frame for slicing.
            * **steps** (*int*) - (1) [1~100000|1] Step for slicing.
            * **mask** (*str*) - ("all-atoms") Mask definition. Values: c-alpha (All c-alpha atoms; protein only), backbone (Backbone atoms), all-atoms (All system atoms), heavy-atoms (System heavy atoms; not hydrogen), side-chain (All not backbone atoms), solute (All system atoms except solvent atoms), ions (All ion molecules), solvent (All solvent atoms), AnyAmberFromatMask (Amber atom selection syntax like `@*`).
            * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd (AMBER trajectory format), cdf (Format used by netCDF software library for writing and reading chromatography-MS data files), netcdf (Format used by netCDF software library for writing and reading chromatography-MS data files), nc (Format used by netCDF software library for writing and reading chromatography-MS data files), restart (AMBER coordinate/restart file with 6 coordinates per line), ncrestart (AMBER coordinate/restart file with 6 coordinates per line), restartnc (AMBER coordinate/restart file with 6 coordinates per line), dcd (AMBER trajectory format), charmm (Format of CHARMM Residue Topology Files (RTF)), cor (Charmm COR), pdb (Protein Data Bank format), mol2 (Complete and portable representation of a SYBYL molecule), trr (Trajectory of a simulation experiment used by GROMACS), gro (GROMACS structure), binpos (Translation of the ASCII atom coordinate format to binary code), xtc (Portable binary format for trajectories produced by GROMACS package), cif (Entry format of PDB database in mmCIF format), arc (Tinker ARC), sqm (SQM Input), sdf (One of a family of chemical-data file formats developed by MDL Information Systems), conflib (LMOD Conflib).
            * **binary_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('afandiadib/ambertools:serial') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_analysis.ambertools.cpptraj_mask import cpptraj_mask
            prop = {
                'start': 1,
                'end': -1,
                'steps': 1,
                'mask': 'c-alpha',
                'format': 'netcdf'
            }
            cpptraj_mask(input_top_path='/path/to/myTopology.top',
                        input_traj_path='/path/to/myTrajectory.dcd',
                        output_cpptraj_path='/path/to/newTrajectory.netcdf',
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

    def __init__(self, input_top_path: str, input_traj_path: str, output_cpptraj_path: str,
                 properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def trajin_frames(self) -> str:
        """Goes from the start, end and steps properties to the frames of the trajin line."""
        return get_in_parameters({'start': self.start, 'end': self.end, 'step': self.steps}, self.out_log, 'mask')

    def instructions(self) -> list[str]:
        """Goes from the mask property to the strip line of the other atoms and the trajout line."""
        if not self.mask or self.mask == 'None':
            fu.log('No mask provided, exiting', self.out_log, self.global_log)
            raise SystemExit('Mask parameter is mandatory')
        return ['strip ' + get_negative_mask(self.mask), self.trajout()]


cpptraj_mask = launcher(CpptrajMask)

if __name__ == '__main__':
    CpptrajMask.main()
