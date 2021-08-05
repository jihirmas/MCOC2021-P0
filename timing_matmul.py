# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:01:17 2021

@author: jihir
"""

from numpy import zeros
from time import perf_counter

#Tamaño
N = 1000
Ns = [10,20,50,100,200,500,1000,2000,5000,10000]
dts = []
mems = []

p = 0#int(input("¿Primera corrida? (si = 1, no = 0) "))
if p:
    fid = open("rendimiento.txt","w")
else:
    fid = open("rendimiento.txt","a+")

for N in Ns:
    A = zeros((N, N))+1
    B = zeros((N, N))+2
    t1 = perf_counter()
    C = A@B
    t2 = perf_counter()
    dt = t2-t1
    dts.append(dt)
    uso_memoria =A.nbytes+B.nbytes+C.nbytes
    mems.append(uso_memoria)
    print(f"N={N} dt = {dt} s mem = {uso_memoria} bytes flops = {N**3/dt} flops/s")
    fid.write(f"{N} {dt} {uso_memoria} {N**3/dt}\n")

fid.close()
