from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_dry import CpptrajDry


class TestCpptrajDryDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_dry_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_dry_docker(self):
        CpptrajDry(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajDrySingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_dry_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_dry_singularity(self):
        CpptrajDry(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
