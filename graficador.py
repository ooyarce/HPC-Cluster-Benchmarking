import numpy as np 
from numpy import zeros,float32
from scipy import linalg
from time import perf_counter
import matplotlib.pyplot as plt
import os 

path = 'C:/Users/oioya/OneDrive/Escritorio/Cluster-CPU-Amd-Ryzen-9-5950-Benchmarking/Results/Text Files/Assambly/Sparse_Conclusions/Nodes_2/Sparse2'
list1 = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600, 800,1000,2000]
names = os.listdir(path)

#labels y escalados para el grafico
x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xlab = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10, 60*100]
ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"] 
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
ylab2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]

#valores que tomara y en la lista times_list
for i in range(len(list1)):
    for name in names:
        #primer rendimiento
        file = open(name,'r')
        results_matrix = [[(num) for num in line.split(' ')] for line in file]
        print (results_matrix)
        for i in range(len(list1)):
            times_yi_values = results_matrix[i][1]
            times_list.append(float(times_yi_values))
        file.close()
        plt.loglog(list1,times_list,"-o")

#defino los parámetros de mi grafico
plt.xticks(x,xlab,rotation='45')
plt.yticks(y,ylab)
plt.grid() 
plt.xlabel("Tamaño de la matriz")
plt.ylabel("Tiempo Transcurrido (s)")
plt.legend(["A_invB_inv.txt","A_invB_npSolve.txt","A_invB_spSolve.txt","A_invB_spSolve_symmetric.txt",
         "A_invB_spSolve_pos.txt","A_invB_spSolve_pos_overwrite.txt"],loc = 'upper left')
plt.title("Rendimiento A@B")

plt.show()