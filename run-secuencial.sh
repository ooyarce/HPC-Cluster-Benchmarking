#!/bin/bash
#SBATCH --job-name=B8x32    # Job name
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=32
#SBATCH --output=log-bench-%j.log   # Standard output and error log
pwd; hostname; date

export PYTHONPATH=/mnt/nfshare/lib
/opt/openmpi/bin/mpirun python Benchmark.py
date
