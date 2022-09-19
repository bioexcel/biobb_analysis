from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_trjconv_str_ens import gmx_trjconv_str_ens


class TestGMXTrjConvStrEns():
    def setup_class(self):
        fx.test_setup(self,'gmx_trjconv_str_ens')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_trjconv_str_ens(self):
        gmx_trjconv_str_ens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_str_ens_path'])
        assert fx.equal(self.paths['output_str_ens_path'], self.paths['ref_output_str_ens_path'])
