import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_slice import cpptraj_slice


class TestCpptrajSliceDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_slice_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_slice_docker(self):
        cpptraj_slice(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajSliceSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_slice_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_slice_singularity(self):
        cpptraj_slice(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
