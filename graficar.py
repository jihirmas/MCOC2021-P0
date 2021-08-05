# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:38:47 2021

@author: jihir
"""
import matplotlib.pylab as plt
tiempo_t = []
fid = open("rendimiento.txt","r")
for i in range(10):
    tiempo = []
    memoria = []
    N = []
    for j in range(len([10,20,50,100,200,500,1000,2000,5000,10000])):
        a = fid.readline().split()
        N.append(int(a[0]))
        memoria.append(int(a[2]))
        tiempo.append(float(a[1]))
    tiempo_t.append(tiempo)
fid.close()

plt.subplot(2,1,1)
for i in range(len(tiempo_t)):
    plt.loglog(N,tiempo_t[i],marker="o")
plt.grid(1)
plt.xticks(visible=0)
plt.yticks([0.0001,0.001,0.01,0.1,1,10,60,600],["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"])
plt.ylabel("Tiempo transcurrido")
plt.title("Rendimiento A@B")
plt.subplot(2,1,2)
plt.loglog(N,memoria,marker="o")
plt.grid(1)
plt.yticks([1e+3,1e+4,1e+5,1e+6,1e+7,1e+8,1e+9,1e+10],["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"])
Ns = []
for i in range(len(N)):
    Ns.append(str(N[i]))
plt.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],['10', '20', '50', '100', '200', '500', '1000', '2000', '5000', '10000',"20000"],rotation=45)
plt.axhline(y=1.6e+10,linestyle="--",color="black")
plt.ylabel("Uso memoria")
plt.xlabel("Tamaño matriz N")
plt.show()

