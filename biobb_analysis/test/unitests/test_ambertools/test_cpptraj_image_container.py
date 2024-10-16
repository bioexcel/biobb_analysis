# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_image import cpptraj_image


class TestCpptrajImageDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_image_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_image_docker(self):
        cpptraj_image(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajImageSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_image_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_image_singularity(self):
        cpptraj_image(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
