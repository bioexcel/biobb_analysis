from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_convert import Convert


class TestCpptrajConvertDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_convert_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_convert_docker(self):
        Convert(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajConvertSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_convert_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_convert_singularity(self):
        Convert(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])