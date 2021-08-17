# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:01:33 2021

@author: jihir
"""

from numpy import *

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
