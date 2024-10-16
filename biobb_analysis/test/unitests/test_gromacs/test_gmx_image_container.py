# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_image import gmx_image


class TestGMXImageDocker():
    def setup_class(self):
        fx.test_setup(self, 'gmx_image_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_image_docker(self):
        gmx_image(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_traj_path'])
        # assert gmx_check(self.paths['output_traj_path'], self.paths['ref_output_traj_path'], gmx=self.properties.get('binary_path', 'gmx'))
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestGMXImageSingularity():
    def setup_class(self):
        fx.test_setup(self, 'gmx_image_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_image_singularity(self):
        gmx_image(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
