# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:21:11 2021

@author: jihir
"""

from time import perf_counter
from numpy import *
from numpy.linalg import inv
from scipy.linalg import solve, eigh
 
t11 = perf_counter()

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

def resolverA(m,caso,d):
    t1 = perf_counter()
    A = laplaciana(m,d)
    b = ones(m)
    t2 = perf_counter()
    if caso == 1:
        Ainv = inv(A)
        Am1 = Ainv*b
    elif caso == 2:
        Am1 = solve(A,b,assume_a="gen", overwrite_a=0, overwrite_b=0)
    elif caso == 3:
        Am1 = solve(A,b,assume_a="pos", overwrite_a=0, overwrite_b=0)
    elif caso == 4:
        Am1 = solve(A,b,assume_a="sym", overwrite_a=0, overwrite_b=0)
    elif caso == 5:
        Am1 = solve(A,b,assume_a="gen", overwrite_a=1, overwrite_b=0)
    elif caso == 6:
        Am1 = solve(A,b,assume_a="gen", overwrite_a=0, overwrite_b=1)
    elif caso == 7:
        Am1 = solve(A,b,assume_a="gen", overwrite_a=1, overwrite_b=1)
    t3 = perf_counter()
    dt_i = t3-t2
    MEM = (A.nbytes+Am1.nbytes)
    # print(f"N={m} dt = {dt_i} s mem = {MEM}")
    return MEM, dt_i

def resolverB(m,caso,d):
    t1 = perf_counter()
    A = laplaciana(m,d)
    t2 = perf_counter()
    if caso == 1:
        Am1 = eigh(A,driver=None,overwrite_a=0)
    elif caso == 2:
        Am1 = eigh(A,driver="ev",overwrite_a=1)
    elif caso == 3:
        Am1 = eigh(A,driver="ev",overwrite_a=0)
    elif caso == 4:
        Am1 = eigh(A,driver="evd",overwrite_a=1)
    elif caso == 5:
        Am1 = eigh(A,driver="evd",overwrite_a=0)
    elif caso == 6:
        Am1 = eigh(A,driver="evr",overwrite_a=1)
    elif caso == 7:
        Am1 = eigh(A,driver="evr",overwrite_a=0)
    elif caso == 8:
        Am1 = eigh(A,driver="evx",overwrite_a=1)
    elif caso == 9:
        Am1 = eigh(A,driver="evx",overwrite_a=0)
    t3 = perf_counter()
    dt_i = t3-t2
    MEM = (A.nbytes+Am1.__sizeof__())
    # print(f"N={m} dt = {dt_i} s mem = {MEM}")
    return MEM, dt_i

def promedios(l1):
    l  =[]
    for i in range(len(l1[0])):
        a = []
        for j in range(len(l1)):
            a.append(l1[j][i])
        l.append(sum(a)/len(a))
    return l

def Correr(txt, d, Nc, Nr, caso):
    p = 1
    if p:
        fid = open(txt,"w")
    else:
        fid = open(txt,"a+")
    tiempos_todos = []
    fid = open(txt,"a+")
    for k in range(1,Nr):
        print("Caso "+str(k)+" de "+str(txt))
        for a in range(Nc):
            # print("corrida "+str(a+1)+" Caso "+str(k)+" de "+str(txt))
            tiempos_corrida = []
            memorias = []
            for N in Ns:
                if caso == "A":
                    memoria, tiempos =  resolverA(N,k,d)
                elif caso == "B":
                    memoria, tiempos =  resolverB(N,k,d)
                else: 
                    print("ERROR")
                    quit()
                tiempos_corrida.append(tiempos)
                memorias.append(memoria)
            tiempos_todos.append(tiempos_corrida)
        ll = promedios(tiempos_todos)
        for i in range(len(ll)):
            fid.write(f"{Ns[i]} {ll[i]} {memorias[i]}\n")
    fid.close()

Ns = [10,20,30,40,50,60,70,80,90,100,150,200,250,300,350,400,450,500,750,800,900,1000,1250,1500,1750,2000,2500,5000,7500,10000,12500]
Ncorridas = 9

Correr("solve float.txt", single, Ncorridas, 8, "A")
Correr("solve double.txt", double, Ncorridas, 8, "A")
Correr("eigh float.txt", single, Ncorridas, 10, "B")
Correr("eigh double.txt", double, Ncorridas, 10, "B")

t12 = perf_counter()
print(t12-t11)