import numpy as np 
from numpy import zeros,float32
from scipy import linalg
from time import perf_counter
import matplotlib.pyplot as plt
from laplacianas import matriz_laplaciana_llena
from PETSc_Sparse import *
import petsc4py
import sys
from mpi4py import MPI
petsc4py.init(sys.argv)
from petsc4py import PETSc
from matplotlib import pylab
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

nnodos = 2
ncores = 2
Nruns = 10
Nlist = [500,1000,2000]

names = [f"Sparse_N500_{nnodos}x{ncores}.txt",f"Sparse_N1000_{nnodos}x{ncores}.txt",f"Sparse_N2000_{nnodos}x{ncores}.txt",f"Dense_{nnodos}x{ncores}.txt"]
files = [open(name,"w") for name in names]
if rank == 0:
    print(f"Trabajando con {nnodos} nodos y {ncores} nucleos")

for N in Nlist:
    Bandwitch = list1(N)
    dts = np.zeros((Nruns, len(files)))
    
    for i in range(Nruns):
        #método 1
        pos = 0
        for bandwitch in Bandwitch:
            t1 = perf_counter()
            A = MATRIX_MPIB(N,bandwitch)
            t2 = perf_counter()
            dt = t2-t1
            dts[i][pos] = dt
            pos+=1
        #método 2 
        t3 = perf_counter()
        A = llena(N)
        t4 = perf_counter()
        dt2 = t4-t3
        dts[i][pos] = dt2
            
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]

    if rank == 0:
        for i in range(len(files)):
            files[i].write(f"{N} {dts_mean[i]}\n")
            files[i].flush()
if rank == 0:
    [file.close() for file in files]        
    #labels y escalados para el grafico
    x = [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2500]#,16000,32000,64000,120000,240000,480000,1000000,1000000*2,1000000*4,1000000*8,1000000*12]
    xlab = ["0","100","200","300","400","500",'600','700','800','900',"1000",'1100','1200','1300','1400','1500','1600','1700','1800','1900',"2000",'2500']#,'16000','32000','64000','120000','240000',"480000",'1e06','2e06','4e06','8e06','16e06']
    y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60.]
    ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min"] 

    for name in names:
        for i in range(len(Nlist)):
            times_list = []
            file = open(name,'r')
            results_matrix = [[(num) for num in line.split(' ')] for line in file]
            for i in range(len(Nlist)):
                times_yi_values = results_matrix[i][1]
                times_list.append(float(times_yi_values))

        file.close()

print("Files ready to be imported")