from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_cluster import GMXCluster


class TestGMXClusterDocker():
    def setUp(self):
        fx.test_setup(self,'gmx_cluster_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_cluster_docker(self):
        GMXCluster(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['ref_output_pdb_path'])

class TestGMXClusterSingularity():
    def setUp(self):
        fx.test_setup(self,'gmx_cluster_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_cluster_singularity(self):
        GMXCluster(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['ref_output_pdb_path'])