# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_cluster import cpptraj_cluster


class TestCpptrajCluster():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_cluster')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cluster(self):
        cpptraj_cluster(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_summary_path'])
        assert fx.equal(self.paths['output_summary_path'], self.paths['ref_output_summary_path'])
        assert fx.not_empty(self.paths['output_info_path'])
        assert fx.equal(self.paths['output_info_path'], self.paths['ref_output_info_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
