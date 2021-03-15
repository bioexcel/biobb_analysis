# BioBB ANALYSIS Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Cpptraj_slice
Wrapper of the Ambertools Cpptraj module for extracting a particular trajectory slice from a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_slice -h
```
    /bin/sh: cpptraj_slice: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.slice.netcdf). Accepted formats: CRD, NETCDF, RST7, NCRST, DCD, PDB, MOL2, BINPOS, TRR, XTC, SQM
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing..
* **end** (*integer*): (-1) Ending frame for slicing..
* **steps** (*integer*): (1) Step for slicing..
* **mask** (*string*): (all-atoms) Mask definition. .
* **format** (*string*): (netcdf) Output trajectory format. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_slice.yml)
```python
properties:
  end: 20
  format: netcdf
  mask: c-alpha
  start: 2
  steps: 2

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_slice_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  end: 20
  format: netcdf
  mask: c-alpha
  start: 2
  steps: 2

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_slice_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  end: 20
  format: netcdf
  mask: c-alpha
  start: 2
  steps: 2

```
#### Command line
```python
cpptraj_slice --config config_cpptraj_slice.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.slice.netcdf
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_slice.json)
```python
{
  "properties": {
    "start": 2,
    "end": 20,
    "steps": 2,
    "mask": "c-alpha",
    "format": "netcdf"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_slice_docker.json)
```python
{
  "properties": {
    "start": 2,
    "end": 20,
    "steps": 2,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_slice_singularity.json)
```python
{
  "properties": {
    "start": 2,
    "end": 20,
    "steps": 2,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_slice --config config_cpptraj_slice.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.slice.netcdf
```

## Cpptraj_convert
Wrapper of the Ambertools Cpptraj module for converting between cpptraj compatible trajectory file formats and/or extracting a selection of atoms or frames.
### Get help
Command:
```python
cpptraj_convert -h
```
    /bin/sh: cpptraj_convert: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.convert.netcdf). Accepted formats: CRD, NETCDF, RST7, NCRST, DCD, PDB, MOL2, BINPOS, TRR, XTC, SQM
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing.
* **end** (*integer*): (-1) Ending frame for slicing.
* **steps** (*integer*): (1) Step for slicing.
* **mask** (*string*): (all-atoms) Mask definition. .
* **format** (*string*): (netcdf) Output trajectory format. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_convert.yml)
```python
properties:
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_convert_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_convert_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_convert --config config_cpptraj_convert.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.convert.netcdf
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_convert.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_convert_docker.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_convert_singularity.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_convert --config config_cpptraj_convert.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.convert.netcdf
```

## Cpptraj_dry
Wrapper of the Ambertools Cpptraj module for dehydrating a given cpptraj compatible trajectory stripping out solvent molecules and ions.
### Get help
Command:
```python
cpptraj_dry -h
```
    /bin/sh: cpptraj_dry: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.dry.netcdf). Accepted formats: CRD, NETCDF, RST7, NCRST, DCD, PDB, MOL2, BINPOS, TRR, XTC, SQM
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing..
* **end** (*integer*): (-1) Ending frame for slicing..
* **steps** (*integer*): (1) Step for slicing..
* **mask** (*string*): (all-atoms) Mask definition. .
* **format** (*string*): (netcdf) Output trajectory format. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_dry.yml)
```python
properties:
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_dry_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_dry_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_dry --config config_cpptraj_dry.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.dry.netcdf
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_dry.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_dry_docker.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_dry_singularity.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_dry --config config_cpptraj_dry.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.dry.netcdf
```

## Cpptraj_rmsf
Wrapper of the Ambertools Cpptraj module for calculating the Root Mean Square fluctuations (RMSf) of a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_rmsf -h
```
    /bin/sh: cpptraj_rmsf: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **input_exp_path** (*string*): Path to the experimental reference file (required if reference = experimental). File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/experimental.1e5t.pdb). Accepted formats: PDB
* **output_cpptraj_path** (*string*): Path to the output processed analysis. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.rmsf.first.dat). Accepted formats: DAT, AGR, XMGR, GNU
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing.
* **end** (*integer*): (-1) Ending frame for slicing.
* **steps** (*integer*): (1) Step for slicing.
* **mask** (*string*): (all-atoms) Mask definition. .
* **reference** (*string*): (first) Reference definition. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rmsf.yml)
```python
properties:
  end: -1
  mask: c-alpha
  reference: first
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_rmsf --config config_cpptraj_rmsf.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --input_exp_path experimental.1e5t.pdb --output_cpptraj_path ref_cpptraj.rmsf.first.dat
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rmsf.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "reference": "first"
  }
}
```
#### Command line
```python
cpptraj_rmsf --config config_cpptraj_rmsf.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --input_exp_path experimental.1e5t.pdb --output_cpptraj_path ref_cpptraj.rmsf.first.dat
```

## Gmx_trjconv_trj
Wrapper of the GROMACS trjconv module for converting between GROMACS compatible trajectory file formats and/or extracts a selection of atoms.
### Get help
Command:
```python
gmx_trjconv_trj -h
```
    /bin/sh: gmx_trjconv_trj: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_traj_path** (*string*): Path to the GROMACS trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_index_path** (*string*): Path to the GROMACS index file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx). Accepted formats: NDX
* **output_traj_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_trjconv.trj.xtc). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **selection** (*string*): (System) Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values. .
* **start** (*integer*): (0) Time of first frame to read from trajectory (default unit ps)..
* **end** (*integer*): (0) Time of last frame to read from trajectory (default unit ps)..
* **dt** (*integer*): (0) Only write frame when t MOD dt = first time (ps)..
* **gmx_path** (*string*): (gmx) Path to the GROMACS executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (gromacs/gromacs:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_trj.yml)
```python
properties:
  dt: 0
  end: 0
  selection: System
  start: 0

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_trj_docker.yml)
```python
properties:
  container_image: gromacs/gromacs:latest
  container_path: docker
  container_volume_path: /tmp
  dt: 0
  end: 0
  selection: System
  start: 0

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_trj_singularity.yml)
```python
properties:
  container_image: shub://michael-tn/gromacs
  container_path: singularity
  container_volume_path: /tmp
  dt: 0
  end: 0
  selection: System
  start: 0

```
#### Command line
```python
gmx_trjconv_trj --config config_gmx_trjconv_trj.yml --input_traj_path trajectory.trr --input_index_path index.ndx --output_traj_path ref_trjconv.trj.xtc
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_trj.json)
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
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_trj_docker.json)
```python
{
  "properties": {
    "selection": "System",
    "start": 0,
    "end": 0,
    "dt": 0,
    "container_path": "docker",
    "container_image": "gromacs/gromacs:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_trj_singularity.json)
```python
{
  "properties": {
    "selection": "System",
    "start": 0,
    "end": 0,
    "dt": 0,
    "container_path": "singularity",
    "container_image": "shub://michael-tn/gromacs",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
gmx_trjconv_trj --config config_gmx_trjconv_trj.json --input_traj_path trajectory.trr --input_index_path index.ndx --output_traj_path ref_trjconv.trj.xtc
```

## Cpptraj_mask
Wrapper of the Ambertools Cpptraj module for extracting a selection of atoms from a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_mask -h
```
    /bin/sh: cpptraj_mask: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.mask.netcdf). Accepted formats: CRD, NETCDF, RST7, NCRST, DCD, PDB, MOL2, BINPOS, TRR, XTC, SQM
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing..
* **end** (*integer*): (-1) Ending frame for slicing..
* **steps** (*integer*): (1) Step for slicing..
* **mask** (*string*): (all-atoms) Mask definition. .
* **format** (*string*): (netcdf) Output trajectory format. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_mask.yml)
```python
properties:
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_mask_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_mask_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_mask --config config_cpptraj_mask.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.mask.netcdf
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_mask.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_mask_docker.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_mask_singularity.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_mask --config config_cpptraj_mask.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.mask.netcdf
```

## Cpptraj_rms
Wrapper of the Ambertools Cpptraj module for calculating the Root Mean Square deviation (RMSd) of a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_rms -h
```
    /bin/sh: cpptraj_rms: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **input_exp_path** (*string*): Path to the experimental reference file (required if reference = experimental). File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/experimental.1e5t.pdb). Accepted formats: PDB
* **output_cpptraj_path** (*string*): Path to the output processed analysis. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.rms.first.dat). Accepted formats: DAT, AGR, XMGR, GNU
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing.
* **end** (*integer*): (-1) Ending frame for slicing.
* **steps** (*integer*): (1) Step for slicing.
* **mask** (*string*): (all-atoms) Mask definition. .
* **reference** (*string*): (first) Reference definition. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rms.yml)
```python
properties:
  end: -1
  mask: c-alpha
  reference: first
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_rms --config config_cpptraj_rms.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --input_exp_path experimental.1e5t.pdb --output_cpptraj_path ref_cpptraj.rms.first.dat
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rms.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "reference": "first"
  }
}
```
#### Command line
```python
cpptraj_rms --config config_cpptraj_rms.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --input_exp_path experimental.1e5t.pdb --output_cpptraj_path ref_cpptraj.rms.first.dat
```

## Cpptraj_bfactor
Wrapper of the Ambertools Cpptraj module for calculating the Bfactor fluctuations of a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_bfactor -h
```
    /bin/sh: cpptraj_bfactor: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **input_exp_path** (*string*): Path to the experimental reference file (required if reference = experimental). File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/experimental.1e5t.pdb). Accepted formats: PDB
* **output_cpptraj_path** (*string*): Path to the output processed analysis. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.bfactor.first.dat). Accepted formats: DAT, AGR, XMGR, GNU
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing.
* **end** (*integer*): (-1) Ending frame for slicing.
* **steps** (*integer*): (1) Step for slicing.
* **mask** (*string*): (all-atoms) Mask definition. .
* **reference** (*string*): (first) Reference definition. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_bfactor.yml)
```python
properties:
  end: -1
  mask: c-alpha
  reference: first
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_bfactor --config config_cpptraj_bfactor.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --input_exp_path experimental.1e5t.pdb --output_cpptraj_path ref_cpptraj.bfactor.first.dat
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_bfactor.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "reference": "first"
  }
}
```
#### Command line
```python
cpptraj_bfactor --config config_cpptraj_bfactor.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --input_exp_path experimental.1e5t.pdb --output_cpptraj_path ref_cpptraj.bfactor.first.dat
```

## Gmx_image
Wrapper of the GROMACS trjconv module for correcting periodicity (image) from a given GROMACS compatible trajectory file.
### Get help
Command:
```python
gmx_image -h
```
    /bin/sh: gmx_image: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_traj_path** (*string*): Path to the GROMACS trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_top_path** (*string*): Path to the GROMACS input topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr). Accepted formats: TPR, GRO, G96, PDB, BRK, ENT
* **input_index_path** (*string*): Path to the GROMACS index file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx). Accepted formats: NDX
* **output_traj_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_image.xtc). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **fit_selection** (*string*): (System) Group where the fitting will be performed. If **input_index_path** provided, check the file for the accepted values. .
* **center_selection** (*string*): (System) Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values. .
* **output_selection** (*string*): (System) Group that is going to be written in the output trajectory. If **input_index_path** provided, check the file for the accepted values. .
* **pbc** (*string*): (mol) PBC treatment (see help text for full description) . .
* **center** (*boolean*): (True) Center atoms in box..
* **ur** (*string*): (compact) Unit-cell representation. .
* **fit** (*string*): (none) Fit molecule to ref structure in the structure file. .
* **gmx_path** (*string*): (gmx) Path to the GROMACS executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (gromacs/gromacs:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_image.yml)
```python
properties:
  center: true
  center_selection: System
  fit: rot+trans
  fit_selection: System
  output_selection: System
  pbc: mol
  ur: compact

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_image_docker.yml)
```python
properties:
  center: true
  center_selection: System
  container_image: gromacs/gromacs:latest
  container_path: docker
  container_volume_path: /tmp
  fit: rot+trans
  fit_selection: System
  output_selection: System
  pbc: mol
  ur: compact

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_image_singularity.yml)
```python
properties:
  center: true
  center_selection: System
  container_image: shub://michael-tn/gromacs
  container_path: singularity
  container_volume_path: /tmp
  fit: rot+trans
  fit_selection: System
  output_selection: System
  pbc: mol
  ur: compact

```
#### Command line
```python
gmx_image --config config_gmx_image.yml --input_traj_path trajectory.trr --input_top_path topology.tpr --input_index_path index.ndx --output_traj_path ref_image.xtc
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_image.json)
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
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_image_docker.json)
```python
{
  "properties": {
    "fit_selection": "System",
    "center_selection": "System",
    "output_selection": "System",
    "pbc": "mol",
    "center": true,
    "fit": "rot+trans",
    "ur": "compact",
    "container_path": "docker",
    "container_image": "gromacs/gromacs:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_image_singularity.json)
```python
{
  "properties": {
    "fit_selection": "System",
    "center_selection": "System",
    "output_selection": "System",
    "pbc": "mol",
    "center": true,
    "fit": "rot+trans",
    "ur": "compact",
    "container_path": "singularity",
    "container_image": "shub://michael-tn/gromacs",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
gmx_image --config config_gmx_image.json --input_traj_path trajectory.trr --input_top_path topology.tpr --input_index_path index.ndx --output_traj_path ref_image.xtc
```

## Cpptraj_image
Wrapper of the Ambertools Cpptraj module for correcting periodicity (image) from a given cpptraj trajectory file.
### Get help
Command:
```python
cpptraj_image -h
```
    /bin/sh: cpptraj_image: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.image.netcdf). Accepted formats: CRD, NETCDF, RST7, NCRST, DCD, PDB, MOL2, BINPOS, TRR, XTC, SQM
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing..
* **end** (*integer*): (-1) Ending frame for slicing..
* **steps** (*integer*): (1) Step for slicing..
* **mask** (*string*): (all-atoms) Mask definition. .
* **format** (*string*): (netcdf) Output trajectory format. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_image.yml)
```python
properties:
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_image_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_image_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_image --config config_cpptraj_image.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.image.netcdf
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_image.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_image_docker.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_image_singularity.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_image --config config_cpptraj_image.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.image.netcdf
```

## Gmx_rms
Wrapper of the GROMACS rms module for performing a Root Mean Square deviation (RMSd) analysis from a given GROMACS compatible trajectory.
### Get help
Command:
```python
gmx_rms -h
```
    /bin/sh: gmx_rms: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_structure_path** (*string*): Path to the input structure file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr). Accepted formats: TPR, GRO, G96, PDB, BRK, ENT
* **input_traj_path** (*string*): Path to the GROMACS trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_index_path** (*string*): Path to the GROMACS index file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx). Accepted formats: NDX
* **output_xvg_path** (*string*): Path to the XVG output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_rms.xvg). Accepted formats: XVG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **xvg** (*string*): (none) XVG plot formatting. .
* **selection** (*string*): (System) Group where the rms will be performed. If **input_index_path** provided, check the file for the accepted values. .
* **gmx_path** (*string*): (gmx) Path to the GROMACS executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (gromacs/gromacs:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rms.yml)
```python
properties:
  selection: System

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rms_docker.yml)
```python
properties:
  container_image: gromacs/gromacs:latest
  container_path: docker
  container_volume_path: /tmp
  selection: System

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rms_singularity.yml)
```python
properties:
  container_image: shub://michael-tn/gromacs
  container_path: singularity
  container_volume_path: /tmp
  selection: System

```
#### Command line
```python
gmx_rms --config config_gmx_rms.yml --input_structure_path topology.tpr --input_traj_path trajectory.trr --input_index_path index.ndx --output_xvg_path ref_rms.xvg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rms.json)
```python
{
  "properties": {
    "selection": "System"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rms_docker.json)
```python
{
  "properties": {
    "selection": "System",
    "container_path": "docker",
    "container_image": "gromacs/gromacs:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rms_singularity.json)
```python
{
  "properties": {
    "selection": "System",
    "container_path": "singularity",
    "container_image": "shub://michael-tn/gromacs",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
gmx_rms --config config_gmx_rms.json --input_structure_path topology.tpr --input_traj_path trajectory.trr --input_index_path index.ndx --output_xvg_path ref_rms.xvg
```

## Gmx_cluster
Wrapper of the GROMACS cluster module for clustering structures from a given GROMACS compatible trajectory.
### Get help
Command:
```python
gmx_cluster -h
```
    /bin/sh: gmx_cluster: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_structure_path** (*string*): Path to the input structure file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr). Accepted formats: TPR, GRO, G96, PDB, BRK, ENT
* **input_traj_path** (*string*): Path to the GROMACS trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_index_path** (*string*): Path to the GROMACS index file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx). Accepted formats: NDX
* **output_pdb_path** (*string*): Path to the output cluster file. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_cluster.pdb). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **fit_selection** (*string*): (System) Group where the fitting will be performed. If **input_index_path** provided, check the file for the accepted values. .
* **output_selection** (*string*): (System) Group that is going to be written in the output trajectory. If **input_index_path** provided, check the file for the accepted values. .
* **dista** (*boolean*): (False) Use RMSD of distances instead of RMS deviation..
* **method** (*string*): (linkage) Method for cluster determination. .
* **cutoff** (*number*): (0.1) RMSD cut-off (nm) for two structures to be neighbor..
* **gmx_path** (*string*): (gmx) Path to the GROMACS executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (gromacs/gromacs:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_cluster.yml)
```python
properties:
  cutoff: 0.1
  dista: false
  fit_selection: System
  method: linkage
  output_selection: System

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_cluster_docker.yml)
```python
properties:
  container_image: gromacs/gromacs:latest
  container_path: docker
  container_volume_path: /tmp
  cutoff: 0.1
  dista: false
  fit_selection: System
  method: linkage
  output_selection: System

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_cluster_singularity.yml)
```python
properties:
  container_image: shub://michael-tn/gromacs
  container_path: singularity
  container_volume_path: /tmp
  cutoff: 0.1
  dista: false
  fit_selection: System
  method: linkage
  output_selection: System

```
#### Command line
```python
gmx_cluster --config config_gmx_cluster.yml --input_structure_path topology.tpr --input_traj_path trajectory.trr --input_index_path index.ndx --output_pdb_path ref_cluster.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_cluster.json)
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
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_cluster_docker.json)
```python
{
  "properties": {
    "fit_selection": "System",
    "output_selection": "System",
    "dista": false,
    "method": "linkage",
    "cutoff": 0.1,
    "container_path": "docker",
    "container_image": "gromacs/gromacs:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_cluster_singularity.json)
```python
{
  "properties": {
    "fit_selection": "System",
    "output_selection": "System",
    "dista": false,
    "method": "linkage",
    "cutoff": 0.1,
    "container_path": "singularity",
    "container_image": "shub://michael-tn/gromacs",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
gmx_cluster --config config_gmx_cluster.json --input_structure_path topology.tpr --input_traj_path trajectory.trr --input_index_path index.ndx --output_pdb_path ref_cluster.pdb
```

## Cpptraj_rgyr
Wrapper of the Ambertools Cpptraj module for computing the radius of gyration (Rgyr) from a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_rgyr -h
```
    /bin/sh: cpptraj_rgyr: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output analysis. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.rgyr.dat). Accepted formats: DAT, AGR, XMGR, GNU
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing..
* **end** (*integer*): (-1) Ending frame for slicing..
* **steps** (*integer*): (1) Step for slicing..
* **mask** (*string*): (all-atoms) Mask definition. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rgyr.yml)
```python
properties:
  end: -1
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rgyr_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  end: -1
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rgyr_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  end: -1
  mask: c-alpha
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_rgyr --config config_cpptraj_rgyr.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.rgyr.dat
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rgyr.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rgyr_docker.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_rgyr_singularity.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_rgyr --config config_cpptraj_rgyr.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.rgyr.dat
```

## Cpptraj_strip
Wrapper of the Ambertools Cpptraj module for stripping a defined set of atoms (mask) from a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_strip -h
```
    /bin/sh: cpptraj_strip: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.strip.netcdf). Accepted formats: CRD, NETCDF, RST7, NCRST, DCD, PDB, MOL2, BINPOS, TRR, XTC, SQM
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing..
* **end** (*integer*): (-1) Ending frame for slicing..
* **steps** (*integer*): (1) Step for slicing..
* **mask** (*string*): (all-atoms) Mask definition. .
* **format** (*string*): (netcdf) Output trajectory format. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_strip.yml)
```python
properties:
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_strip_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_strip_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  end: -1
  format: netcdf
  mask: c-alpha
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_strip --config config_cpptraj_strip.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.strip.netcdf
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_strip.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_strip_docker.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_strip_singularity.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "netcdf",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_strip --config config_cpptraj_strip.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.strip.netcdf
```

## Cpptraj_snapshot
Wrapper of the Ambertools Cpptraj module for extracting a particular snapshot from a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_snapshot -h
```
    /bin/sh: cpptraj_snapshot: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed structure. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.snapshot.pdb). Accepted formats: CRD, NETCDF, RST7, NCRST, DCD, PDB, MOL2, BINPOS, TRR, XTC, SQM
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **snapshot** (*integer*): (1) Frame to be captured for snapshot.
* **mask** (*string*): (all-atoms) Mask definition. .
* **format** (*string*): (netcdf) Output trajectory format. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_snapshot.yml)
```python
properties:
  format: pdb
  mask: c-alpha
  snapshot: 12

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_snapshot_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  format: pdb
  mask: c-alpha
  snapshot: 12

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_snapshot_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  format: pdb
  mask: c-alpha
  snapshot: 12

```
#### Command line
```python
cpptraj_snapshot --config config_cpptraj_snapshot.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.snapshot.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_snapshot.json)
```python
{
  "properties": {
    "snapshot": 12,
    "mask": "c-alpha",
    "format": "pdb"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_snapshot_docker.json)
```python
{
  "properties": {
    "snapshot": 12,
    "mask": "c-alpha",
    "format": "pdb",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_snapshot_singularity.json)
```python
{
  "properties": {
    "snapshot": 12,
    "mask": "c-alpha",
    "format": "pdb",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_snapshot --config config_cpptraj_snapshot.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.snapshot.pdb
```

## Gmx_energy
Wrapper of the GROMACS energy module for extracting energy components from a given GROMACS energy file.
### Get help
Command:
```python
gmx_energy -h
```
    /bin/sh: gmx_energy: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_energy_path** (*string*): Path to the input EDR file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/energy.edr). Accepted formats: EDR
* **output_xvg_path** (*string*): Path to the XVG output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_energy.xvg). Accepted formats: XVG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **xvg** (*string*): (none) XVG plot formatting. .
* **terms** (*array*): ([Potential]) Energy terms. .
* **gmx_path** (*string*): (gmx) Path to the GROMACS executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (gromacs/gromacs:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_energy.yml)
```python
properties:
  terms:
  - Potential
  - Pressure

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_energy_docker.yml)
```python
properties:
  container_image: gromacs/gromacs:latest
  container_path: docker
  container_volume_path: /tmp
  terms:
  - Potential
  - Pressure

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_energy_singularity.yml)
```python
properties:
  container_image: shub://michael-tn/gromacs
  container_path: singularity
  container_volume_path: /tmp
  terms:
  - Potential
  - Pressure

```
#### Command line
```python
gmx_energy --config config_gmx_energy.yml --input_energy_path energy.edr --output_xvg_path ref_energy.xvg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_energy.json)
```python
{
  "properties": {
    "terms": [
      "Potential",
      "Pressure"
    ]
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_energy_docker.json)
```python
{
  "properties": {
    "terms": [
      "Potential",
      "Pressure"
    ],
    "container_path": "docker",
    "container_image": "gromacs/gromacs:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_energy_singularity.json)
```python
{
  "properties": {
    "terms": [
      "Potential",
      "Pressure"
    ],
    "container_path": "singularity",
    "container_image": "shub://michael-tn/gromacs",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
gmx_energy --config config_gmx_energy.json --input_energy_path energy.edr --output_xvg_path ref_energy.xvg
```

## Gmx_trjconv_str_ens
Wrapper of the GROMACS trjconv module for extracting an ensemble of frames containing a selection of atoms from GROMACS compatible trajectory files.
### Get help
Command:
```python
gmx_trjconv_str_ens -h
```
    /bin/sh: gmx_trjconv_str_ens: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_traj_path** (*string*): Path to the GROMACS trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_top_path** (*string*): Path to the GROMACS input topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr). Accepted formats: TPR, GRO, G96, PDB, BRK, ENT
* **input_index_path** (*string*): Path to the GROMACS index file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx). Accepted formats: NDX
* **output_str_ens_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_trjconv.str.ens.zip). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **selection** (*string*): (System) Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values. .
* **skip** (*integer*): (1) Only write every nr-th frame..
* **start** (*integer*): (0) Time of first frame to read from trajectory (default unit ps)..
* **end** (*integer*): (0) Time of last frame to read from trajectory (default unit ps)..
* **dt** (*integer*): (0) Only write frame when t MOD dt = first time (ps)..
* **output_name** (*string*): (output) File name for ensemble of output files..
* **output_type** (*string*): (pdb) File type for ensemble of output files. .
* **gmx_path** (*string*): (gmx) Path to the GROMACS executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (gromacs/gromacs:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_ens.yml)
```python
properties:
  dt: 1
  end: 10
  output_name: output
  output_type: pdb
  selection: System
  start: 0

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_ens_docker.yml)
```python
properties:
  container_image: gromacs/gromacs:latest
  container_path: docker
  container_volume_path: /tmp
  dt: 1
  end: 10
  output_name: output
  output_type: pdb
  selection: System
  start: 0

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_ens_singularity.yml)
```python
properties:
  container_image: shub://michael-tn/gromacs
  container_path: singularity
  container_volume_path: /tmp
  dt: 1
  end: 10
  output_name: output
  output_type: pdb
  selection: System
  start: 0

```
#### Command line
```python
gmx_trjconv_str_ens --config config_gmx_trjconv_str_ens.yml --input_traj_path trajectory.trr --input_top_path topology.tpr --input_index_path index.ndx --output_str_ens_path ref_trjconv.str.ens.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_ens.json)
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
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_ens_docker.json)
```python
{
  "properties": {
    "selection": "System",
    "start": 0,
    "end": 10,
    "dt": 1,
    "output_name": "output",
    "output_type": "pdb",
    "container_path": "docker",
    "container_image": "gromacs/gromacs:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_ens_singularity.json)
```python
{
  "properties": {
    "selection": "System",
    "start": 0,
    "end": 10,
    "dt": 1,
    "output_name": "output",
    "output_type": "pdb",
    "container_path": "singularity",
    "container_image": "shub://michael-tn/gromacs",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
gmx_trjconv_str_ens --config config_gmx_trjconv_str_ens.json --input_traj_path trajectory.trr --input_top_path topology.tpr --input_index_path index.ndx --output_str_ens_path ref_trjconv.str.ens.zip
```

## Cpptraj_average
Wrapper of the Ambertools Cpptraj module for calculating a structure average of a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_average -h
```
    /bin/sh: cpptraj_average: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd). Accepted formats: CRD, CDF, NETCDF, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed structure. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.average.pdb). Accepted formats: CRD, NETCDF, RST7, NCRST, DCD, PDB, MOL2, BINPOS, TRR, XTC, SQM
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing..
* **end** (*integer*): (-1) Ending frame for slicing..
* **steps** (*integer*): (1) Step for slicing..
* **mask** (*string*): (all-atoms) Mask definition. .
* **format** (*string*): (netcdf) Output trajectory format. .
* **cpptraj_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_average.yml)
```python
properties:
  end: -1
  format: pdb
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_average_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  end: -1
  format: pdb
  mask: c-alpha
  start: 1
  steps: 1

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_average_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  end: -1
  format: pdb
  mask: c-alpha
  start: 1
  steps: 1

```
#### Command line
```python
cpptraj_average --config config_cpptraj_average.yml --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.average.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_average.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "pdb"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_average_docker.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "pdb",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_cpptraj_average_singularity.json)
```python
{
  "properties": {
    "start": 1,
    "end": -1,
    "steps": 1,
    "mask": "c-alpha",
    "format": "pdb",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
cpptraj_average --config config_cpptraj_average.json --input_top_path cpptraj.parm.top --input_traj_path cpptraj.traj.dcd --output_cpptraj_path ref_cpptraj.average.pdb
```

## Gmx_trjconv_str
Wrapper of the GROMACS trjconv module for converting between GROMACS compatible structure file formats and/or extracting a selection of atoms.
### Get help
Command:
```python
gmx_trjconv_str -h
```
    /bin/sh: gmx_trjconv_str: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_structure_path** (*string*): Path to the input structure file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_top_path** (*string*): Path to the GROMACS input topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr). Accepted formats: TPR, GRO, G96, PDB, BRK, ENT
* **input_index_path** (*string*): Path to the GROMACS index file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx). Accepted formats: NDX
* **output_str_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_trjconv.str.pdb). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **selection** (*string*): (System) Group where the trjconv will be performed. If **input_index_path** provided, check the file for the accepted values. .
* **gmx_path** (*string*): (gmx) Path to the GROMACS executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (gromacs/gromacs:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str.yml)
```python
properties:
  selection: System

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_docker.yml)
```python
properties:
  container_image: gromacs/gromacs:latest
  container_path: docker
  container_volume_path: /tmp
  selection: System

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_singularity.yml)
```python
properties:
  container_image: shub://michael-tn/gromacs
  container_path: singularity
  container_volume_path: /tmp
  selection: System

```
#### Command line
```python
gmx_trjconv_str --config config_gmx_trjconv_str.yml --input_structure_path trajectory.trr --input_top_path topology.tpr --input_index_path index.ndx --output_str_path ref_trjconv.str.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str.json)
```python
{
  "properties": {
    "selection": "System"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_docker.json)
```python
{
  "properties": {
    "selection": "System",
    "container_path": "docker",
    "container_image": "gromacs/gromacs:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_trjconv_str_singularity.json)
```python
{
  "properties": {
    "selection": "System",
    "container_path": "singularity",
    "container_image": "shub://michael-tn/gromacs",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
gmx_trjconv_str --config config_gmx_trjconv_str.json --input_structure_path trajectory.trr --input_top_path topology.tpr --input_index_path index.ndx --output_str_path ref_trjconv.str.pdb
```

## Gmx_rgyr
Wrapper of the GROMACS gyrate module for computing the radius of gyration (Rgyr) of a molecule about the x-, y- and z-axes, as a function of time, from a given GROMACS compatible trajectory.
### Get help
Command:
```python
gmx_rgyr -h
```
    /bin/sh: gmx_rgyr: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_structure_path** (*string*): Path to the input structure file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr). Accepted formats: TPR, GRO, G96, PDB, BRK, ENT
* **input_traj_path** (*string*): Path to the GROMACS trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_index_path** (*string*): Path to the GROMACS index file. File type: input. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx). Accepted formats: NDX
* **output_xvg_path** (*string*): Path to the XVG output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_rgyr.xvg). Accepted formats: XVG
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **xvg** (*string*): (none) XVG plot formatting. .
* **selection** (*string*): (System) Group where the rgyr will be performed. If **input_index_path** provided, check the file for the accepted values. .
* **gmx_path** (*string*): (gmx) Path to the GROMACS executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (gromacs/gromacs:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rgyr.yml)
```python
properties:
  selection: System

```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rgyr_docker.yml)
```python
properties:
  container_image: gromacs/gromacs:latest
  container_path: docker
  container_volume_path: /tmp
  selection: System

```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rgyr_singularity.yml)
```python
properties:
  container_image: shub://michael-tn/gromacs
  container_path: singularity
  container_volume_path: /tmp
  selection: System

```
#### Command line
```python
gmx_rgyr --config config_gmx_rgyr.yml --input_structure_path topology.tpr --input_traj_path trajectory.trr --input_index_path index.ndx --output_xvg_path ref_rgyr.xvg
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rgyr.json)
```python
{
  "properties": {
    "selection": "System"
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rgyr_docker.json)
```python
{
  "properties": {
    "selection": "System",
    "container_path": "docker",
    "container_image": "gromacs/gromacs:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_analysis/blob/master/biobb_analysis/test/data/config/config_gmx_rgyr_singularity.json)
```python
{
  "properties": {
    "selection": "System",
    "container_path": "singularity",
    "container_image": "shub://michael-tn/gromacs",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
gmx_rgyr --config config_gmx_rgyr.json --input_structure_path topology.tpr --input_traj_path trajectory.trr --input_index_path index.ndx --output_xvg_path ref_rgyr.xvg
```
