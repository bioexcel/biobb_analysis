from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_energy import GMXEnergy


class TestGMXEnergyDocker():
    def setUp(self):
        fx.test_setup(self,'gmx_energy_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_cluster_docker(self):
        GMXEnergy(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])

class TestGMXEnergySingularity():
    def setUp(self):
        fx.test_setup(self,'gmx_energy_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_cluster_singularity(self):
        GMXEnergy(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_xvg_path'])
        assert fx.equal(self.paths['output_xvg_path'], self.paths['ref_output_xvg_path'])