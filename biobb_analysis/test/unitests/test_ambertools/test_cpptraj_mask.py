# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_mask import cpptraj_mask


class TestCpptrajMask():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_mask')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_mask(self):
        cpptraj_mask(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
