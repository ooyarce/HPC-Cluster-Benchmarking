import numpy as np 
from numpy import zeros,float32
from scipy import linalg
from time import perf_counter
import matplotlib.pyplot as plt
from laplacianas import matriz_laplaciana_llena
Ncorridas = 10
list1 = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600, 800,
         1000,2000, 5000, 10000]
names = ["A_invB_inv.txt", "A_invB_npSolve.txt","A_invB_spSolve.txt","A_invB_spSolve_symmetric.txt",
         "A_invB_spSolve_pos.txt","A_invB_spSolve_pos_overwrite.txt"]
files = [open(name,"w") for name in names]
#labels y escalados para el grafico
x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xlab = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10, 60*100]
ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"] 
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
ylab2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]

plt.figure()
#creo el gráfico 
plt.subplot(2,1,1)
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
    print (results_matrix)
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
plt.xticks(x,xlab,rotation='45')
plt.yticks(y,ylab)
plt.grid() 
plt.xlabel("Tamaño de la matriz")
plt.ylabel("Tiempo Transcurrido (s)")
plt.legend(["A_invB_inv.txt","A_invB_npSolve.txt","A_invB_spSolve.txt","A_invB_spSolve_symmetric.txt",
         "A_invB_spSolve_pos.txt","A_invB_spSolve_pos_overwrite.txt"],loc = 'upper left')
plt.title("Rendimiento A@B")

plt.show()