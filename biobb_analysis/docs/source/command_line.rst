
BioBB Analysis Command Line Help
================================

Generic usage:

.. parsed-literal::

    biobb_command [-h] --config CONFIG [--system SYSTEM] [--step STEP] --input_file(s) <input_file(s)> --output_file <output_file>

Please refer to the `system & step
documentation <https://biobb-common.readthedocs.io/en/latest/system_step.html>`__
for more information of these two parameters.

--------------

Cpptraj average
---------------

Wrapper of the Ambertools Cpptraj module. Computing average structure.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_average -h

.. parsed-literal::

    usage: cpptraj_average [-h] [--config CONFIG] [--system SYSTEM] [--step STEP]
                           --input_top_path INPUT_TOP_PATH --input_traj_path
                           INPUT_TRAJ_PATH --output_cpptraj_path
                           OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Computing average structure.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input Amber structure or topology file.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input Amber trajectory to be processed.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed Amber trajectory or to
                            the output dat file containing the analysis results


Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **in_parameters** (*dict*) - (None) Parameters for input trajectory.
   Accepted parameters:

   -  **start** (*int*) - (1) Starting frame for slicing
   -  **end** (*int*) - (-1) Ending frame for slicing
   -  **step** (*int*) - (1) Step for slicing
   -  **mask** (*string*) - (“all-atoms”) Mask definition. Values:
      c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute,
      ions, solvent.

-  **out_parameters** (*dict*) - (None) Parameters for output
   trajectory.

   -  **format** (*str*) - (“netcdf”) Output trajectory format. Values:
      crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor,
      pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
   -  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj
      executable binary.

YAML file config
~~~~~~~~~~~~~~~~

average.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 1
        end: -1
        step: 1
        mask: c-alpha
      out_parameters:
        format: pdb

Command:

.. parsed-literal::

    cpptraj_average --config data/conf/average.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.average.nc

JSON file config
~~~~~~~~~~~~~~~~

average.json:

.. parsed-literal::

    {
      "properties": {
        "in_parameters": {
          "start": 1,
          "end": -1,
          "step": 1,
          "mask": "c-alpha"
        },
        "out_parameters": {
           "format": "pdb"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_average --config data/conf/average.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.average.nc

Cpptraj bfactor
---------------

Wrapper for the Ambertools Cpptraj module. Calculating B-Factor.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_bfactor -h

.. parsed-literal::

    usage: cpptraj_bfactor [-h] [--config CONFIG] [--system SYSTEM] [--step STEP]
                           --input_top_path INPUT_TOP_PATH --input_traj_path
                           INPUT_TRAJ_PATH [--input_exp_path INPUT_EXP_PATH]
                           --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper for the Ambertools Cpptraj module. Calculating B-Factor.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --input_exp_path INPUT_EXP_PATH
                            Path to the experimental reference file (required if reference = experimental).
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input Amber structure or topology file.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input Amber trajectory to be processed.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed Amber trajectory or to
                            the output dat file containing the analysis results.


Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **in_parameters** (*dict*) - (None) Parameters for input trajectory.
   Accepted parameters:

   -  **start** (*int*) - (1) Starting frame for slicing
   -  **end** (*int*) - (-1) Ending frame for slicing
   -  **step** (*int*) - (1) Step for slicing
   -  **mask** (*string*) - (“all-atoms”) Mask definition. Values:
      c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute,
      ions, solvent.
   -  **reference** (*string*) - (“first”) Reference definition. Values:
      first, average, experimental.

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

bfactor.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 1
        end: -1
        step: 1
        mask: c-alpha
        reference: first

Command:

.. parsed-literal::

    cpptraj_bfactor --config data/conf/bfactor.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.bfactor.dat

JSON file config
~~~~~~~~~~~~~~~~

bfactor.json:

.. parsed-literal::

    {
      "properties": {
        "in_parameters": {
          "start": 1,
          "end": -1,
          "step": 1,
          "mask": "c-alpha",
          "reference": "first"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_bfactor --config data/conf/bfactor.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.average.dat

Gromacs energy
--------------

Wrapper of the GROMACS energy
(http://manual.gromacs.org/current/onlinehelp/gmx-energy.html) module.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    gmx_energy -h

.. parsed-literal::

    usage: gmx_energy [-h] [--config CONFIG] [--system SYSTEM] [--step STEP]
                      --input_energy_path INPUT_ENERGY_PATH --output_xvg_path
                      OUTPUT_XVG_PATH
    
    Wrapper for the GROMACS energy module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_energy_path INPUT_ENERGY_PATH
                            Path to the input GROMACS energy file.
      --output_xvg_path OUTPUT_XVG_PATH
                            Path to the output analysis file.


Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **xvg** (*str*) - (“none”) XVG plot formatting: xmgrace, xmgr, none.
-  **terms** (*list*) - ([“Potential”]) Energy terms. Select one or more
   from: Angle, Proper-Dih., Improper-Dih., LJ-14, Coulomb-14, LJ-(SR),
   Coulomb-(SR), Coul.-recip., Position-Rest., Potential, Kinetic-En.,
   Total-Energy, Temperature, Pressure, Constr.-rmsd, Box-X, Box-Y,
   Box-Z, Volume, Density, pV, Enthalpy, Vir-XX, Vir-XY, Vir-XZ, Vir-YX,
   Vir-YY, Vir-YZ, Vir-ZX, Vir-ZY, Vir-ZZ, Pres-XX, Pres-XY, Pres-XZ,
   Pres-YX, Pres-YY, Pres-YZ, Pres-ZX, Pres-ZY, Pres-ZZ, #Surf*SurfTen,
   Box-Vel-XX, Box-Vel-YY, Box-Vel-ZZ, Mu-X, Mu-Y, Mu-Z, T-Protein,
   T-non-Protein, Lamb-Protein, Lamb-non-Protein
-  **gmx_path** (*str*) - (“gmx”) Path to the GROMACS executable binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx_energy.yml:

.. parsed-literal::

    properties:
      terms: [Potential, Pressure]

Command:

.. parsed-literal::

    gmx_energy --config data/conf/gmx_energy.yml --input_energy_path data/input/energy.edr --output_xvg_path data/output/output.energy.xvg

JSON file config
~~~~~~~~~~~~~~~~

gmx_energy.json:

.. parsed-literal::

    {
      "properties": {
        "terms": ["Potential", "Pressure"]
      }
    }

Command:

.. parsed-literal::

    gmx_energy --config data/conf/gmx_energy.json --input_energy_path data/input/energy.edr --output_xvg_path data/output/output.energy.xvg
