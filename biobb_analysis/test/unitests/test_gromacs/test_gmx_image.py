from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_image import GMXImage


class TestGMXImage():
    def setUp(self):
        fx.test_setup(self,'gmx_image')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_image(self):
        GMXImage(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
