from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.cluster import Cluster


class TestCluster():
    def setUp(self):
        fx.test_setup(self,'cluster')

    def tearDown(self):
        fx.test_teardown(self)

    def test_cluster(self):
        Cluster(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['ref_output_pdb_path'])
