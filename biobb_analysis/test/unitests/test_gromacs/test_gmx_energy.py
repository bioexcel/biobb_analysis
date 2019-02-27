from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_energy import GMXEnergy


class TestGMXEnergy():
    def setUp(self):
        fx.test_setup(self,'gmx_energy')

    def tearDown(self):
        #fx.test_teardown(self)
        pass

    def test_cluster(self):
        GMXEnergy(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])
