import numpy as np 
from numpy import zeros,float32
from scipy import linalg
from time import perf_counter
import matplotlib.pyplot as plt
import os 

list1 = list(range(10,101,10))
list1.append(range(125,1001,25))
list1.append(range(1100,2001,100))

nnodes = 2
ncores = 16

path = f'C:/Users/oioya/OneDrive/Escritorio/Cluster-CPU-Amd-Ryzen-9-5950-Benchmarking/Results/Text Files/Assambly/2x2'
names = os.listdir(path)

x = [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2500]#,16000,32000,64000,120000,240000,480000,1000000,1000000*2,1000000*4,1000000*8,1000000*12]
xlab = ["0","100","200","300","400","500",'600','700','800','900',"1000",'1100','1200','1300','1400','1500','1600','1700','1800','1900',"2000",'2500']
y = [0.1e-3,1e-3,1e-2,0.1,1.,10.]
ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s"] 

for name in names:
    times_list = []
    file = open(name,'r')
    results_matrix = [[(num) for num in line.split(' ')] for line in file]

    for i in range(len(list1)):
        times_yi_values = results_matrix[i][1]
        times_list.append(float(times_yi_values))
    
    file.close()
    plt.loglog(list1,times_list,"-o")

plt.xticks(x,xlab,rotation=45)
plt.yticks(y,ylab)
plt.grid() 
plt.xlabel("Matrix Size (N)")
plt.ylabel("Time (s)")
plt.legend(names,loc = 'upper left')
plt.title(f"Assambly time {nnodos}nodes-{ncores}cores")
plt.show()