# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rgyr import cpptraj_rgyr


class TestCpptrajRgyrDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_rgyr_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rgyr_docker(self):
        cpptraj_rgyr(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajRgyrSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_rgyr_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rgyr_singularity(self):
        cpptraj_rgyr(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
