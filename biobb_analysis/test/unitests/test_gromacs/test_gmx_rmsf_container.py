# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_rmsf import gmx_rmsf
import pytest
import sys

class TestGMXRmsfDocker():
    def setup_class(self):
        fx.test_setup(self, 'gmx_rmsf_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_docker(self):
        gmx_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])

@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestGMXRmsfSingularity():
    def setup_class(self):
        fx.test_setup(self, 'gmx_rmsf_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_singularity(self):
        gmx_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])
