# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.gromacs.gmx_check import gmx_check


class TestGMXCheck():
    def setup_class(self):
        fx.test_setup(self, 'gmx_check')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_check(self):
        gmx_check(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_log_path'])
        # assert fx.equal(self.paths['output_log_path'], self.paths['ref_output_log_path'])

