from biobb_common.tools import test_fixtures as fx
from gromacs.editconf import Editconf
from biobb_analysis.ambertools.cpptraj import Cpptraj


class TestCpptraj():
    def setUp(self):
        fx.test_setup(self,'cpptraj')

    def tearDown(self):
        fx.test_teardown(self)

    def test_rms(self):
        Cpptraj(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_dat_path'])
        assert fx.equal(self.paths['output_dat_path'], self.paths['ref_output_dat_path'])
