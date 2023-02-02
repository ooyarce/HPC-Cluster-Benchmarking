import matplotlib.pyplot as plt
from petsc_funcs import *
import os 

Nnodes = 2
Ncores = 2
N = 500
Nbandwidth = 100
list1 = NLIST(N,Nbandwidth)

path = f'C:/Users/oioya/OneDrive/Escritorio/Cluster-CPU-Amd-Ryzen-9-5950-Benchmarking/Assambly/2-nodes/2-cores'
names = os.listdir(path)

xaxis = [10,100,200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2500]
xlabel = ["10",'100',"200","300","400","500",'600','700','800','900',"1000",'1200','1400','1600','1800',"2000",'2500']
yaxis = [0.1e-3,1e-3,1e-2,0.1,1.,10.]
ylabel = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s"] 

for name in names:
    times_list = []
    file = open(name,'r')
    results_matrix = [[(num) for num in line.split(' ')] for line in file]
    print (results_matrix)
    for i in range(len(list1)):
        times_yi_values = results_matrix[i][1]
        times_list.append(float(times_yi_values))
        
    file.close()
    plt.loglog(list1,times_list,"-o")

plt.xticks(xaxis,xlabel,rotation=45)
plt.yticks(yaxis,ylabel)
plt.grid() 
plt.xlabel("Matrix Size (N)")
plt.ylabel("Time (s)")
plt.legend(names,loc = 'upper left')
plt.title(f"Assambly time for N = {N} | {Ncores}cores & {Nnodes}")
plt.show()