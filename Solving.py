import numpy as np 
import petsc4py
from time import perf_counter
from petsc_funcs import *
from mpi4py import MPI
petsc4py.init(sys.argv)
from petsc4py import PETSc
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

Nnodes = 2
Ncores = 2
Nruns = 10
Nbandwidth = 100
Nlist = [500,800,1500]
iterator = 0 
names = NAMES(Nlist,Ncores,Nnodes)
files = [open(name,"w") for name in names]

for N in Nlist:
    Bandwidth = NLIST(N,Nbandwidth)
    dts,dtd = np.zeros((Nruns, len(Bandwidth))),np.zeros((Nruns, len(Bandwidth)))    
    for i in range(Nruns):
        pos = 0
        for b in Bandwidth:
            A1 = MATRIX_MPIB(N,b)
            v1 = PETSc.Vec().createSeq(N)
            x1 = PETSc.Vec().createSeq(N)
            ksp = PETSc.KSP().create()

            t1 = perf_counter()
            ksp.setOperators(A1)
            ksp.solve(v1,x1)
            t2 = perf_counter()
            dts[i][pos] = t2-t1
            
            A2 = MATRIX_DENSE(N,b)
            v2 = PETSc.Vec().createSeq(N)
            x2 = PETSc.Vec().createSeq(N)
            ksp = PETSc.KSP().create()
            
            t3 = perf_counter()
            ksp.setOperators(A2)
            ksp.solve(v2,x2)
            t4 = perf_counter()
            dtd[i][pos] = t4-t3
            
            pos+=1

    dts_mean,dtd_mean = [np.mean(dts[:,j]) for j in range(len(Bandwidth))],[np.mean(dtd[:,j]) for j in range(len(Bandwidth))]
    if rank == 0:
        for b in range(Nbandwidth):
            files[iterator].write(f"{Bandwidth[b]} {dts_mean[i]}\n")
            files[iterator+1].write(f"{Bandwidth[b]} {dtd_mean[i]}\n")
            files[iterator].flush()
            files[iterator+1].flush()
    iterator +=2            
    
print("Files ready to be imported")