from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_bfactor import cpptraj_bfactor


class TestCpptrajBfactorFirstDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_first_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_first_docker(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajBfactorFirstSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_first_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_first_singularity(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajBfactorAverageDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_average_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_average_docker(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajBfactorAverageSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_average_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_average_singularity(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajBfactorExperimentalDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_experimental_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_experimental_docker(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajBfactorExperimentalSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_bfactor_experimental_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_bfactor_experimental_singularity(self):
        cpptraj_bfactor(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])