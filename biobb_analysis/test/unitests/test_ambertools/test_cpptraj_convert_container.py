import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_convert import cpptraj_convert


class TestCpptrajConvertDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_convert_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_convert_docker(self):
        cpptraj_convert(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajConvertSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_convert_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_convert_singularity(self):
        cpptraj_convert(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])