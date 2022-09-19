from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_mask import cpptraj_mask


class TestCpptrajMaskDocker():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_mask_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_mask_docker(self):
        cpptraj_mask(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

import pytest
@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajMaskSingularity():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_mask_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_mask_singularity(self):
        cpptraj_mask(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
