from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_slice import cpptraj_slice


class TestCpptrajSlice():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_slice')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_slice(self):
        cpptraj_slice(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
