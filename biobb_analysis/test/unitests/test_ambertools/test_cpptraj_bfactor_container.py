# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_bfactor import cpptraj_bfactor


class TestCpptrajBfactorFirstDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_bfactor_first_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_first_docker(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajBfactorFirstSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_bfactor_first_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_first_singularity(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


class TestCpptrajBfactorAverageDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_bfactor_average_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_average_docker(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajBfactorAverageSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_bfactor_average_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_average_singularity(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


class TestCpptrajBfactorExperimentalDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_bfactor_experimental_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_experimental_docker(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])


@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajBfactorExperimentalSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_bfactor_experimental_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_experimental_singularity(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
