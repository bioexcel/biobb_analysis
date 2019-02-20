#!/usr/bin/env python3

"""Module containing the Cluster class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper


class Cluster():
    """Wrapper class for the GROMACS cluster (http://manual.gromacs.org/current/onlinehelp/gmx-cluster.html) module.

    Args:
        input_gro_path (str): Path to the original (before launching the trajectory) GROMACS structure file GRO.
        input_traj_path (str): Path to the GROMACS trajectory: TRR or XTC formats.
        output_pdb_path (str): Path to the output cluster PDB file.
        properties (dic):
            | - **dista** (*bool*) - (False) Use RMSD of distances instead of RMS deviation.
            | - **method** (*str*) - ("linkage") Method for cluster determination: linkage, jarvis-patrick, monte-carlo, diagonalization, gromos
            | - **cutoff** (*float*) - (0.1) RMSD cut-off (nm) for two structures to be neighbor
            | - **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
    """

    def __init__(self, input_gro_path, input_traj_path, output_pdb_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_gro_path = input_gro_path
        self.input_traj_path = input_traj_path
        self.output_pdb_path = output_pdb_path

        # Properties specific for BB
        self.dista = properties.get('dista', False)
        self.method = properties.get('method', "linkage")
        self.cutoff = properties.get('cutoff', 0.1)

        # Properties common in all GROMACS BB
        self.gmx_path = properties.get('gmx_path', 'gmx')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')


    def launch(self):
        """Launches the execution of the GROMACS rms module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        cmd = ['echo', '\"'+'1 1'+'\"', '|',
               self.gmx_path, 'cluster',
               '-s', self.input_gro_path,
               '-f', self.input_traj_path,
               '-cl', self.output_pdb_path,
               '-cutoff', str(self.cutoff),
               '-method', self.method]

        if self.dista:
            cmd.append('-dista')

        return cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()

def main():
    parser = argparse.ArgumentParser(description="Wrapper of the GROMACS cluster module.")
    parser.add_argument('--config', required=False)
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    #Specific args of each building block
    parser.add_argument('--input_gro_path', required=True)
    parser.add_argument('--input_traj_path', required=True)
    parser.add_argument('--output_pdb_path', required=True)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    Cluster(input_gro_path=args.input_gro_path, input_traj_path=args.input_traj_path, output_pdb_path=args.output_pdb_path, properties=properties).launch()

if __name__ == '__main__':
    main()
