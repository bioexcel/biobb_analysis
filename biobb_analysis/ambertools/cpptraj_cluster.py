#!/usr/bin/env python3

"""Module containing the Cpptraj Cluster class and the command line interface."""

from typing import Optional
from pathlib import PurePath
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger
from biobb_analysis.ambertools.common import get_default_value, check_top_path, check_traj_path, check_out_path, get_binary_path, get_in_parameters, get_negative_mask, setup_structure, get_cluster_algorithm, get_cluster_metric, get_traj_format


class CpptrajCluster(BiobbObject):
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
            * **container_working_dir** (*str*) - (None) Container working directory definition.
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

    def __init__(self, input_top_path, input_traj_path, output_cpptraj_path,
                 output_summary_path=None, output_info_path=None, output_traj_path=None,
                 properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_top_path": input_top_path, "input_traj_path": input_traj_path},
            "out": {"output_cpptraj_path": output_cpptraj_path, "output_summary_path": output_summary_path,
                    "output_info_path": output_info_path, "output_traj_path": output_traj_path}
        }

        # Properties specific for BB
        self.instructions_file = get_default_value('instructions_file')
        self.start = properties.get('start', 1)
        self.end = properties.get('end', -1)
        self.steps = properties.get('steps', 1)
        self.mask = properties.get('mask', 'all-atoms')
        self.algorithm = properties.get('algorithm', 'hieragglo')
        self.clusters = properties.get('clusters', 10)
        self.epsilon = properties.get('epsilon', -1.0)
        self.minpoints = properties.get('minpoints', 4)
        self.linkage = properties.get('linkage', 'linkage')
        self.metric = properties.get('metric', 'rms')
        self.metric_mask = properties.get('metric_mask', 'all-atoms')
        self.mass = properties.get('mass', False)
        self.nofit = properties.get('nofit', False)
        self.sieve = properties.get('sieve', 0)
        self.properties = properties
        self.binary_path = get_binary_path(properties, 'binary_path')

        # Check the properties
        self.check_init(properties)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_top_path"], self.input_top_path_orig = check_top_path(self.io_dict["in"]["input_top_path"], out_log, self.__class__.__name__)
        self.io_dict["in"]["input_traj_path"] = check_traj_path(self.io_dict["in"]["input_traj_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_cpptraj_path"] = check_out_path(self.io_dict["out"]["output_cpptraj_path"], out_log, self.__class__.__name__)
        for out_file in ("output_summary_path", "output_info_path", "output_traj_path"):
            if self.io_dict["out"][out_file]:
                self.io_dict["out"][out_file] = check_out_path(self.io_dict["out"][out_file], out_log, self.__class__.__name__)
        self.in_parameters = {'start': self.start, 'end': self.end, 'step': self.steps, 'mask': self.mask}

    def create_instructions_file(self, container_io_dict, out_log, err_log):
        """Creates an input file using the properties file settings"""
        instructions_list = []
        # different path if container execution or not
        if self.container_path:
            self.instructions_file = str(PurePath(self.stage_io_dict['unique_dir']).joinpath("cpptraj.in"))
            self.instructions_file_path = str(PurePath(self.container_volume_path).joinpath("cpptraj.in"))
        else:
            self.instructions_file = self.create_tmp_file(self.instructions_file)
            self.instructions_file_path = self.instructions_file

        # parm
        instructions_list.append('parm ' + container_io_dict["in"]["input_top_path"])

        # trajin
        in_params = get_in_parameters(self.in_parameters, out_log)
        instructions_list.append('trajin ' + container_io_dict["in"]["input_traj_path"] + ' ' + in_params)

        # Set up
        instructions_list += setup_structure(self)

        # mask
        mask = self.in_parameters.get('mask', '')
        if mask:
            strip_mask = get_negative_mask(mask, out_log)
            instructions_list.append('strip ' + strip_mask)

        # the cluster analysis works on a COORDS data set, so the processed frames must be saved first
        cluster_set = get_default_value('cluster_set')
        instructions_list.append('createcrd ' + cluster_set)
        instructions_list.append('run')

        # cluster
        cluster = ['cluster', 'crdset', cluster_set]
        cluster.append(get_cluster_algorithm(self.algorithm, self.clusters, self.epsilon, self.minpoints, self.linkage, out_log))
        cluster.append(get_cluster_metric(self.metric, self.mass, self.nofit, self.metric_mask, out_log))
        if self.sieve:
            cluster += ['sieve', str(self.sieve)]
        cluster += ['out', container_io_dict["out"]["output_cpptraj_path"]]
        if container_io_dict["out"].get("output_summary_path"):
            cluster += ['summary', container_io_dict["out"]["output_summary_path"]]
        if container_io_dict["out"].get("output_info_path"):
            cluster += ['info', container_io_dict["out"]["output_info_path"]]
        if container_io_dict["out"].get("output_traj_path"):
            traj_path = container_io_dict["out"]["output_traj_path"]
            cluster += ['singlerepout', traj_path, 'singlerepfmt', get_traj_format(traj_path, out_log)]
        instructions_list.append(' '.join(cluster))

        # create .in file
        with open(self.instructions_file, 'w') as mdp:
            for line in instructions_list:
                mdp.write(line.strip() + '\n')

        return self.instructions_file_path

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`CpptrajCluster <ambertools.cpptraj_cluster.CpptrajCluster>` object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # create instructions file
        self.create_instructions_file(self.stage_io_dict, self.out_log, self.err_log)

        # create cmd and launch execution
        self.cmd = [self.binary_path, '-i', self.instructions_file_path]

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # remove temporary folder(s)
        self.remove_tmp_files()
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def cpptraj_cluster(input_top_path: str, input_traj_path: str, output_cpptraj_path: str, output_summary_path: Optional[str] = None, output_info_path: Optional[str] = None, output_traj_path: Optional[str] = None, properties: Optional[dict] = None, **kwargs) -> int:
    """Create the :class:`CpptrajCluster <ambertools.cpptraj_cluster.CpptrajCluster>` class and
    execute the :meth:`launch() <ambertools.cpptraj_cluster.CpptrajCluster.launch>` method."""
    return CpptrajCluster(**dict(locals())).launch()


cpptraj_cluster.__doc__ = CpptrajCluster.__doc__
main = CpptrajCluster.get_main(cpptraj_cluster, "Clusters the frames of a given cpptraj compatible trajectory.")

if __name__ == '__main__':
    main()
