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

nnodos = 1
ncores = 6
Ncorridas = 10
list1 = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600]#,2000]#,4000,8000,16000,32000,64000,120000]
names = [f"Sparse_MPI1{nnodos}x{ncores}.txt",f"Sparse_MPI2{nnodos}x{ncores}.txt",f"Sparse_MPI3{nnodos}x{ncores}.txt",f"Dense_MPI{nnodos}x{ncores}.txt"]
files = [open(name,"w") for name in names]

print(f"Trabajando con {nnodos} nodos y {ncores} nucleos")


#escribo mis archivos de texto con los tiempos promedio para cada tamaño de matriz
for N in list1:
    Bandwitch = [int(N/4),int(N/2),int(3*N/4)]
    print (f"N = {N}")
    print (f"Rank = {rank}\n")
    dts = np.zeros((Ncorridas, len(files)))
    
    for i in range(Ncorridas):
        #método 1
        pos = 0
        for bandwitch in Bandwitch:
            t1 = perf_counter()
            A = MATRIX_MPIB(N,bandwitch)
            t2 = perf_counter()
            b = PETSc.Vec().createMPI(N) # creating a vector
            #b.setValues(range(N), range(1,N+1)) # assigning values to the vector

            x = PETSc.Vec().createMPI(N) # create the solution vector x

            ksp = PETSc.KSP().create() # creating a KSP object named ksp
            ksp.setOperators(A)

            # Allow for solver choice to be set from command line with -ksp_type <solver>.
            ksp.setFromOptions()
            #print ('\\n Solving with:', ksp.getType()) # prints the type of solver
            
            # Solve!
            ksp.solve(b, x) 

            
            dt = t2-t1
            dts[i][pos] = dt
            pos+=1

        #método 2
        t3 = perf_counter()
        A = llena(N)
        t4 = perf_counter()
        b = PETSc.Vec().createMPI(N) # creating a vector
        #b.setValues(range(N), range(1,N+1)) # assigning values to the vector

        x = PETSc.Vec().createMPI(N) # create the solution vector x

        ksp = PETSc.KSP().create() # creating a KSP object named ksp
        ksp.setOperators(A)

        # Allow for solver choice to be set from command line with -ksp_type <solver>.
        ksp.setFromOptions()
        #print ('\\n Solving with:', ksp.getType()) # prints the type of solver
        
        # Solve!
        ksp.solve(b, x) 

        
        dt2 = t4-t3
        dts[i][pos] = dt2
            
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    #print (f"dts_mean = {dts_mean}")
    #relleno con la info de la media de los tiempos los archivos de texto
    if rank == 0:
        for i in range(len(files)):
            files[i].write(f"{N} {dts_mean[i]}\n")
            files[i].flush()
if rank == 0:
    [file.close() for file in files]        

    #labels y escalados para el grafico
    x = [10,20,50,100,200,500,1000,2000]#,4000,8000,16000,32000,64000,120000,240000,480000,1000000,1000000*2,1000000*4,1000000*8,1000000*12]
    xlab = ["10","20","50","100","200","500","1000","2000"]#,'4000','8000','16000','32000','64000','120000','240000',"480000",'1e06','2e06','4e06','8e06','16e06']
    y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60]
    ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min"] 

    #creo el grafico
    #valores que tomara y en la lista times_list
    for name in names:
        for i in range(len(list1)):
            times_list = []
            file = open(name,'r')
            results_matrix = [[(num) for num in line.split(' ')] for line in file]
            for i in range(len(list1)):
                times_yi_values = results_matrix[i][1]
                times_list.append(float(times_yi_values))
        plt.loglog(list1,times_list,"-o")
        file.close()

    #ploteo
    #defino los parámetros de mi grafico
    plt.xticks(x,xlab,rotation=45)
    plt.yticks(y,ylab)
    plt.grid() 
    plt.xlabel("Tamaño de la matriz")
    plt.ylabel("Tiempo Transcurrido (s)")
    plt.legend([f"Sparse_MPI1{nnodos}x{ncores}.txt",f"Sparse_MPI2{nnodos}x{ncores}.txt",f"Sparse_MPI3{nnodos}x{ncores}.txt",f"Dense_MPI{nnodos}x{ncores}.txt"],loc = 'upper left')
    plt.title(f"Ensamblado {nnodos}nodos-{ncores}nucleos")
    plt.tight_layout()
    plt.show()
    plt.savefig(f"Assambly{nnodos}x{ncores}")