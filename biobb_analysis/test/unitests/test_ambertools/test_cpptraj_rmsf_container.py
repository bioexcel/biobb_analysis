from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rmsf import Rmsf


class TestCpptrajRmsfFirstContainer():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_first_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_first_container(self):
        Rmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfAverageContainer():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_average_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_average_container(self):
        Rmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfExperimentalContainer():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_experimental_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_experimental_container(self):
        Rmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

