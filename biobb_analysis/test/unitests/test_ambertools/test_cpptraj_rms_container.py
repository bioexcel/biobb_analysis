from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rms import CpptrajRms


class TestCpptrajRmsFirstDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_first_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_first_docker(self):
        CpptrajRms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsAverageDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_average_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_average_docker(self):
        CpptrajRms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsExperimentalDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_experimental_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_experimental_docker(self):
        CpptrajRms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsFirstSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_first_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_first_singularity(self):
        CpptrajRms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsAverageSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_average_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_average_singularity(self):
        CpptrajRms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsExperimentalSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rms_experimental_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_experimental_singularity(self):
        CpptrajRms(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])