# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:57:58 2021

@author: jihir
"""

from numpy import *
import numpy as np
from scipy.linalg import solve, inv
import scipy.sparse as sparse
import scipy.sparse.linalg as lin
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

Ns1 = [10,20,30,40,50,60,70,80,90,100,150,200,250,300,350,400,450,500,750,800,900,1000,1250,1500,1750,2000,2500,3000,3500,4000,5000,10000]
Ns2 = [10,20,30,40,50,60,70,80,90,100,150,200,250,300,350,400,450,500,750,800,900,1000,1250,1500,1750,2000,2500,3000,3500,4000,5000,10000]

dt_ensamblado = []
dt_solve = []
p = 1
if p:
    fid = open("Tiempos_Matrices_Llenas_SOLVE.txt","w")
else:
    fid = open("Tiempos_Matrices_Llenas_SOLVE.txt","a+")
for j in range(9):
    for N in Ns1:
        print(f"corrida del N = {N}")
        t1 = perf_counter()
        A = laplaciana(N,double)
        B = np.ones(N,double)
        t2 = perf_counter()
        C = solve(A,B)
        t3 = perf_counter()
        dt_e = t2-t1
        dt_ensamblado.append(dt_e)
        dt_s = t3-t2
        dt_solve.append(dt_s)
        fid.write(f"{N} {dt_e} {dt_s}\n")
    print(f"Corrida {j}")
fid.close()

dt_ensamblado = []
dt_solve = []
p = 1
if p:
    fid = open("Tiempos_Matrices_Dispersa_SOLVE.txt","w")
else:
    fid = open("Tiempos_Matrices_Dispersa_SOLVE.txt","a+")
for j in range(9):
    for N in Ns2:
        print(f"corrida del N = {N}")
        t1 = perf_counter()
        A = sparse.csr_matrix(laplaciana(N,double))
        B = np.ones(N,double)
        t2 = perf_counter()
        C = lin.spsolve(A,B)
        t3 = perf_counter()
        dt_e = t2-t1
        dt_ensamblado.append(dt_e)
        dt_s = t3-t2
        dt_solve.append(dt_s)
        fid.write(f"{N} {dt_e} {dt_s}\n")
    print(f"Corrida {j}")
fid.close()

dt_ensamblado = []
dt_solve = []
p = 1
if p:
    fid = open("Tiempos_Matrices_Llenas_INV.txt","w")
else:
    fid = open("Tiempos_Matrices_Llenas_INV.txt","a+")
for j in range(9):
    for N in Ns1:
        print(f"corrida del N = {N}")
        t1 = perf_counter()
        A = laplaciana(N,double)
        t2 = perf_counter()
        C = inv(A,overwrite_a=True)
        t3 = perf_counter()
        dt_e = t2-t1
        dt_ensamblado.append(dt_e)
        dt_s = t3-t2
        dt_solve.append(dt_s)
        fid.write(f"{N} {dt_e} {dt_s}\n")
    print(f"Corrida {j}")
fid.close()
    
dt_ensamblado = []
dt_solve = []
p = 1
if p:
    fid = open("Tiempos_Matrices_Dispersa_INV.txt","w")
else:
    fid = open("Tiempos_Matrices_Dispersa_INV.txt","a+")
for j in range(9):
    for N in Ns2:
        print(f"corrida del N = {N}")
        t1 = perf_counter()
        A = sparse.csc_matrix(laplaciana(N,double))
        t2 = perf_counter()
        C = lin.inv(A)
        t3 = perf_counter()
        dt_e = t2-t1
        dt_ensamblado.append(dt_e)
        dt_s = t3-t2
        dt_solve.append(dt_s)
        fid.write(f"{N} {dt_e} {dt_s}\n")
    print(f"Corrida {j}")
fid.close()
