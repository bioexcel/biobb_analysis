from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_image import gmx_image
from biobb_analysis.gromacs.common import gmx_check
# import platform


class TestGMXImage():
    def setup_class(self):
        fx.test_setup(self, 'gmx_image')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_image(self):
        gmx_image(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_traj_path'])
        print(self.properties.get('binary_path', 'gmx'))
        assert gmx_check(self.paths['output_traj_path'], self.paths['ref_output_traj_path'], gmx=self.properties.get('binary_path', 'gmx'))
        # if platform.system() == 'Darwin':
        #    assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
