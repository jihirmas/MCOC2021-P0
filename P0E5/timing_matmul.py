# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:01:17 2021

@author: jihir
"""

from numpy import *
import numpy as np
import scipy.sparse as sparse
from time import perf_counter

def laplaciana(N,tipo):
    A = zeros((N,N),dtype = tipo)
    
    for i in range(N):
        A[i][i] = 2
        for j in range(max(0,i-2),i+1):
            if abs(i-j) == 1:
                    A[i][j] = -1
                    A[j][i] = -1
               
    A[N-1][N-1] = 2; A[N-1][N-2] = -1
    return A

Ns = [10,20,30,40,50,60,70,80,90,100,150,200,250,300,350,400,450,500,750,800,900,1000,1250,1500,1750,2000,2500,3000,3500,4000,5000,10000]
dt_ensamblado = []
dt_matmul = []
p = 1
if p:
    fid = open("Tiempos_Matrices_Llenas.txt","w")
else:
    fid = open("Tiempos_Matrices_Llenas.txt","a+")
for j in range(9):
    for N in Ns:
        t1 = perf_counter()
        A = laplaciana(N,double)
        B = laplaciana(N,double)
        t2 = perf_counter()
        C = A@B
        t3 = perf_counter()
        dt_e = t2-t1
        dt_ensamblado.append(dt_e)
        dt_m = t3-t2
        dt_matmul.append(dt_m)
        fid.write(f"{N} {dt_e} {dt_m}\n")
    print(f"Corrida {j}")
fid.close()

dt_ensamblado = []
dt_matmul = []
p = 1
if p:
    fid = open("Tiempos_Matrices_Dispersas.txt","w")
else:
    fid = open("Tiempos_Matrices_Dispersas.txt","a+")
for j in range(9):
    for N in Ns:
        t1 = perf_counter()
        A = sparse.csr_matrix(laplaciana(N,double))
        B = sparse.csr_matrix(laplaciana(N,double))
        t2 = perf_counter()
        C = A@B
        t3 = perf_counter()
        dt_e = t2-t1
        dt_ensamblado.append(dt_e)
        dt_m = t3-t2
        dt_matmul.append(dt_m)
        fid.write(f"{N} {dt_e} {dt_m}\n")
    print(f"Corrida {j}")
fid.close()