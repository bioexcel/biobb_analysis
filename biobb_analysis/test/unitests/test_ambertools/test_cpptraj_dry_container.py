from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_dry import cpptraj_dry


class TestCpptrajDryDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_dry_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_dry_docker(self):
        cpptraj_dry(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajDrySingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_dry_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_dry_singularity(self):
        cpptraj_dry(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
