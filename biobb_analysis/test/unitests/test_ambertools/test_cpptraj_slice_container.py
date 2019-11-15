from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_slice import Slice


class TestCpptrajSliceDocker():
    def setUp(self):
        fx.test_setup(self,'cpptraj_slice_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_slice_docker(self):
        Slice(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])

class TestCpptrajSliceSingularity():
    def setUp(self):
        fx.test_setup(self,'cpptraj_slice_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_slice_singularity(self):
        Slice(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])