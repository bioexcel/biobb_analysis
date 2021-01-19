from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_rgyr import gmx_rgyr


class TestGMXRgyrDocker():
    def setUp(self):
        fx.test_setup(self,'gmx_rgyr_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rgyr_docker(self):
        gmx_rgyr(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])

class TestGMXRgyrSingularity():
    def setUp(self):
        fx.test_setup(self,'gmx_rgyr_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rgyr_singularity(self):
        gmx_rgyr(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])