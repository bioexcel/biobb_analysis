from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_trjconv_trj import gmx_trjconv_trj


class TestGMXTrjConvTrjDocker():
    def setUp(self):
        fx.test_setup(self,'gmx_trjconv_trj_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_trjconv_trj_docker(self):
        gmx_trjconv_trj(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])

class TestGMXTrjConvTrjSingularity():
    def setUp(self):
        fx.test_setup(self,'gmx_trjconv_trj_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_trjconv_trj_singularity(self):
        gmx_trjconv_trj(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])