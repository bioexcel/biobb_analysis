# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rms import cpptraj_rms


class TestCpptrajRmsFirst():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_rms_first')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_first(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])


class TestCpptrajRmsAverage():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_rms_average')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_average(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])


class TestCpptrajRmsExperimental():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_rms_experimental')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rms_experimental(self):
        cpptraj_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.not_empty(self.paths['output_traj_path'])
        assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
