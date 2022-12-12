import numpy as np 
from numpy import zeros,float32
from scipy import linalg
from time import perf_counter
import matplotlib.pyplot as plt
from laplacianas import matriz_laplaciana_llena
from PETSc_Sparse import sparse, llena
import petsc4py
import sys
petsc4py.init(sys.argv)
from petsc4py import PETSc
from matplotlib import pylab


Ncorridas = 10
list1 = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600]
names = ["PETSc_Sparse", "PETSc_LLena","A_invB_spSolve.txt","A_invB_spSolve_symmetric.txt",
         "A_invB_spSolve_pos.txt","A_invB_spSolve_pos_overwrite.txt"]
files = [open(name,"w") for name in names]

#escribo mis archivos de texto con los tiempos promedio para cada tamaño de matriz
for N in list1:
    print (f"Para N = {N}")
    dts = np.zeros((Ncorridas, len(files)))
    
    for i in range(Ncorridas):

        A = sparse(N)

        b = PETSc.Vec().createSeq(N) # creating a vector
        b.setValues(range(N), range(1,N+1)) # assigning values to the vector

        x = PETSc.Vec().createSeq(N) # create the solution vector x

        ksp = PETSc.KSP().create() # creating a KSP object named ksp
        ksp.setOperators(A)

        # Allow for solver choice to be set from command line with -ksp_type <solver>.
        ksp.setFromOptions()
        #print ('\\n Solving with:', ksp.getType()) # prints the type of solver
        t1 = perf_counter()
        # Solve!
        ksp.solve(b, x) 

        t2 = perf_counter()
        dt = t2-t1
        dts[i][0] = dt


        #metodo2
        A2 = llena(N)

        b2 = PETSc.Vec().createSeq(N) # creating a vector
        b2.setValues(range(N), range(1,N+1)) # assigning values to the vector

        x2 = PETSc.Vec().createSeq(N) # create the solution vector x

        ksp = PETSc.KSP().create() # creating a KSP object named ksp
        ksp.setOperators(A2)

        # Allow for solver choice to be set from command line with -ksp_type <solver>.
        ksp.setFromOptions()
        #print ('\\n Solving with:', ksp.getType()) # prints the type of solver
        t3 = perf_counter()
        # Solve!
        ksp.solve(b2, x2) 

        t4 = perf_counter()
        dt2 = t4-t3
        dts[i][1] = dt2
        

        #metodo3
        A3 = matriz_laplaciana_llena(N)
        b3 = np.ones(N)
        t5 = perf_counter()
        X3 = linalg.solve(A3,b3,assume_a="sym")
        t6 = perf_counter()
        dt3 = t6-t5
        dts[i][2] = dt3
        #metodo4
        A4 = matriz_laplaciana_llena(N)
        b4 = np.ones(N)
        t7 = perf_counter()
        X4 = linalg.solve(A4,b4,assume_a="sym")
        t8 = perf_counter()
        dt4 = t8-t7
        dts[i][3] = dt4
        #metodo5
        A5 = matriz_laplaciana_llena(N)
        b5 = np.ones(N)
        t9 = perf_counter()
        X5 = linalg.solve(A5,b5,assume_a="pos")
        t10 = perf_counter()
        dt5 = t10-t9
        dts[i][4] = dt5
        #metodo6
        A6 = matriz_laplaciana_llena(N)
        b6 = np.ones(N)
        t11 = perf_counter()
        X6 = linalg.solve(A6,b6,assume_a="pos",overwrite_a=True,overwrite_b=True)
        t12 = perf_counter()
        dt6 = t12-t11
        dts[i][5] = dt6
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    print (f"dts_mean = {dts_mean}")
    #relleno con la info de la media de los tiempos los archivos de texto
    for i in range(len(files)):
        files[i].write(f"{N} {dts_mean[i]}\n")
        files[i].flush()
[file.close() for file in files]        

#labels y escalados para el grafico
x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xlab = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]
ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"] 
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
ylab2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]

#creo el grafico
#valores que tomara y en la lista times_list
for i in range(len(list1)):
    times_list = []
    times_list2 = []
    times_list3 = []
    times_list4 = []
    times_list5 = []
    times_list6 = []
    name = names[0]
    name2 = names[1]
    name3 = names[2]
    name4 = names[3]
    name5 = names[4]
    name6 = names[5]
    
    #primer rendimiento
    file = open(name,'r')
    results_matrix = [[(num) for num in line.split(' ')] for line in file]
    for i in range(len(list1)):
        times_yi_values = results_matrix[i][1]
        times_list.append(float(times_yi_values))
    file.close()
    
    #segundo rendimiento
    file = open(name2,'r')
    results_matrix2 = [[(num) for num in line.split(' ')] for line in file]
    for i in range(len(list1)):
        times_yi_values = results_matrix2[i][1]
        times_list2.append(float(times_yi_values))
    file.close()
    
    #tercer rendimiento
    file = open(name3,'r')
    results_matrix3 = [[(num) for num in line.split(' ')] for line in file]
    for i in range(len(list1)):
        times_yi_values = results_matrix3[i][1]
        times_list3.append(float(times_yi_values))
    file.close()
    
    #cuarto rendimiento
    file = open(name4,'r')
    results_matrix4 = [[(num) for num in line.split(' ')] for line in file]
    for i in range(len(list1)):
        times_yi_values = results_matrix4[i][1]
        times_list4.append(float(times_yi_values))
    file.close()
    
    #quinto rendimiento
    file = open(name5,'r')
    results_matrix5 = [[(num) for num in line.split(' ')] for line in file]
    for i in range(len(list1)):
        times_yi_values = results_matrix5[i][1]
        times_list5.append(float(times_yi_values))
    file.close()
    
    #sexto rendimiento
    file = open(name6,'r')
    results_matrix6 = [[(num) for num in line.split(' ')] for line in file]
    for i in range(len(list1)):
        times_yi_values = results_matrix6[i][1]
        times_list6.append(float(times_yi_values))
    file.close()
    
#ploteo
plt.loglog(list1,times_list,"-o")
plt.loglog(list1,times_list2,"-o")
plt.loglog(list1,times_list3,"-o")
plt.loglog(list1,times_list4,"-o")
plt.loglog(list1,times_list5,"-o")
plt.loglog(list1,times_list6,"-o")

#defino los parámetros de mi grafico
plt.xticks(x,xlab,rotation=45)
plt.yticks(y,ylab)
plt.grid() 
plt.xlabel("Tamaño de la matriz")
plt.ylabel("Tiempo Transcurrido (s)")
plt.legend(["PETSc_Sparse","PETSc_LLena","A_invB_spSolve.txt","A_invB_spSolve_symmetric.txt",
         "A_invB_spSolve_pos.txt","A_invB_spSolve_pos_overwrite.txt"],loc = 'upper left')
plt.title("Rendimiento")

plt.tight_layout()
plt.savefig("Result_plot")