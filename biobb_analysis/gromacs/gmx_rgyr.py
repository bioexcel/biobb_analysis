#!/usr/bin/env python3

"""Module containing the GMX Rgyr class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_analysis.gromacs.common import *


class GMXRgyr():
    """Wrapper of the GROMACS rgyr (http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-gyrate.html) module.

    Args:
        input_structure_path (str): Path to the input structure file: tpr, gro, g96, pdb, brk, ent.
        input_traj_path (str): Path to the GROMACS trajectory file: xtc, trr, cpt, gro, g96, pdb, tng.
        output_xvg_path (str): Path to the XVG output file.
        properties (dic):
            * **xvg** (*str*) - ("none") XVG plot formatting: xmgrace, xmgr, none.
            * **selection** (*str*) - ("Protein-H") Group where the rgyr will be performed: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
            * **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
    """

    def __init__(self, input_structure_path, input_traj_path, output_xvg_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_structure_path = check_input_path(input_structure_path)
        self.input_traj_path = check_traj_path(input_traj_path)
        self.output_xvg_path = check_out_xvg_path(output_xvg_path)

        # Properties specific for BB
        self.xvg = get_xvg(properties)
        self.selection = get_selection(properties)

        # Properties common in all GROMACS BB
        self.gmx_path = get_binary_path(properties, 'gmx_path')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

    def launch(self):
        """Launches the execution of the GROMACS rgyr module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        cmd = ['echo', '\"'+self.selection+'\"', '|',
               self.gmx_path, 'gyrate',
               '-s', self.input_structure_path,
               '-f', self.input_traj_path,
               '-o', self.output_xvg_path,
               '-xvg', self.xvg]

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the GROMACS rgyr module.")
    parser.add_argument('--config', required=False)
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    #Specific args of each building block
    parser.add_argument('--input_structure_path', required=True)
    parser.add_argument('--input_traj_path', required=True)
    parser.add_argument('--output_xvg_path', required=True)


    args = parser.parse_args()
    check_conf(args.config)
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    GMXRgyr(input_structure_path=args.input_structure_path, input_traj_path=args.input_traj_path, output_xvg_path=args.output_xvg_path, properties=properties).launch()

if __name__ == '__main__':
    main()
