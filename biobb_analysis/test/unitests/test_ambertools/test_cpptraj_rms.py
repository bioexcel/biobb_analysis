from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rms import Rms


class TestCpptrajRmsFirst():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_first')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_first(self):
        Rms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsAverage():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_average')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_average(self):
        Rms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsExperimental():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_experimental')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_experimental(self):
        Rms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
