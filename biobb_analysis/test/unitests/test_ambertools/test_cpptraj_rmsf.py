from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rmsf import cpptraj_rmsf


class TestCpptrajRmsfFirst():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_first')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_first(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfAverage():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_average')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_average(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfExperimental():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_experimental')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_experimental(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

