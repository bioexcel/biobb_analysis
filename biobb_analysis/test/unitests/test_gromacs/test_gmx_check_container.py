# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_check import gmx_check


class TestGMXCheckDocker():
    def setup_class(self):
        fx.test_setup(self, 'gmx_check_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_check_docker(self):
        gmx_check(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_log_path'])
        assert fx.equal(self.paths['output_log_path'], self.paths['ref_output_log_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestGMXCheckSingularity():
    def setup_class(self):
        fx.test_setup(self, 'gmx_check_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_check_singularity(self):
        gmx_check(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_log_path'])
        assert fx.equal(self.paths['output_log_path'], self.paths['ref_output_log_path'])


