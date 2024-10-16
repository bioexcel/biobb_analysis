# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_strip import cpptraj_strip


class TestCpptrajStrip():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_strip')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_strip(self):
        cpptraj_strip(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
