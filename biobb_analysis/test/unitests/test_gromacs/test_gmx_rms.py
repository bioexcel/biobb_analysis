# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_rms import gmx_rms
import platform


class TestGMXRms():
    def setup_class(self):
        fx.test_setup(self, 'gmx_rms')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms(self):
        gmx_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        if platform.system() == 'Darwin':
            assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])
