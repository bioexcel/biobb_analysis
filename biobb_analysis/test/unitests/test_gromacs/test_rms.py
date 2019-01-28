from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.rms import Rms


class TestRms():
    def setUp(self):
        fx.test_setup(self,'rms')

    def tearDown(self):
        fx.test_teardown(self)

    def test_rms(self):
        Rms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])
