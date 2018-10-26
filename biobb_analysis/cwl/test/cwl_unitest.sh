#!/usr/bin/env bash
BIOBB_ANALYSIS=$HOME/projects/biobb_analysis/biobb_analysis
cwltool $BIOBB_ANALYSIS/cwl/gromacs/cluster.cwl $BIOBB_ANALYSIS/cwl/test/gromacs/cluster.yml
cwltool $BIOBB_ANALYSIS/cwl/gromacs/rms.cwl $BIOBB_ANALYSIS/cwl/test/gromacs/rms.yml
