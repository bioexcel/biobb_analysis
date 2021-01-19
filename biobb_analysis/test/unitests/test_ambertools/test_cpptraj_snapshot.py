from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_snapshot import cpptraj_snapshot


class TestCpptrajSnapshot():
    def setUp(self):
        fx.test_setup(self,'cpptraj_snapshot')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_snapshot(self):
        cpptraj_snapshot(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
