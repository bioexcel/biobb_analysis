from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_rmsf import CpptrajRmsf


class TestCpptrajRmsfFirstDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_first_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_first_docker(self):
        CpptrajRmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfAverageDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_average_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_average_docker(self):
        CpptrajRmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfExperimentalDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_experimental_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_experimental_docker(self):
        CpptrajRmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfFirstSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_first_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_first_singularity(self):
        CpptrajRmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfAverageSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_average_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_average_singularity(self):
        CpptrajRmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajRmsfExperimentalSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_rmsf_experimental_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rmsf_experimental_singularity(self):
        CpptrajRmsf(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])