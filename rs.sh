#!/bin/bash
#SBATCH --job-name=S2x2    # Job name
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --output=log-solving-%j.log   # Standard output and error log
pwd; hostname; date

export PYTHONPATH=/mnt/nfshare/lib
/opt/openmpi/bin/mpirun python Solving.py
date
