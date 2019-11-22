
# BioBB Analysis Command Line Help

Generic usage:


```python
biobb_command [-h] --config CONFIG [--system SYSTEM] [--step STEP] --input_file(s) <input_file(s)> --output_file <output_file>
```

Please refer to the [system & step documentation](https://biobb-common.readthedocs.io/en/latest/system_step.html) for more information of these two parameters.

-----------------

## Cpptraj average

Calculates a structure average of a given cpptraj compatible trajectory.

### Get help

Command:


```python
cpptraj_average -h
```


```python
usage: cpptraj_average [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Calculates a structure average of a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed structure.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **out_parameters** (*dict*) - (None) Parameters for output trajectory.
    * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

average.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
  out_parameters:
    format: netcdf
```

Command:


```python
cpptraj_average --config data/conf/average.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.average.netcdf
```

### JSON file config

average.json:


```python
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
```

Command:


```python
cpptraj_average --config data/conf/average.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.average.netcdf
```

## Cpptraj bfactor

Calculates the Bfactor fluctuations of a given cpptraj compatible trajectory.

### Get help

Command:


```python
cpptraj_bfactor -h
```


```python
usage: cpptraj_bfactor [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH [--input_exp_path INPUT_EXP_PATH] --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Calculates the Bfactor fluctuations of a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **input_exp_path** (*str*): Path to the experimental reference file (required if reference = experimental).
* **output_cpptraj_path** (*str*): Path to the output processed analysis.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
    * **reference** (*string*) - ("first") Reference definition. Values: first, average, experimental.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

bfactor.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
    reference: first
```

Command:


```python
cpptraj_bfactor --config data/conf/bfactor.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.bfactor.dat
```

### JSON file config

bfactor.json:


```python
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
```

Command:


```python
cpptraj_bfactor --config data/conf/bfactor.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.average.dat
```

## Cpptraj convert

Converts between cpptraj compatible trajectory file formats and/or extracts a selection of atoms or frames.

### Get help

Command:


```python
cpptraj_convert -h
```


```python
usage: cpptraj_convert [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Converts between cpptraj compatible trajectory file formats and/or extracts a selection of atoms or frames.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed structure.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **out_parameters** (*dict*) - (None) Parameters for output trajectory.
    * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

convert.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
  out_parameters:
    format: netcdf
```

Command:


```python
cpptraj_convert --config data/conf/convert.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.convert.netcdf
```

### JSON file config

convert.json:


```python
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
```

Command:


```python
cpptraj_convert --config data/conf/convert.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.convert.netcdf
```

## Cpptraj dry

Dehydrates a given cpptraj compatible trajectory stripping out solvent molecules and ions.

### Get help

Command:


```python
cpptraj_dry -h
```


```python
usage: cpptraj_dry [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Dehydrates a given cpptraj compatible trajectory stripping out solvent molecules and ions.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed trajectory.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **out_parameters** (*dict*) - (None) Parameters for output trajectory.
    * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

dry.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
  out_parameters:
    format: netcdf
```

Command:


```python
cpptraj_dry --config data/conf/dry.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.dry.netcdf
```

### JSON file config

dry.json:


```python
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
```

Command:


```python
cpptraj_dry --config data/conf/dry.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.dry.netcdf
```

## Cpptraj image

Corrects periodicity (image) from a given cpptraj trajectory file.

### Get help

Command:


```python
cpptraj_image -h
```


```python
usage: cpptraj_image [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Corrects periodicity (image) from a given cpptraj trajectory file.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed trajectory.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **out_parameters** (*dict*) - (None) Parameters for output trajectory.
    * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

image.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
  out_parameters:
    format: netcdf
```

Command:


```python
cpptraj_image --config data/conf/image.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.image.netcdf
```

### JSON file config

image.json:


```python
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
```

Command:


```python
cpptraj_image --config data/conf/image.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.image.netcdf
```

## Cpptraj input

Performs multiple analysis and trajectory operations of a given trajector

### Get help

Command:


```python
cpptraj_input -h
```


```python
usage: cpptraj_input [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_instructions_path INPUT_INSTRUCTIONS_PATH

Performs multiple analysis and trajectory operations of a given trajectory.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help

required arguments:
  --input_instructions_path INPUT_INSTRUCTIONS_PATH
                        Path of the instructions file.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_instructions_path** (*str*): Path of the instructions file.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

### Instructions file

input.in:


```python
parm data/input/cpptraj.convert.pdb
trajin data/input/cpptraj.convert.dcd
trajout data/output/output.netcdf netcdf
```

### YAML file config

input.yml:


```python
properties:
  cpptraj_path: cpptraj
```

Command:


```python
cpptraj_input --config data/conf/input.yml --input_instructions_path data/input/input.in
```

### JSON file config

image.json:


```python
{
  "properties": {
    "cpptraj_path": "cpptraj"
  }
}
```

Command:


```python
cpptraj_input --config data/conf/input.json --input_instructions_path data/input/input.in
```

## Cpptraj mask

Extracts a selection of atoms from a given cpptraj compatible trajectory.

### Get help

Command:


```python
cpptraj_mask -h
```


```python
usage: cpptraj_mask [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Extracts a selection of atoms from a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed trajectory.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **out_parameters** (*dict*) - (None) Parameters for output trajectory.
    * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

mask.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
  out_parameters:
    format: netcdf
```

Command:


```python
cpptraj_mask --config data/conf/mask.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.mask.netcdf
```

### JSON file config

mask.json:


```python
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
```

Command:


```python
cpptraj_mask --config data/conf/mask.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.image.netcdf
```

## Cpptraj rgyr

Computes the radius of gyration (Rgyr) from a given cpptraj compatible trajectory.

### Get help

Command:


```python
cpptraj_rgyr -h
```


```python
usage: cpptraj_rgyr [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Computes the radius of gyration (Rgyr) from a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed analysis.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

rgyr.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
```

Command:


```python
cpptraj_rgyr --config data/conf/rgyr.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rgyr.dat
```

### JSON file config

rgyr.json:


```python
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
```

Command:


```python
cpptraj_rgyr --config data/conf/rgyr.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rgyr.dat
```

## Cpptraj rms

Calculates the Root Mean Square deviation (RMSd) of a given cpptraj compatible trajectory.s.

### Get help

Command:


```python
cpptraj_rms -h
```


```python
usage: cpptraj_rms [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH [--input_exp_path INPUT_EXP_PATH] --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Calculates the Root Mean Square deviation (RMSd) of a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **input_exp_path** (*str*): Path to the experimental reference file (required if reference = experimental).
* **output_cpptraj_path** (*str*): Path to the output processed analysis.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
    * **reference** (*string*) - ("first") Reference definition. Values: first, average, experimental.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

rms.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
    reference: first
```

Command:


```python
cpptraj_rms --config data/conf/rms.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rms.dat
```

### JSON file config

rms.json:


```python
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
```

Command:


```python
cpptraj_rms --config data/conf/rms.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rms.dat
```

## Cpptraj rmsf

Calculates the Root Mean Square fluctuations (RMSf) of a given cpptraj compatible trajectory.

### Get help

Command:


```python
cpptraj_rmsf -h
```


```python
usage: cpptraj_rmsf [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH [--input_exp_path INPUT_EXP_PATH] --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Calculates the Root Mean Square fluctuations (RMSf) of a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **input_exp_path** (*str*): Path to the experimental reference file (required if reference = experimental).
* **output_cpptraj_path** (*str*): Path to the output processed analysis.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
    * **reference** (*string*) - ("first") Reference definition. Values: first, average, experimental.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

rmsf.yml:


```python
properties:
  in_parameters:
    start: 1
    end: -1
    step: 1
    mask: c-alpha
    reference: first
```

Command:


```python
cpptraj_rmsf --config data/conf/rmsf.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rmsf.dat
```

### JSON file config

rmsf.json:


```python
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
```

Command:


```python
cpptraj_rmsf --config data/conf/rmsf.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.rmsf.dat
```

## Cpptraj slice

Extracts a particular trajectory slice from a given cpptraj compatible trajectory.

### Get help

Command:


```python
cpptraj_slice -h
```


```python
usage: cpptraj_slice [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Extracts a particular trajectory slice from a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed trajectory.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **out_parameters** (*dict*) - (None) Parameters for output trajectory.
    * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

slice.yml:


```python
properties:
  in_parameters:
    start: 2
    end: 20
    step: 2
    mask: c-alpha
  out_parameters:
    format: netcdf
```

Command:


```python
cpptraj_slice --config data/conf/slice.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.slice.netcdf
```

### JSON file config

slice.json:


```python
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
```

Command:


```python
cpptraj_slice --config data/conf/slice.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.slice.netcdf
```

## Cpptraj snapshot

Extracts a particular snapshot from a given cpptraj compatible trajectory.

### Get help

Command:


```python
cpptraj_snapshot -h
```


```python
usage: cpptraj_snapshot [-h] --config CONFIG [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Extracts a particular snapshot from a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed structure.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **snapshot** (*int*) - (1) Frame to be captured for snapshot
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **out_parameters** (*dict*) - (None) Parameters for output trajectory.
    * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

snapshot.yml:


```python
properties:
  in_parameters:
    snapshot: 12
    mask: c-alpha
  out_parameters:
    format: pdb
```

Command:


```python
cpptraj_snapshot --config data/conf/snapshot.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.snapshot.pdb
```

### JSON file config

snapshot.json:


```python
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
```

Command:


```python
cpptraj_snapshot --config data/conf/slice.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.slice.netcdf
```

## Cpptraj strip

Strips a defined set of atoms (mask) from a given cpptraj compatible trajectory.

### Get help

Command:


```python
cpptraj_strip -h
```


```python
usage: cpptraj_strip [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH

Strips a defined set of atoms (mask) from a given cpptraj compatible trajectory.

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
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_top_path** (*str*): Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
* **input_traj_path** (*str*): Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **output_cpptraj_path** (*str*): Path to the output processed trajectory.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **in_parameters** (*dict*) - (None) Parameters for input trajectory. Accepted parameters:
    * **start** (*int*) - (1) Starting frame for slicing
    * **end** (*int*) - (-1) Ending frame for slicing
    * **step** (*int*) - (1) Step for slicing
    * **mask** (*string*) - ("all-atoms") Mask definition. Values: c-alpha, backbone, all-atoms, heavy-atoms, side-chain, solute, ions, solvent.
* **out_parameters** (*dict*) - (None) Parameters for output trajectory.
    * **format** (*str*) - ("netcdf") Output trajectory format. Values: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
* **cpptraj_path** (*str*) - ("cpptraj") Path to the cpptraj executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

strip.yml:


```python
properties:
  in_parameters:
    start: 2
    end: 20
    step: 2
    mask: c-alpha
  out_parameters:
    format: netcdf
```

Command:


```python
cpptraj_strip --config data/conf/strip.yml --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.strip.netcdf
```

### JSON file config

strip.json:


```python
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
```

Command:


```python
cpptraj_strip --config data/conf/strip.json --input_top_path data/input/cpptraj.parm.top --input_traj_path data/input/cpptraj.traj.dcd --output_cpptraj_path data/output/output.strip.netcdf
```

## GROMACS cluster

Creates cluster structures from a given GROMACS compatible trajectory.

### Get help

Command:


```python
gmx_cluster -h
```


```python
usage: gmx_cluster [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_structure_path INPUT_STRUCTURE_PATH --input_traj_path INPUT_TRAJ_PATH [--input_index_path INPUT_INDEX_PATH] --output_pdb_path OUTPUT_PDB_PATH

Creates cluster structures from a given GROMACS compatible trajectory.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --input_index_path INPUT_INDEX_PATH
                        Path to the GROMACS index file. Accepted formats: ndx.

required arguments:
  --input_structure_path INPUT_STRUCTURE_PATH
                        Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
  --input_traj_path INPUT_TRAJ_PATH
                        Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
  --output_pdb_path OUTPUT_PDB_PATH
                        Path to the output cluster file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_structure_path** (*str*): Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
* **input_traj_path** (*str*): Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
* **input_index_path** (*str*): Path to the GROMACS index file. Accepted formats: ndx.
* **output_pdb_path** (*str*): Path to the output cluster file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **fit_selection** (*str*) - ("System") - Group where the fitting will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **output_selection** (*str*) - ("System") Group that is going to be written in the output trajectory. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **dista** (*bool*) - (False) Use RMSD of distances instead of RMS deviation.
* **method** (*str*) - ("linkage") Method for cluster determination. Values: linkage, jarvis-patrick, monte-carlo, diagonalization, gromos
* **cutoff** (*float*) - (0.1) RMSD cut-off (nm) for two structures to be neighbor
* **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('gromacs/gromacs:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

cluster.yml:


```python
properties:
  fit_selection: System
  output_selection: System
  dista: False
  method: linkage
  cutoff: 0.1
```

Command:


```python
gmx_cluster --config data/conf/cluster.yml --input_structure_path data/input/cluster.gro --input_traj_path data/input/cluster.trr --output_pdb_path data/output/output.cluster.pdb
```

### JSON file config

cluster.json:


```python
{
  "properties": {
    "fit_selection": "System",
    "output_selection": "System",
    "dista": false,
    "method": "linkage",
    "cutoff": 0.1
  }
}
```

Command:


```python
gmx_cluster --config data/conf/cluster.json --input_structure_path data/input/cluster.gro --input_traj_path data/input/cluster.trr --output_pdb_path data/output/output.cluster.pdb
```

## GROMACS energy

Extracts energy components from a given GROMACS energy file.

### Get help

Command:


```python
gmx_energy -h
```


```python
usage: gmx_energy [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_energy_path INPUT_ENERGY_PATH --output_xvg_path OUTPUT_XVG_PATH

Extracts energy components from a given GROMACS energy file.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help

required arguments:
  --input_energy_path INPUT_ENERGY_PATH
                        Path to the input EDR file. Accepted formats: edr.
  --output_xvg_path OUTPUT_XVG_PATH
                        Path to the XVG output file. Accepted formats: xvg.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_energy_path** (*str*): Path to the input EDR file. Accepted formats: edr.
* **output_xvg_path** (*str*): Path to the XVG output file. Accepted formats: xvg.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **xvg** (*str*) - ("none") XVG plot formatting. Values: xmgrace, xmgr, none.
* **terms** (*list*) - (["Potential"]) Energy terms. Select one or more from values: Angle, Proper-Dih., Improper-Dih., LJ-14, Coulomb-14, LJ-(SR), Coulomb-(SR), Coul.-recip., Position-Rest., Potential, Kinetic-En., Total-Energy, Temperature, Pressure,  Constr.-rmsd, Box-X, Box-Y,  Box-Z, Volume, Density, pV, Enthalpy, Vir-XX, Vir-XY, Vir-XZ, Vir-YX, Vir-YY, Vir-YZ, Vir-ZX, Vir-ZY, Vir-ZZ, Pres-XX, Pres-XY, Pres-XZ, Pres-YX, Pres-YY,  Pres-YZ, Pres-ZX, Pres-ZY, Pres-ZZ, #Surf*SurfTen, Box-Vel-XX, Box-Vel-YY, Box-Vel-ZZ, Mu-X, Mu-Y, Mu-Z, T-Protein, T-non-Protein, Lamb-Protein, Lamb-non-Protein
* **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('gromacs/gromacs:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

energy.yml:


```python
properties:
  terms: [Potential, Pressure]
```

Command:


```python
gmx_energy --config data/conf/energy.yml --input_energy_path data/input/energy.edr --output_xvg_path data/output/output.energy.xvg
```

### JSON file config

energy.json:


```python
{
  "properties": {
    "terms": ["Potential", "Pressure"]
  }
}
```

Command:


```python
gmx_energy --config data/conf/energy.json --input_energy_path data/input/energy.edr --output_xvg_path data/output/output.energy.xvg
```

## GROMACS image

Corrects periodicity (image) from a given GROMACS compatible trajectory file.

### Get help

Command:


```python
gmx_image -h
```


```python
usage: gmx_image [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_traj_path INPUT_TRAJ_PATH --input_top_path INPUT_TOP_PATH [--input_index_path INPUT_INDEX_PATH] --output_traj_path OUTPUT_TRAJ_PATH

Corrects periodicity (image) from a given GROMACS compatible trajectory file.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --input_index_path INPUT_INDEX_PATH
                        Path to the GROMACS index file. Accepted formats: ndx.

required arguments:
  --input_traj_path INPUT_TRAJ_PATH
                        Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
  --input_top_path INPUT_TOP_PATH
                        Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
  --output_traj_path OUTPUT_TRAJ_PATH
                        Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_traj_path** (*str*): Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
* **input_top_path** (*str*): Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
* **input_index_path** (*str*): Path to the GROMACS index file. Accepted formats: ndx.
* **output_traj_path** (*str*): Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **fit_selection** (*str*) - ("System") - Group where the fitting will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **center_selection** (*str*) - ("System") Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **output_selection** (*str*) - ("System") Group that is going to be written in the output trajectory. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **pbc** (*str*) - ("mol") PBC treatment (see help text for full description). Values: none, mol, res, atom, nojump, cluster, whole.
* **center** (*bool*) - (True) Center atoms in box.
* **ur** (*str*) - ("compact") Unit-cell representation. Values: rect, tric, compact.
* **fit** (*str*) - ("none") Fit molecule to ref structure in the structure file. Values: none, rot+trans, rotxy+transxy, translation, transxy, progressive.
* **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('gromacs/gromacs:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

gmx_image.yml:


```python
properties:
  fit_selection: System
  center_selection: System
  output_selection: System
  pbc: mol
  center: True
  fit: rot+trans
  ur: compact
```

Command:


```python
gmx_image --config data/conf/gmx_image.yml --input_traj_path data/input/image.trr --input_top_path data/input/image.gro --output_traj_path data/output/output.image.xtc
```

### JSON file config

gmx_image.json:


```python
{
  "properties": {
    "fit_selection": "System",
    "center_selection": "System",
    "output_selection": "System",
    "pbc": "mol",
    "center": true,
    "fit": "rot+trans",
    "ur": "compact"
  }
}
```

Command:


```python
gmx_image --config data/conf/gmx_image.json --input_traj_path data/input/image.trr --input_top_path data/input/image.gro --output_traj_path data/output/output.image.xtc
```

## GROMACS rgyr

Computes the radius of gyration (Rgyr) of a molecule about the x-, y- and z-axes, as a function of time, from a given GROMACS compatible trajectory.

### Get help

Command:


```python
gmx_rgyr -h
```


```python
usage: gmx_rgyr [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_structure_path INPUT_STRUCTURE_PATH --input_traj_path INPUT_TRAJ_PATH [--input_index_path INPUT_INDEX_PATH] --output_xvg_path OUTPUT_XVG_PATH

Computes the radius of gyration (Rgyr) of a molecule about the x-, y- and z-axes, as a function of time, from a given GROMACS compatible trajectory.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --input_index_path INPUT_INDEX_PATH
                        Path to the GROMACS index file. Accepted formats: ndx.

required arguments:
  --input_structure_path INPUT_STRUCTURE_PATH
                        Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
  --input_traj_path INPUT_TRAJ_PATH
                        Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
  --output_xvg_path OUTPUT_XVG_PATH
                        Path to the XVG output file. Accepted formats: xvg.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_structure_path** (*str*): Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
* **input_traj_path** (*str*): Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
* **input_index_path** (*str*): Path to the GROMACS index file. Accepted formats: ndx.
* **output_xvg_path** (*str*): Path to the XVG output file. Accepted formats: xvg.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **xvg** (*str*) - ("none") XVG plot formatting. Values: xmgrace, xmgr, none.
* **selection** (*str*) - ("System") Group where the rgyr will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('gromacs/gromacs:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

gmx_rgyr.yml:


```python
properties:
  selection: System
```

Command:


```python
gmx_rgyr --config data/conf/gmx_rgyr.yml --input_structure_path data/input/rgyr.gro --input_traj_path data/input/rgyr.trr --output_xvg_path data/output/output.rgyr.xvg
```

### JSON file config

gmx_rgyr.json:


```python
{
  "properties": {
    "selection": "System"
  }
}
```

Command:


```python
gmx_rgyr --config data/conf/gmx_rgyr.json --input_structure_path data/input/rgyr.gro --input_traj_path data/input/rgyr.trr --output_xvg_path data/output/output.rgyr.xvg
```

## GROMACS rms

Performs a Root Mean Square deviation (RMSd) analysis from a given GROMACS compatible trajectory.

### Get help

Command:


```python
gmx_rms -h
```


```python
usage: gmx_rms [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_structure_path INPUT_STRUCTURE_PATH --input_traj_path INPUT_TRAJ_PATH [--input_index_path INPUT_INDEX_PATH] --output_xvg_path OUTPUT_XVG_PATH

Performs a Root Mean Square deviation (RMSd) analysis from a given GROMACS compatible trajectory.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --input_index_path INPUT_INDEX_PATH
                        Path to the GROMACS index file. Accepted formats: ndx.

required arguments:
  --input_structure_path INPUT_STRUCTURE_PATH
                        Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
  --input_traj_path INPUT_TRAJ_PATH
                        Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
  --output_xvg_path OUTPUT_XVG_PATH
                        Path to the XVG output file. Accepted formats: xvg.

```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_structure_path** (*str*): Path to the input structure file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
* **input_traj_path** (*str*): Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
* **input_index_path** (*str*): Path to the GROMACS index file. Accepted formats: ndx.
* **output_xvg_path** (*str*): Path to the XVG output file. Accepted formats: xvg.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **xvg** (*str*) - ("none") XVG plot formatting. Values: xmgrace, xmgr, none.
* **selection** (*str*) - ("System") Group where the rms will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('gromacs/gromacs:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

gmx_rms.yml:


```python
properties:
  selection: System
```

Command:


```python
gmx_rms --config data/conf/gmx_rms.yml --input_structure_path data/input/rgyr.gro --input_traj_path data/input/rgyr.trr --output_xvg_path data/output/output.rms.xvg
```

### JSON file config

gmx_rgyr.json:


```python
{
  "properties": {
    "selection": "System"
  }
}
```

Command:


```python
gmx_rms --config data/conf/gmx_rms.json --input_structure_path data/input/rgyr.gro --input_traj_path data/input/rgyr.trr --output_xvg_path data/output/output.rms.xvg
```

## GROMACS trjconv structure

Converts between GROMACS compatible structure file formats and/or extracts a selection of atoms.

### Get help

Command:


```python
gmx_trjconv_str -h
```


```python
usage: gmx_trjconv_str [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_structure_path INPUT_STRUCTURE_PATH --input_top_path INPUT_TOP_PATH [--input_index_path INPUT_INDEX_PATH] --output_str_path OUTPUT_STR_PATH

Converts between GROMACS compatible structure file formats and/or extracts a selection of atoms.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --input_index_path INPUT_INDEX_PATH
                        Path to the GROMACS index file. Accepted formats: ndx.

required arguments:
  --input_structure_path INPUT_STRUCTURE_PATH
                        Path to the input structure file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
  --input_top_path INPUT_TOP_PATH
                        Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
  --output_str_path OUTPUT_STR_PATH
                        Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_structure_path** (*str*): Path to the input structure file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
* **input_top_path** (*str*): Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
* **input_index_path** (*str*): Path to the GROMACS index file. Accepted formats: ndx.
* **output_str_path** (*str*): Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **selection** (*str*) - ("System") Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('gromacs/gromacs:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

gmx_trjconv_str.yml:


```python
properties:
  selection: System
```

Command:


```python
gmx_trjconv_str --config data/conf/gmx_trjconv_str.yml --input_structure_path data/input/trjconv.str.gro --input_top_path data/input/trjconv.str.gro --output_str_path data/output/output.trjconv.str.pdb
```

### JSON file config

gmx_rgyr.json:


```python
{
  "properties": {
    "selection": "System"
  }
}
```

Command:


```python
gmx_trjconv_str --config data/conf/gmx_trjconv_str.json --input_structure_path data/input/trjconv.str.gro --input_top_path data/input/trjconv.str.gro --output_str_path data/output/output.trjconv.str.pdb
```

## GROMACS trjconv structure ensemble

Extracts an ensemble of frames containing a selection of atoms from GROMACS compatible trajectory files.

### Get help

Command:


```python
gmx_trjconv_str_ens -h
```


```python
usage: gmx_trjconv_str_ens [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_traj_path INPUT_TRAJ_PATH --input_top_path INPUT_TOP_PATH [--input_index_path INPUT_INDEX_PATH] --output_str_ens_path OUTPUT_STR_ENS_PATH

Extracts an ensemble of frames containing a selection of atoms from GROMACS compatible trajectory files.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --input_index_path INPUT_INDEX_PATH
                        Path to the GROMACS index file. Accepted formats: ndx.

required arguments:
  --input_traj_path INPUT_TRAJ_PATH
                        Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
  --input_top_path INPUT_TOP_PATH
                        Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
  --output_str_ens_path OUTPUT_STR_ENS_PATH
                        Path to the output file. Accepted formats: zip.

```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_traj_path** (*str*): Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
* **input_top_path** (*str*): Path to the GROMACS input topology file. Accepted formats: tpr, gro, g96, pdb, brk, ent.
* **input_index_path** (*str*): Path to the GROMACS index file. Accepted formats: ndx.
* **output_str_ens_path** (*str*): Path to the output file. Accepted formats: zip.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **selection** (*str*) - ("System") Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **start** (*int*) - (0) Time of first frame to read from trajectory (default unit ps).
* **end** (*int*) - (0) Time of last frame to read from trajectory (default unit ps).
* **dt** (*int*) - (0) Only write frame when t MOD dt = first time (ps).
* **output_name** (*str*) - ("output") File name for ensemble of output files.
* **output_type** (*str*) - ("pdb") File type for ensemble of output files. Values: gro, g96, pdb.
* **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('gromacs/gromacs:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

gmx_trjconv_str_ens.yml:


```python
properties:
  selection: System
  start: 0
  end: 10
  dt: 1
  output_name: output
  output_type: pdb
```

Command:


```python
gmx_trjconv_str_ens --config data/conf/gmx_trjconv_str_ens.yml --input_traj_path data/input/trjconv.str.ens.trr --input_top_path data/input/trjconv.str.ens.gro --output_str_ens_path data/output/output.trjconv.str.ens.zip
```

### JSON file config

gmx_rgyr.json:


```python
{
  "properties": {
    "selection": "System",
    "start": 0,
    "end": 10,
    "dt": 1,
    "output_name": "output",
    "output_type": "pdb"
  }
}
```

Command:


```python
gmx_trjconv_str_ens --config data/conf/gmx_trjconv_str_ens.json --input_traj_path data/input/trjconv.str.ens.trr --input_top_path data/input/trjconv.str.ens.gro --output_str_ens_path data/output/output.trjconv.str.ens.zip
```

## GROMACS trjconv trajectory

Converts between GROMACS compatible trajectory file formats and/or extracts a selection of atoms.

### Get help

Command:


```python
gmx_trjconv_trj -h
```


```python
usage: gmx_trjconv_trj [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_traj_path INPUT_TRAJ_PATH [--input_index_path INPUT_INDEX_PATH] --output_traj_path OUTPUT_TRAJ_PATH

Converts between GROMACS compatible trajectory file formats and/or extracts a selection of atoms.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --input_index_path INPUT_INDEX_PATH
                        Path to the GROMACS index file. Accepted formats: ndx.

required arguments:
  --input_traj_path INPUT_TRAJ_PATH
                        Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
  --output_traj_path OUTPUT_TRAJ_PATH
                        Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_traj_path** (*str*): Path to the GROMACS trajectory file. Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng.
* **input_index_path** (*str*): Path to the GROMACS index file. Accepted formats: ndx.
* **output_traj_path** (*str*): Path to the output file. Accepted formats: xtc, trr, gro, g96, pdb, tng.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **selection** (*str*) - ("System") Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values, if not, values: System, Protein, Protein-H, C-alpha, Backbone, MainChain, MainChain+Cb, MainChain+H, SideChain, SideChain-H, Prot-Masses, non-Protein, Water, SOL, non-Water, Ion, NA, CL, Water_and_ions.
* **start** (*int*) - (0) Time of first frame to read from trajectory (default unit ps).
* **end** (*int*) - (0) Time of last frame to read from trajectory (default unit ps).
* **dt** (*int*) - (0) Only write frame when t MOD dt = first time (ps).
* **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('gromacs/gromacs:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML file config

gmx_trjconv_trj.yml:


```python
properties:
  selection: System
  start: 0
  end: 0
  dt: 0
```

Command:


```python
gmx_trjconv_trj --config data/conf/gmx_trjconv_trj.yml --input_traj_path data/input/trjconv.trj.trr --output_traj_path data/output/output.trjconv.trj.xtc
```

### JSON file config

gmx_rgyr.json:


```python
{
  "properties": {
    "selection": "System",
    "start": 0,
    "end": 0,
    "dt": 0
  }
}
```

Command:


```python
gmx_trjconv_trj --config data/conf/gmx_trjconv_trj.json --input_traj_path data/input/trjconv.trj.trr --output_traj_path data/output/output.trjconv.trj.xtc
```
