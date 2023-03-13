from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_average import cpptraj_average

class TestCpptrajAverage():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_average')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_average(self):
        cpptraj_average(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
