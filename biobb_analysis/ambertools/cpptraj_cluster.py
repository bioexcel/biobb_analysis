#!/usr/bin/env python3

"""Module containing the Cpptraj Cluster class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_analysis.ambertools.common import CpptrajBase, get_default_value, setup_structure, get_cluster_algorithm, get_cluster_metric, get_traj_format


class CpptrajCluster(CpptrajBase):
    """
    | biobb_analysis CpptrajCluster
    | Wrapper of the Ambertools Cpptraj module for clustering the frames of a given cpptraj compatible trajectory.
    | Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files. The parameter names and defaults are the same as the ones in the official `Cpptraj manual <https://raw.githubusercontent.com/Amber-MD/cpptraj/master/doc/CpptrajManual.pdf>`_.

    Args:
        input_top_path (str): Path to the input structure or topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top>`_. Accepted formats: top (edam:format_3881), pdb (edam:format_1476), prmtop (edam:format_3881), parmtop (edam:format_3881), zip (edam:format_3987).
        input_traj_path (str): Path to the input trajectory to be processed. File type: input. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd>`_. Accepted formats: mdcrd (edam:format_3878), crd (edam:format_3878), cdf (edam:format_3650), netcdf (edam:format_3650), nc (edam:format_3650), restart (edam:format_3886), ncrestart (edam:format_3886), restartnc (edam:format_3886), dcd (edam:format_3878), charmm (edam:format_3887), cor (edam:format_2033), pdb (edam:format_1476), mol2 (edam:format_3816), trr (edam:format_3910), gro (edam:format_2033), binpos (edam:format_3885), xtc (edam:format_3875), cif (edam:format_1477), arc (edam:format_2333), sqm (edam:format_2033), sdf (edam:format_3814), conflib (edam:format_2033).
        output_cpptraj_path (str): Path to the output cluster number vs time analysis. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.cluster.dat>`_. Accepted formats: dat (edam:format_1637), agr (edam:format_2033), xmgr (edam:format_2033), gnu (edam:format_2033).
        output_summary_path (str) (Optional): Path to the output summary of the generated clusters. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.cluster.summary.dat>`_. Accepted formats: dat (edam:format_1637), agr (edam:format_2033), xmgr (edam:format_2033), gnu (edam:format_2033).
        output_info_path (str) (Optional): Path to the output detailed information of the generated clusters. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.cluster.info.dat>`_. Accepted formats: dat (edam:format_1637), agr (edam:format_2033), xmgr (edam:format_2033), gnu (edam:format_2033).
        output_traj_path (str) (Optional): Path to the output trajectory containing the representative frame of every cluster. File type: output. `Sample file <https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.cluster.netcdf>`_. Accepted formats: mdcrd (edam:format_3878), crd (edam:format_3878), cdf (edam:format_3650), netcdf (edam:format_3650), nc (edam:format_3650), restart (edam:format_3886), ncrestart (edam:format_3886), restartnc (edam:format_3886), dcd (edam:format_3878), charmm (edam:format_3887), cor (edam:format_2033), pdb (edam:format_1476), mol2 (edam:format_3816), trr (edam:format_3910), gro (edam:format_2033), binpos (edam:format_3885), xtc (edam:format_3875), cif (edam:format_1477), arc (edam:format_2333), sqm (edam:format_2033), sdf (edam:format_3814), conflib (edam:format_2033).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **start** (*int*) - (1) [1~100000|1] Starting frame for slicing
            * **end** (*int*) - (-1) [-1~100000|1] Ending frame for slicing
            * **steps** (*int*) - (1) [1~100000|1] Step for slicing
            * **mask** (*str*) - ("all-atoms") Mask definition. Values: c-alpha (All c-alpha atoms; protein only), backbone (Backbone atoms), all-atoms (All system atoms), heavy-atoms (System heavy atoms; not hydrogen), side-chain (All not backbone atoms), solute (All system atoms except solvent atoms), ions (All ion molecules), solvent (All solvent atoms), AnyAmberFromatMask (Amber atom selection syntax like `@*`).
            * **algorithm** (*str*) - ("hieragglo") Clustering algorithm. Values: hieragglo (Hierarchical agglomerative -bottom up- clustering), dbscan (Density-based spatial clustering of applications with noise), kmeans (K-means clustering), dpeaks (Clustering by fast search and find of density peaks; Cpptraj leaves an extra temp.dat file in the working directory).
            * **clusters** (*int*) - (10) [1~1000|1] Target number of clusters. Only used by the hieragglo and kmeans algorithms.
            * **epsilon** (*float*) - (-1.0) [-1~100|0.1] Minimum distance between clusters. Mandatory for the dbscan and dpeaks algorithms; for hieragglo it is an additional stop condition, only used when greater than 0.
            * **minpoints** (*int*) - (4) [1~1000|1] Minimum number of points required to form a cluster. Only used by the dbscan algorithm.
            * **linkage** (*str*) - ("linkage") Distance between clusters. Only used by the hieragglo algorithm. Values: linkage (Shortest distance between members of the two clusters), averagelinkage (Average distance between members of the two clusters), complete (Longest distance between members of the two clusters).
            * **metric** (*str*) - ("rms") Distance metric between frames. Values: rms (Coordinate root mean square deviation), srmsd (Symmetry-corrected coordinate root mean square deviation), dme (Distance root mean square deviation), qrmsd (Quaternion root mean square deviation).
            * **metric_mask** (*str*) - ("all-atoms") Mask used for the distance metric calculation. Unlike **mask**, the atoms outside this selection are kept in the clustered coordinates, they are only left out of the frame to frame distance calculation. Values: c-alpha (All c-alpha atoms; protein only), backbone (Backbone atoms), all-atoms (All system atoms), heavy-atoms (System heavy atoms; not hydrogen), side-chain (All not backbone atoms), solute (All system atoms except solvent atoms), ions (All ion molecules), solvent (All solvent atoms), AnyAmberFromatMask (Amber atom selection syntax like `@*`).
            * **mass** (*bool*) - (False) Mass-weight the distance metric.
            * **nofit** (*bool*) - (False) Do not best-fit the frames before calculating the distance metric.
            * **sieve** (*int*) - (0) [0~100000|1] Cluster only every nth frame and add the remaining frames back in afterwards. 0 disables sieving.
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

            from biobb_analysis.ambertools.cpptraj_cluster import cpptraj_cluster
            prop = {
                'start': 1,
                'end': -1,
                'steps': 1,
                'mask': 'c-alpha',
                'algorithm': 'hieragglo',
                'clusters': 5
            }
            cpptraj_cluster(input_top_path='/path/to/myTopology.top',
                            input_traj_path='/path/to/myTrajectory.dcd',
                            output_cpptraj_path='/path/to/newAnalysis.dat',
                            output_summary_path='/path/to/newSummary.dat',
                            output_info_path='/path/to/newInfo.dat',
                            output_traj_path='/path/to/newTrajectory.netcdf',
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
                 output_summary_path: Optional[str] = None, output_info_path: Optional[str] = None, output_traj_path: Optional[str] = None,
                 properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def instructions(self) -> list[str]:
        """Goes from the properties to the set up, strip, createcrd and cluster lines."""
        out = self.stage_io_dict["out"]
        cluster_set = get_default_value('cluster_set')
        cluster = ['cluster', 'crdset', cluster_set,
                   get_cluster_algorithm(self.algorithm, self.clusters, self.epsilon, self.minpoints, self.linkage, self.out_log),
                   get_cluster_metric(self.metric, self.mass, self.nofit, self.metric_mask, self.out_log)]
        if self.sieve:
            cluster += ['sieve', str(self.sieve)]
        cluster += ['out', out["output_cpptraj_path"]]
        if out.get("output_summary_path"):
            cluster += ['summary', out["output_summary_path"]]
        if out.get("output_info_path"):
            cluster += ['info', out["output_info_path"]]
        if out.get("output_traj_path"):
            cluster += ['singlerepout', out["output_traj_path"], 'singlerepfmt', get_traj_format(out["output_traj_path"], self.out_log)]
        # the cluster analysis works on a COORDS data set, so the processed frames must be saved first
        return setup_structure() + self.strip_mask() + ['createcrd ' + cluster_set, 'run', ' '.join(cluster)]


cpptraj_cluster = launcher(CpptrajCluster)

if __name__ == '__main__':
    CpptrajCluster.main()
