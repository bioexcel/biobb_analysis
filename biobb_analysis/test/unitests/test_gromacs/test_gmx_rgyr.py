# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_rgyr import gmx_rgyr


class TestGMXRgyr():
    def setup_class(self):
        fx.test_setup(self, 'gmx_rgyr')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rgyr(self):
        gmx_rgyr(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])
