# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_rmsf import gmx_rmsf
import platform

class TestGMXRmsf():
    def setup_class(self):
        fx.test_setup(self, 'gmx_rmsf')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf(self):
        gmx_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        if platform.system() == 'Darwin':
            assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])
