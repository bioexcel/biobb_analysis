from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_average import CpptrajAverage


class TestCpptrajAverageDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_average_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_average_docker(self):
        CpptrajAverage(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajAverageSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_average_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_average_singularity(self):
        CpptrajAverage(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])