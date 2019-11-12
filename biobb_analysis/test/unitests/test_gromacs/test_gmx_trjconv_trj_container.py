from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_trjconv_trj import GMXTrjConvTrj


class TestGMXTrjConvTrjContainer():
    def setUp(self):
        fx.test_setup(self,'gmx_trjconv_trj_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_trjconv_trj_container(self):
        GMXTrjConvTrj(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
