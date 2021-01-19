from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_trjconv_str import gmx_trjconv_str


class TestGMXTrjConvStr():
    def setUp(self):
        fx.test_setup(self,'gmx_trjconv_str')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_trjconv_str(self):
        gmx_trjconv_str(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_str_path'])
        assert fx.equal(self.paths['output_str_path'], self.paths['ref_output_str_path'])
