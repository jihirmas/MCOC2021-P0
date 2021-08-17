# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:21:11 2021

@author: jihir
"""

from time import perf_counter
from numpy import *
from numpy.linalg import inv
from laplaciana import laplaciana


Ns = [10,20,30,40,50,60,70,80,90,100,150,200,250,300,350,400,450,500,750,1000,1500,2000,5000,10000]
dts = []
mems = []

txt = "timing_inv_caso_1_half.txt"

p = 1
if p:
    fid = open(txt,"w")
else:
    fid = open(txt,"a+")
for a in range(10):
    fid = open(txt,"a+")
    print("corrida "+str(a+1))
    for N in Ns:
        t1 = perf_counter()
        A = laplaciana(N,half)
        t2 = perf_counter()
        Am1 = inv(A)
        t3 = perf_counter()
        dt_i = t3-t2
        print(f"N={N} dt = {dt_i} s mem = {(A.nbytes+Am1.nbytes)}")
        fid.write(f"{N} {dt_i} {(A.nbytes+Am1.nbytes)}\n")
    
    fid.close()