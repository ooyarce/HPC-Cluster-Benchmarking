#!/bin/bash
#SBATCH --job-name=A4x8    # Job name
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=8
#SBATCH --output=log-assambly-%j.log   # Standard output and error log
pwd; hostname; date
export PYTHONPATH=/mnt/nfshare/lib
/opt/openmpi/bin/mpirun python Assambly.py
date
