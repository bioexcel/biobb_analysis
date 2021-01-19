from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_bfactor import cpptraj_bfactor


class TestCpptrajBfactorFirst():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_first')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_first(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajBfactorAverage():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_average')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_average(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajBfactorExperimental():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_experimental')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_experimental(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
