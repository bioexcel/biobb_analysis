from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_trjconv_str_ens import GMXTrjConvStrEns


class TestGMXTrjConvStrEnsContainer():
    def setUp(self):
        fx.test_setup(self,'gmx_trjconv_str_ens_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_trjconv_str_ens_container(self):
        GMXTrjConvStrEns(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_str_ens_path'])
        assert fx.equal(self.paths['output_str_ens_path'], self.paths['ref_output_str_ens_path'])
