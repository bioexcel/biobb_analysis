# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_analysis.ambertools.cpptraj_input import CpptrajInput


class TestCpptrajInput():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_input')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_input(self):
        with open(self.paths['input_instructions_path'], 'w') as instructions:
            instructions.write(f"parm {self.paths['input_top_path']}\n"
                               f"trajin {self.paths['input_traj_path']}\n"
                               f"trajout {self.paths['output_cpptraj_path']} netcdf\n")
        CpptrajInput(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
