from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_slice import Slice


class TestCpptrajSliceContainer():
    def setUp(self):
        fx.test_setup(self,'cpptraj_slice_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_slice_container(self):
        Slice(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
