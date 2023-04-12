import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_strip import cpptraj_strip


class TestCpptrajStripDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_strip_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_strip_docker(self):
        cpptraj_strip(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajStripSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_strip_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_strip_singularity(self):
        cpptraj_strip(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
