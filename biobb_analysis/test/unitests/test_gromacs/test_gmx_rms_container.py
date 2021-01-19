from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_rms import gmx_rms


class TestGMXRmsDocker():
    def setUp(self):
        fx.test_setup(self,'gmx_rms_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_docker(self):
        gmx_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])

class TestGMXRmsSingularity():
    def setUp(self):
        fx.test_setup(self,'gmx_rms_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_rms_singularity(self):
        gmx_rms(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])