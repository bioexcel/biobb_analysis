#!/usr/bin/env python3

"""Module containing the Cpptraj Rmsf class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_analysis.ambertools.common import CpptrajBase, setup_structure, get_mask, get_reference


class CpptrajRmsf(CpptrajBase):
    """
    | biobb_analysis CpptrajRmsf
    | Wrapper of the Ambertools Cpptraj module for calculating the Root Mean Square fluctuations (RMSf) of a given cpptraj compatible trajectory.
    | Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files. The parameter names and defaults are the same as the ones in the official `Cpptraj manual <https://raw.githubusercontent.com/Amber-MD/cpptraj/master/doc/CpptrajManual.pdf>`_.

    Args:
        input_top_path (str): Path to the input structure or topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top>`_. Accepted formats: top (edam:format_3881), pdb (edam:format_1476), prmtop (edam:format_3881), parmtop (edam:format_3881), zip (edam:format_3987).
        input_traj_path (str): Path to the input trajectory to be processed.  File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd>`_. Accepted formats: mdcrd (edam:format_3878), crd (edam:format_3878), cdf (edam:format_3650), netcdf (edam:format_3650), nc (edam:format_3650), restart (edam:format_3886), ncrestart (edam:format_3886), restartnc (edam:format_3886), dcd (edam:format_3878), charmm (edam:format_3887), cor (edam:format_2033), pdb (edam:format_1476), mol2 (edam:format_3816), trr (edam:format_3910), gro (edam:format_2033), binpos (edam:format_3885), xtc (edam:format_3875), cif (edam:format_1477), arc (edam:format_2333), sqm (edam:format_2033), sdf (edam:format_3814), conflib (edam:format_2033).
        input_exp_path (str) (Optional): Path to the experimental reference file (required if reference = experimental). File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/experimental.1e5t.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_cpptraj_path (str): Path to the output processed analysis. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.rmsf.first.dat>`_. Accepted formats: dat (edam:format_1637), agr (edam:format_2033), xmgr (edam:format_2033), gnu (edam:format_2033).
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
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_analysis.ambertools.cpptraj_rmsf import cpptraj_rmsf
            prop = {
                'start': 1,
                'end': -1,
                'steps': 1,
                'mask': 'c-alpha',
                'reference': 'first'
            }
            cpptraj_rmsf(input_top_path='/path/to/myTopology.top',
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

    def __init__(self, input_top_path: str, input_traj_path: str, output_cpptraj_path: str,
                 input_exp_path: Optional[str] = None, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def instructions(self) -> list[str]:
        """Goes from the properties to the set up, strip, reference and atomicfluct lines."""
        out = self.stage_io_dict["out"]["output_cpptraj_path"]
        exp_path = self.stage_io_dict["in"].get("input_exp_path")
        ref_mask = get_mask(self.mask) if self.mask else ''
        reference = get_reference(self.reference, out, exp_path, ref_mask, False, self.__class__.__name__, self.out_log)
        return setup_structure() + self.strip_mask() + reference + ['atomicfluct out ' + out + ' byres']


cpptraj_rmsf = launcher(CpptrajRmsf)

if __name__ == '__main__':
    CpptrajRmsf.main()
