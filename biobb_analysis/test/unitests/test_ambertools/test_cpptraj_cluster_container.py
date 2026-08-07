# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_cluster import cpptraj_cluster
import sys


class TestCpptrajClusterDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_cluster_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cluster_docker(self):
        cpptraj_cluster(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_summary_path'])
        assert fx.equal(self.paths['output_summary_path'], self.paths['ref_output_summary_path'])
        assert fx.not_empty(self.paths['output_info_path'])
        assert fx.equal(self.paths['output_info_path'], self.paths['ref_output_info_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestCpptrajClusterSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_cluster_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cluster_singularity(self):
        cpptraj_cluster(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_summary_path'])
        assert fx.equal(self.paths['output_summary_path'], self.paths['ref_output_summary_path'])
        assert fx.not_empty(self.paths['output_info_path'])
        assert fx.equal(self.paths['output_info_path'], self.paths['ref_output_info_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
