from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_image import CpptrajImage


class TestCpptrajImageDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_image_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_image_docker(self):
        CpptrajImage(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajImageSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_image_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_image_singularity(self):
        CpptrajImage(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
