from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rms import Rms


class TestCpptrajRmsFirstContainer():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_first_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_first_container(self):
        Rms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsAverageContainer():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_average_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_average_container(self):
        Rms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsExperimentalContainer():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_experimental_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_experimental_container(self):
        Rms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
