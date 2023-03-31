from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rms import cpptraj_rms


class TestCpptrajRmsFirstDocker():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rms_first_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_first_docker(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])

class TestCpptrajRmsAverageDocker():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rms_average_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_average_docker(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])

class TestCpptrajRmsExperimentalDocker():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rms_experimental_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_experimental_docker(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])

import pytest
@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajRmsFirstSingularity():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rms_first_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_first_singularity(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])

@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajRmsAverageSingularity():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rms_average_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_average_singularity(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])

@pytest.mark.skip(reason="singularity currently not available")
class TestCpptrajRmsExperimentalSingularity():
    def setup_class(self):
        fx.test_setup(self,'cpptraj_rms_experimental_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_experimental_singularity(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])