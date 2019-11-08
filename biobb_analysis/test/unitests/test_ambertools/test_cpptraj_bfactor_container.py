from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_bfactor import Bfactor


class TestCpptrajBfactorContainer():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_container(self):
        Bfactor(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

