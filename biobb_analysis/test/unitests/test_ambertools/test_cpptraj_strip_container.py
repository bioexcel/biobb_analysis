from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_strip import CpptrajStrip


class TestCpptrajStripDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_strip_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_strip_docker(self):
        CpptrajStrip(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajStripSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_strip_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_strip_singularity(self):
        CpptrajStrip(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
