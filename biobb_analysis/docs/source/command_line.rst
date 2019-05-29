
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

    usage: cpptraj_average [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Computing average structure.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed structure.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   structure.

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

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

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
        format: netcdf

Command:

.. parsed-literal::

    cpptraj_average --config data/conf/average.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.average.netcdf

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
           "format": "netcdf"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_average --config data/conf/average.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.average.netcdf

Cpptraj bfactor
---------------

Wrapper for the Ambertools Cpptraj module. Calculating B-Factor.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_bfactor -h

.. parsed-literal::

    usage: cpptraj_bfactor [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH [--input_exp_path INPUT_EXP_PATH] --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
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
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed analysis.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **input_exp_path** (*str*): Path to the experimental reference file
   (required if reference = experimental).
-  **output_cpptraj_path** (*str*): Path to the output processed
   analysis.

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

Cpptraj convert
---------------

Wrapper of the Ambertools Cpptraj module. Converting trajectory format.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_convert -h

.. parsed-literal::

    usage: cpptraj_convert [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Converting trajectory format.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed structure.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   structure.

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

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

convert.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 1
        end: -1
        step: 1
        mask: c-alpha
      out_parameters:
        format: netcdf

Command:

.. parsed-literal::

    cpptraj_convert --config data/conf/convert.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.convert.netcdf

JSON file config
~~~~~~~~~~~~~~~~

convert.json:

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
          "format": "netcdf"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_convert --config data/conf/convert.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.convert.netcdf

Cpptraj dry
-----------

Wrapper of the Ambertools Cpptraj module. Calculating dry structure.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_dry -h

.. parsed-literal::

    usage: cpptraj_dry [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Calculating dry structure.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed trajectory.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   trajectory.

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

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

dry.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 1
        end: -1
        step: 1
        mask: c-alpha
      out_parameters:
        format: netcdf

Command:

.. parsed-literal::

    cpptraj_dry --config data/conf/dry.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.dry.netcdf

JSON file config
~~~~~~~~~~~~~~~~

dry.json:

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
          "format": "netcdf"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_dry --config data/conf/dry.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.dry.netcdf

Cpptraj image
-------------

Wrapper of the Ambertools Cpptraj module. Calculating image.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_image -h

.. parsed-literal::

    usage: cpptraj_image [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Calculating image.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed trajectory.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   trajectory.

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

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

image.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 1
        end: -1
        step: 1
        mask: c-alpha
      out_parameters:
        format: netcdf

Command:

.. parsed-literal::

    cpptraj_image --config data/conf/image.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.image.netcdf

JSON file config
~~~~~~~~~~~~~~~~

image.json:

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
          "format": "netcdf"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_image --config data/conf/image.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.image.netcdf

Cpptraj input
-------------

Wrapper of the Ambertools Cpptraj module. Performing any Cpptraj
operation from a given instructions file.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_input -h

.. parsed-literal::

    usage: cpptraj_input [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_instructions_path INPUT_INSTRUCTIONS_PATH
    
    Wrapper of the Ambertools Cpptraj module. Performing any Cpptraj operation from a given instructions file.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_instructions_path INPUT_INSTRUCTIONS_PATH
                            Path of the instructions file.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_instructions_path** (*str*): Path of the instructions file.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

Instructions file
~~~~~~~~~~~~~~~~~

input.in:

.. parsed-literal::

    parm data/input/cpptraj.convert.pdb
    trajin data/input/cpptraj.convert.dcd
    trajout data/output/output.netcdf netcdf

YAML file config
~~~~~~~~~~~~~~~~

input.yml:

.. parsed-literal::

    properties:
      cpptraj_path: cpptraj

Command:

.. parsed-literal::

    cpptraj_input --config data/conf/input.yml --input_instructions_path data/input/input.in

JSON file config
~~~~~~~~~~~~~~~~

image.json:

.. parsed-literal::

    {
      "properties": {
        "cpptraj_path": "cpptraj"
      }
    }

Command:

.. parsed-literal::

    cpptraj_input --config data/conf/input.json --input_instructions_path data/input/input.in

Cpptraj mask
------------

Wrapper of the Ambertools Cpptraj module. Masking a trajectory.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_mask -h

.. parsed-literal::

    usage: cpptraj_mask [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Masking a trajectory.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed trajectory.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   trajectory.

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

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

mask.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 1
        end: -1
        step: 1
        mask: c-alpha
      out_parameters:
        format: netcdf

Command:

.. parsed-literal::

    cpptraj_mask --config data/conf/mask.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.mask.netcdf

JSON file config
~~~~~~~~~~~~~~~~

mask.json:

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
          "format": "netcdf"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_mask --config data/conf/mask.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.image.netcdf

Cpptraj rgyr
------------

Wrapper of the Ambertools Cpptraj module. Calculating Rgyr analysis.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_rgyr -h

.. parsed-literal::

    usage: cpptraj_rgyr [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Calculating Rgyr analysis.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output analysis.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   analysis.

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

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

rgyr.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 1
        end: -1
        step: 1
        mask: c-alpha

Command:

.. parsed-literal::

    cpptraj_rgyr --config data/conf/rgyr.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rgyr.dat

JSON file config
~~~~~~~~~~~~~~~~

rgyr.json:

.. parsed-literal::

    {
      "properties": {
        "in_parameters": {
          "start": 1,
          "end": -1,
          "step": 1,
          "mask": "c-alpha"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_rgyr --config data/conf/rgyr.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rgyr.dat

Cpptraj rms
-----------

Wrapper of the Ambertools Cpptraj module. Calculating Rms analysis.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_rms -h

.. parsed-literal::

    usage: cpptraj_rms [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH [--input_exp_path INPUT_EXP_PATH] --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Calculating Rms analysis.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --input_exp_path INPUT_EXP_PATH
                            Path to the experimental reference file (required if reference = experimental).
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed analysis.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **input_exp_path** (*str*): Path to the experimental reference file
   (required if reference = experimental).
-  **output_cpptraj_path** (*str*): Path to the output processed
   analysis.

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

rms.yml:

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

    cpptraj_rms --config data/conf/rms.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rms.dat

JSON file config
~~~~~~~~~~~~~~~~

rms.json:

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

    cpptraj_rms --config data/conf/rms.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rms.dat

Cpptraj rmsf
------------

Wrapper of the Ambertools Cpptraj module. Calculating Rmsf analysis.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_rmsf -h

.. parsed-literal::

    usage: cpptraj_rmsf [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH [--input_exp_path INPUT_EXP_PATH] --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Calculating Rmsf analysis.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --input_exp_path INPUT_EXP_PATH
                            Path to the experimental reference file (required if reference = experimental).
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed analysis.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **input_exp_path** (*str*): Path to the experimental reference file
   (required if reference = experimental).
-  **output_cpptraj_path** (*str*): Path to the output processed
   analysis.

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

rmsf.yml:

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

    cpptraj_rmsf --config data/conf/rmsf.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rmsf.dat

JSON file config
~~~~~~~~~~~~~~~~

rmsf.json:

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

    cpptraj_rmsf --config data/conf/rmsf.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rmsf.dat

Cpptraj slice
-------------

Wrapper of the Ambertools Cpptraj module. Calculating a slice from a
given trajectory.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_slice -h

.. parsed-literal::

    usage: cpptraj_slice [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Calculating a slice from a given trajectory.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed trajectory.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   trajectory.

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

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

slice.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 2
        end: 20
        step: 2
        mask: c-alpha
      out_parameters:
        format: netcdf

Command:

.. parsed-literal::

    cpptraj_slice --config data/conf/slice.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.slice.netcdf

JSON file config
~~~~~~~~~~~~~~~~

slice.json:

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
          "format": "netcdf"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_slice --config data/conf/slice.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.slice.netcdf

Cpptraj snapshot
----------------

Wrapper of the Ambertools Cpptraj module. Calculating a snapshot
structure.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_snapshot -h

.. parsed-literal::

    usage: cpptraj_snapshot [-h] --config CONFIG [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper of the Ambertools Cpptraj module. Calculating a snapshot structure.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed structure.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   structure.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **in_parameters** (*dict*) - (None) Parameters for input trajectory.
   Accepted parameters:

   -  **snapshot** (*int*) - (1) Frame to be captured for snapshot
   -  **mask** (*string*) - (“all-atoms”) Mask definition. Values:
      c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute,
      ions, solvent.

-  **out_parameters** (*dict*) - (None) Parameters for output
   trajectory.

   -  **format** (*str*) - (“netcdf”) Output trajectory format. Values:
      crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor,
      pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

snapshot.yml:

.. parsed-literal::

    properties:
      in_parameters:
        snapshot: 12
        mask: c-alpha
      out_parameters:
        format: pdb

Command:

.. parsed-literal::

    cpptraj_snapshot --config data/conf/snapshot.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.snapshot.pdb

JSON file config
~~~~~~~~~~~~~~~~

snapshot.json:

.. parsed-literal::

    {
      "properties": {
        "in_parameters": {
          "snapshot": 12,
          "mask": "c-alpha"
        },
        "out_parameters": {
          "format": "pdb"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_snapshot --config data/conf/slice.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.slice.netcdf

Cpptraj strip
-------------

Wrapper of the Ambertools Cpptraj module. Stripping a trajectory.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    cpptraj_strip -h

.. parsed-literal::

    usage: cpptraj_strip [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
    
    Wrapper for the Ambertools Cpptraj module. Stripping a trajectory.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed trajectory.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_top_path** (*str*): Path to the input structure or topology
   file. Accepted formats: top, pdb, prmtop, parmtop, zip.
-  **input_traj_path** (*str*): Path to the input trajectory to be
   processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart,
   restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif,
   arc, sqm, sdf, conflib.
-  **output_cpptraj_path** (*str*): Path to the output processed
   trajectory.

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

-  **cpptraj_path** (*str*) - (“cpptraj”) Path to the cpptraj executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

strip.yml:

.. parsed-literal::

    properties:
      in_parameters:
        start: 2
        end: 20
        step: 2
        mask: c-alpha
      out_parameters:
        format: netcdf

Command:

.. parsed-literal::

    cpptraj_strip --config data/conf/strip.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.strip.netcdf

JSON file config
~~~~~~~~~~~~~~~~

strip.json:

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
          "format": "netcdf"
        }
      }
    }

Command:

.. parsed-literal::

    cpptraj_strip --config data/conf/strip.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.strip.netcdf

Gromacs cluster
---------------

Wrapper class for the GROMACS cluster
(http://manual.gromacs.org/current/onlinehelp/gmx-cluster.html) module.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    gmx_cluster -h

.. parsed-literal::

    usage: gmx_cluster [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_structure_path INPUT_STRUCTURE_PATH --input_traj_path INPUT_TRAJ_PATH --output_pdb_path OUTPUT_PDB_PATH
    
    Wrapper of the GROMACS cluster module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_structure_path INPUT_STRUCTURE_PATH
                            Path to the input structure file: tpr, gro, g96, pdb, brk, ent.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the GROMACS trajectory file: xtc, trr, cpt, gro, g96, pdb, tng.
      --output_pdb_path OUTPUT_PDB_PATH
                            Path to the output cluster file: xtc, trr, cpt, gro, g96, pdb, tng.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_structure_path** (*str*): Path to the input structure file:
   tpr, gro, g96, pdb, brk, ent.
-  **input_traj_path** (*str*): Path to the GROMACS trajectory file:
   xtc, trr, cpt, gro, g96, pdb, tng.
-  **output_pdb_path** (*str*): Path to the output cluster file: xtc,
   trr, cpt, gro, g96, pdb, tng.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **dista** (*bool*) - (False) Use RMSD of distances instead of RMS
   deviation.
-  **method** (*str*) - (“linkage”) Method for cluster determination:
   linkage, jarvis-patrick, monte-carlo, diagonalization, gromos
-  **cutoff** (*float*) - (0.1) RMSD cut-off (nm) for two structures to
   be neighbor
-  **gmx_path** (*str*) - (“gmx”) Path to the GROMACS executable binary.

YAML file config
~~~~~~~~~~~~~~~~

cluster.yml:

.. parsed-literal::

    properties:
      dista: False
      method: linkage
      cutoff: 0.1

Command:

.. parsed-literal::

    gmx_cluster --config data/conf/cluster.yml --input_structure_path data/input/cluster.gro --input_traj_path data/input/cluster.trr --output_pdb_path data/output/output.cluster.pdb

JSON file config
~~~~~~~~~~~~~~~~

cluster.json:

.. parsed-literal::

    {
      "properties": {
        "dista": false,
        "method": "linkage",
        "cutoff": 0.1
      }
    }

Command:

.. parsed-literal::

    gmx_cluster --config data/conf/cluster.json --input_structure_path data/input/cluster.gro --input_traj_path data/input/cluster.trr --output_pdb_path data/output/output.cluster.pdb

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

    usage: gmx_energy [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_energy_path INPUT_ENERGY_PATH --output_xvg_path OUTPUT_XVG_PATH
    
    Wrapper for the GROMACS energy module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_energy_path INPUT_ENERGY_PATH
                            Path to the input EDR file.
      --output_xvg_path OUTPUT_XVG_PATH
                            Path to the XVG output file.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_energy_path** (*str*): Path to the input EDR file.
-  **output_xvg_path** (*str*): Path to the XVG output file.

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

energy.yml:

.. parsed-literal::

    properties:
      terms: [Potential, Pressure]

Command:

.. parsed-literal::

    gmx_energy --config data/conf/energy.yml --input_energy_path data/input/energy.edr --output_xvg_path data/output/output.energy.xvg

JSON file config
~~~~~~~~~~~~~~~~

energy.json:

.. parsed-literal::

    {
      "properties": {
        "terms": ["Potential", "Pressure"]
      }
    }

Command:

.. parsed-literal::

    gmx_energy --config data/conf/energy.json --input_energy_path data/input/energy.edr --output_xvg_path data/output/output.energy.xvg

Gromacs image
-------------

Wrapper of the GROMACS trjconv
(http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-trjconv.html)
module.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    gmx_image -h

.. parsed-literal::

    usage: gmx_image [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_traj_path INPUT_TRAJ_PATH --input_top_path INPUT_TOP_PATH --output_traj_path OUTPUT_TRAJ_PATH
    
    Wrapper of the GROMACS trjconv module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the GROMACS trajectory file: xtc, trr, cpt, gro, g96, pdb, tng.
      --input_top_path INPUT_TOP_PATH
                            Path to the GROMACS input topology file: tpr, gro, g96, pdb, brk, ent.
      --output_traj_path OUTPUT_TRAJ_PATH
                            Path to the output file: xtc, trr, gro, g96, pdb, tng.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_traj_path** (*str*): Path to the GROMACS trajectory file:
   xtc, trr, cpt, gro, g96, pdb, tng.
-  **input_top_path** (*str*): Path to the GROMACS input topology file:
   tpr, gro, g96, pdb, brk, ent.
-  **output_traj_path** (*str*): Path to the output file: xtc, trr, gro,
   g96, pdb, tng.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **center_selection** (*str*) - (“System”) Group where the trjconv
   will be performed: System, Protein, Protein-H, C-alpha, Backbone,
   MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H,
   Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL,
   Water_and_ions.
-  **output_selection** (*str*) - (“System”) Group that is going to be
   written in the output trajectory: System, Protein, Protein-H,
   C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain,
   SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion,
   NA, CL, Water_and_ions.
-  **pbc** (*str*) - (“mol”) PBC treatment (see help text for full
   description): none, mol, res, atom, nojump, cluster, whole
-  **center** (*bool*) - (True) Center atoms in box.
-  **ur** (*str*) - (“compact”) Unit-cell representation: rect, tric,
   compact.
-  **fit** (*str*) - (“none”) Fit molecule to ref structure in the
   structure file: none, rot+trans, rotxy+transxy, translation, transxy,
   progressive.
-  **gmx_path** (*str*) - (“gmx”) Path to the GROMACS executable binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx_image.yml:

.. parsed-literal::

    properties:
      center_selection: Protein-H
      output_selection: Protein-H
      pbc: mol
      center: True
      fit: none
      ur: compact

Command:

.. parsed-literal::

    gmx_image --config data/conf/gmx_image.yml --input_traj_path data/input/image.trr --input_top_path data/input/image.gro --output_traj_path data/output/output.image.xtc

JSON file config
~~~~~~~~~~~~~~~~

gmx_image.json:

.. parsed-literal::

    {
      "properties": {
        "center_selection": "Protein-H",
        "output_selection": "Protein-H",
        "pbc": "mol",
        "center": true,
        "fit": "none",
        "ur": "compact"
      }
    }

Command:

.. parsed-literal::

    gmx_image --config data/conf/gmx_image.json --input_traj_path data/input/image.trr --input_top_path data/input/image.gro --output_traj_path data/output/output.image.xtc

Gromacs rgyr
------------

Wrapper of the GROMACS rgyr
(http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-gyrate.html)
module.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    gmx_rgyr -h

.. parsed-literal::

    usage: gmx_rgyr [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_structure_path INPUT_STRUCTURE_PATH --input_traj_path INPUT_TRAJ_PATH --output_xvg_path OUTPUT_XVG_PATH
    
    Wrapper for the GROMACS rgyr module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_structure_path INPUT_STRUCTURE_PATH
                            Path to the input structure file: tpr, gro, g96, pdb, brk, ent.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the GROMACS trajectory file: xtc, trr, cpt, gro, g96, pdb, tng.
      --output_xvg_path OUTPUT_XVG_PATH
                            Path to the XVG output file.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_structure_path** (*str*): Path to the input structure file:
   tpr, gro, g96, pdb, brk, ent.
-  **input_traj_path** (*str*): Path to the GROMACS trajectory file:
   xtc, trr, cpt, gro, g96, pdb, tng.
-  **output_xvg_path** (*str*): Path to the XVG output file.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **xvg** (*str*) - (“none”) XVG plot formatting: xmgrace, xmgr, none.
-  **selection** (*str*) - (“System”) Group where the rgyr will be
   performed: System, Protein, Protein-H, C-alpha, Backbone, MainChain,
   MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses,
   non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
-  **gmx_path** (*str*) - (“gmx”) Path to the GROMACS executable binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx_rgyr.yml:

.. parsed-literal::

    properties:
      selection: Protein-H

Command:

.. parsed-literal::

    gmx_rgyr --config data/conf/gmx_rgyr.yml --input_structure_path data/input/rgyr.gro --input_traj_path data/input/rgyr.trr --output_xvg_path data/output/output.rgyr.xvg

JSON file config
~~~~~~~~~~~~~~~~

gmx_rgyr.json:

.. parsed-literal::

    {
      "properties": {
        "selection": "Protein-H"
      }
    }

Command:

.. parsed-literal::

    gmx_rgyr --config data/conf/gmx_rgyr.json --input_structure_path data/input/rgyr.gro --input_traj_path data/input/rgyr.trr --output_xvg_path data/output/output.rgyr.xvg

Gromacs rms
-----------

Wrapper of the GROMACS rms
(http://manual.gromacs.org/current/onlinehelp/gmx-rms.html) module.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    gmx_rms -h

.. parsed-literal::

    usage: gmx_rms [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_structure_path INPUT_STRUCTURE_PATH --input_traj_path INPUT_TRAJ_PATH --output_xvg_path OUTPUT_XVG_PATH
    
    Wrapper for the GROMACS rms module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_structure_path INPUT_STRUCTURE_PATH
                            Path to the input structure file: tpr, gro, g96, pdb, brk, ent.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the GROMACS trajectory file: xtc, trr, cpt, gro, g96, pdb, tng.
      --output_xvg_path OUTPUT_XVG_PATH
                            Path to the XVG output file.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_structure_path** (*str*): Path to the input structure file:
   tpr, gro, g96, pdb, brk, ent.
-  **input_traj_path** (*str*): Path to the GROMACS trajectory file:
   xtc, trr, cpt, gro, g96, pdb, tng.
-  **output_xvg_path** (*str*): Path to the XVG output file.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **xvg** (*str*) - (“none”) XVG plot formatting: xmgrace, xmgr, none.
-  **selection** (*str*) - (“System”) Group where the rgyr will be
   performed: System, Protein, Protein-H, C-alpha, Backbone, MainChain,
   MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses,
   non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
-  **gmx_path** (*str*) - (“gmx”) Path to the GROMACS executable binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx_rms.yml:

.. parsed-literal::

    properties:
      selection: Protein-H

Command:

.. parsed-literal::

    gmx_rms --config data/conf/gmx_rms.yml --input_structure_path data/input/rgyr.gro --input_traj_path data/input/rgyr.trr --output_xvg_path data/output/output.rms.xvg

JSON file config
~~~~~~~~~~~~~~~~

gmx_rgyr.json:

.. parsed-literal::

    {
      "properties": {
        "selection": "Protein-H"
      }
    }

Command:

.. parsed-literal::

    gmx_rms --config data/conf/gmx_rms.json --input_structure_path data/input/rgyr.gro --input_traj_path data/input/rgyr.trr --output_xvg_path data/output/output.rms.xvg

Gromacs trjconv structure
-------------------------

Wrapper of the GROMACS trjconv
(http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-trjconv.html)
module.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    gmx_trjconv_str -h

.. parsed-literal::

    usage: gmx_trjconv_str [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_structure_path INPUT_STRUCTURE_PATH --input_top_path INPUT_TOP_PATH --output_str_path OUTPUT_STR_PATH
    
    Wrapper of the GROMACS trjconv module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_structure_path INPUT_STRUCTURE_PATH
                            Path to the input structure file: xtc, trr, cpt, gro, g96, pdb, tng.
      --input_top_path INPUT_TOP_PATH
                            Path to the GROMACS input topology file: tpr, gro, g96, pdb, brk, ent.
      --output_str_path OUTPUT_STR_PATH
                            Path to the output file: xtc, trr, gro, g96, pdb, tng.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_structure_path** (*str*): Path to the input structure file:
   xtc, trr, cpt, gro, g96, pdb, tng.
-  **input_top_path** (*str*): Path to the GROMACS input topology file:
   tpr, gro, g96, pdb, brk, ent.
-  **output_str_path** (*str*): Path to the output file: xtc, trr, gro,
   g96, pdb, tng.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **selection** (*str*) - (“System”) Group where the trjconv will be
   performed: System, Protein, Protein-H, C-alpha, Backbone, MainChain,
   MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses,
   non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
-  **gmx_path** (*str*) - (“gmx”) Path to the GROMACS executable binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx_trjconv_str.yml:

.. parsed-literal::

    properties:
      selection: Protein-H

Command:

.. parsed-literal::

    gmx_trjconv_str --config data/conf/gmx_trjconv_str.yml --input_structure_path data/input/trjconv.str.gro --input_top_path data/input/trjconv.str.gro --output_str_path data/output/output.trjconv.str.pdb

JSON file config
~~~~~~~~~~~~~~~~

gmx_rgyr.json:

.. parsed-literal::

    {
      "properties": {
        "selection": "Protein-H"
      }
    }

Command:

.. parsed-literal::

    gmx_trjconv_str --config data/conf/gmx_trjconv_str.json --input_structure_path data/input/trjconv.str.gro --input_top_path data/input/trjconv.str.gro --output_str_path data/output/output.trjconv.str.pdb

Gromacs trjconv structure ensemble
----------------------------------

Wrapper of the GROMACS trjconv
(http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-trjconv.html)
module.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    gmx_trjconv_str_ens -h

.. parsed-literal::

    usage: gmx_trjconv_str_ens [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_traj_path INPUT_TRAJ_PATH --input_top_path INPUT_TOP_PATH --output_str_ens_path OUTPUT_STR_ENS_PATH
    
    Wrapper of the GROMACS trjconv module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the GROMACS trajectory file: xtc, trr, cpt, gro, g96, pdb, tng.
      --input_top_path INPUT_TOP_PATH
                            Path to the GROMACS input topology file: tpr, gro, g96, pdb, brk, ent.
      --output_str_ens_path OUTPUT_STR_ENS_PATH
                            Path to the output file: zip.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_traj_path** (*str*): Path to the input structure file: xtc,
   trr, cpt, gro, g96, pdb, tng.
-  **input_top_path** (*str*): Path to the GROMACS input topology file:
   tpr, gro, g96, pdb, brk, ent.
-  **output_str_ens_path** (*str*): Path to the output file: zip.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **selection** (*str*) - (“System”) Group where the trjconv will be
   performed: System, Protein, Protein-H, C-alpha, Backbone, MainChain,
   MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses,
   non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
-  **start** (*int*) - (0) Time of first frame to read from trajectory
   (default unit ps).
-  **end** (*int*) - (0) Time of last frame to read from trajectory
   (default unit ps).
-  **dt** (*int*) - (0) Only write frame when t MOD dt = first time
   (ps).
-  **output_name** (*str*) - (“output”) File name for ensemble of output
   files.
-  **output_type** (*str*) - (“pdb”) File type for ensemble of output
   files: gro, g96, pdb.
-  **gmx_path** (*str*) - (“gmx”) Path to the GROMACS executable binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx_trjconv_str_ens.yml:

.. parsed-literal::

    properties:
      selection: Protein-H
      start: 0
      end: 10
      dt: 1
      output_name: output
      output_type: pdb

Command:

.. parsed-literal::

    gmx_trjconv_str_ens --config data/conf/gmx_trjconv_str_ens.yml --input_traj_path data/input/trjconv.str.ens.trr --input_top_path data/input/trjconv.str.ens.gro --output_str_ens_path data/output/output.trjconv.str.ens.zip

JSON file config
~~~~~~~~~~~~~~~~

gmx_rgyr.json:

.. parsed-literal::

    {
      "properties": {
        "selection": "Protein-H",
        "start": 0,
        "end": 10,
        "dt": 1,
        "output_name": "output",
        "output_type": "pdb"
      }
    }

Command:

.. parsed-literal::

    gmx_trjconv_str_ens --config data/conf/gmx_trjconv_str_ens.json --input_traj_path data/input/trjconv.str.ens.trr --input_top_path data/input/trjconv.str.ens.gro --output_str_ens_path data/output/output.trjconv.str.ens.zip

Gromacs trjconv trajectory
--------------------------

Wrapper of the GROMACS trjconv
(http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-trjconv.html)
module.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    gmx_trjconv_trj -h

.. parsed-literal::

    usage: gmx_trjconv_trj [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_traj_path INPUT_TRAJ_PATH --output_traj_path OUTPUT_TRAJ_PATH
    
    Wrapper of the GROMACS trjconv module.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the GROMACS trajectory file: xtc, trr, cpt, gro, g96, pdb, tng.
      --output_traj_path OUTPUT_TRAJ_PATH
                            Path to the output file: xtc, trr, gro, g96, pdb, tng.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_traj_path** (*str*): Path to the GROMACS trajectory file:
   xtc, trr, cpt, gro, g96, pdb, tng.
-  **output_traj_path** (*str*): Path to the output file: xtc, trr, gro,
   g96, pdb, tng.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **selection** (*str*) - (“System”) Group where the trjconv will be
   performed: System, Protein, Protein-H, C-alpha, Backbone, MainChain,
   MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses,
   non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
-  **start** (*int*) - (0) Time of first frame to read from trajectory
   (default unit ps).
-  **end** (*int*) - (0) Time of last frame to read from trajectory
   (default unit ps).
-  **dt** (*int*) - (0) Only write frame when t MOD dt = first time
   (ps).
-  **gmx_path** (*str*) - (“gmx”) Path to the GROMACS executable binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx_trjconv_trj.yml:

.. parsed-literal::

    properties:
      selection: Protein-H
      start: 0
      end: 0
      dt: 0

Command:

.. parsed-literal::

    gmx_trjconv_trj --config data/conf/gmx_trjconv_str_ens.yml --input_traj_path data/input/trjconv.trj.trr --output_traj_path data/output/output.trjconv.trj.xtc

JSON file config
~~~~~~~~~~~~~~~~

gmx_rgyr.json:

.. parsed-literal::

    {
      "properties": {
        "selection": "Protein-H",
        "start": 0,
        "end": 0,
        "dt": 0
      }
    }

Command:

.. parsed-literal::

    gmx_trjconv_trj --config data/conf/gmx_trjconv_str_ens.json --input_traj_path data/input/trjconv.trj.trr --output_traj_path data/output/output.trjconv.trj.xtc

