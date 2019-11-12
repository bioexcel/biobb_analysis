from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_rgyr import GMXRgyr


class TestGMXRgyr():
    def setUp(self):
        fx.test_setup(self,'gmx_rgyr')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rgyr(self):
        GMXRgyr(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])
