# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:38:47 2021

@author: jihir
"""
import matplotlib.pyplot as plt
import os
import numpy as np
# import glob
# import sys

# print(glob.glob("*.txt"))
# sys.exit()


NS1 = [10,20,30,40,50,60,70,80,90,100,150,200,250,300,350,400,450,500,750,800,900,1000,1250,1500,1750,2000,2500,3000,3500,4000,5000,10000]
contenido = os.listdir()
for k in contenido:
    f = (k.split("."))
    try:
        if f[1] == "txt":
            fg = k
            tiempo_e = []
            tiempo_m = []
            with open(fg) as myfile:
                total_lines = sum(1 for line in myfile)
            if total_lines == 0:
                continue
            fid = open(fg,"r")
            
            for i in range(int(total_lines/len(NS1))):
                tiempo = []
                tiempo_m1 = []
                N = []
                for j in range(len(NS1)):
                    a = fid.readline().split(" ")
                    N.append(int(a[0]))
                    tiempo_m1.append(float(a[2]))
                    tiempo.append(float(a[1]))
                tiempo_m.append(tiempo_m1)
                tiempo_e.append(tiempo)
            fid.close()
            promedio_e = []
            promedio_m = []
            for i in range(len(tiempo_m)):
                promedio_m.append(tiempo_m[i][-1])
                promedio_e.append(tiempo_e[i][-1])
            mean_m = np.mean(promedio_m)
            mean_e = np.mean(promedio_e)
            N = np.array(N,dtype=np.float64)
            iFig = 1
            plt.figure(iFig)
            plt.subplot(2,1,1)
            for i in range(len(tiempo_e)):
                plt.loglog(N,tiempo_e[i],marker="o",markersize=2,linewidth=1.5,color="grey",mec="black",mfc="black")
            
            plt.loglog(N,[mean_e]*len(N),'--', color = 'blue',label="O(cte)")
            plt.loglog(N,(mean_e/N[-1])*(N),'--', color = 'orange',label="O(N)")
            plt.loglog(N,(mean_e/N[-1]**2)*(N**2),'--', color = 'green',label="O(N2)")
            plt.loglog(N,(mean_e/N[-1]**3)*(N**3),'--', color = 'red',label="O(N3)")
            plt.loglog(N,(mean_e/N[-1]**4)*(N**4),'--', color = 'pink',label="O(N4)")
            plt.ylim(0.00001,600)
            
            plt.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '," "],rotation=45)
            plt.yticks([0.0001,0.001,0.01,0.1,1,10,60,600],["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"])
            plt.ylabel("Tiempo ensamblado")
            plt.title(f[0])
            plt.grid(1)
            plt.subplot(2,1,2)
            for i in range(len(tiempo_m)):
                plt.loglog(N,tiempo_m[i],marker="o",markersize=2,linewidth=1.5,color="grey",mec="black",mfc="black")
            
            plt.loglog(N,[mean_m]*len(N),'--', color = 'blue',label="O(cte)")
            plt.loglog(N,(mean_m/N[-1])*(N),'--', color = 'orange',label="O(N)")
            plt.loglog(N,(mean_m/N[-1]**2)*(N**2),'--', color = 'green',label="O(N2)")
            plt.loglog(N,(mean_m/N[-1]**3)*(N**3),'--', color = 'red',label="O(N3)")
            plt.loglog(N,(mean_m/N[-1]**4)*(N**4),'--', color = 'pink',label="O(N4)")
            
            plt.ylim(0.00001,600)
            plt.legend(loc='best')
            plt.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],['10', '20', '50', '100', '200', '500', '1000', '2000', '5000', '10000',"20000"],rotation=45)
            plt.yticks([0.0001,0.001,0.01,0.1,1,10,60,600],["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"])
            plt.ylabel("Tiempo solución")
            plt.grid(1)
            
            plt.savefig(f[0],bbox_inches='tight')
            plt.show()
            iFig += 1
    except:
        pass


