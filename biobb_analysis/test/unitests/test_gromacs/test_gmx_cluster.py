from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_cluster import gmx_cluster


class TestGMXCluster():
    def setup_class(self):
        fx.test_setup(self, 'gmx_cluster')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cluster(self):
        gmx_cluster(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['ref_output_pdb_path'])