from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rmsf import cpptraj_rmsf


class TestCpptrajRmsfFirstDocker():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_first_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_first_docker(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfAverageDocker():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_average_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_average_docker(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfExperimentalDocker():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_experimental_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_experimental_docker(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

import pytest
@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajRmsfFirstSingularity():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_first_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_first_singularity(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajRmsfAverageSingularity():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_average_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_average_singularity(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajRmsfExperimentalSingularity():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rmsf_experimental_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_experimental_singularity(self):
        cpptraj_rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])