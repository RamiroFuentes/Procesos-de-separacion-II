# Librerias 
import numpy as np
from numpy import poly1d,polyfit  
import matplotlib.pyplot as plt
from sympy import Symbol
import pandas as pd

# Para imprimir en formato LaTex
from sympy.interactive import printing
printing.init_printing(use_latex=True)


def Rachford_Rice_4(z,k,Li,Ls,p):
    psi = np.arange(Li,Ls+p,p)
    f_psi = []
    for value in psi:
        f_psi.append((z[0]*(1-k[0])/(1+value*(k[0]-1))) + (z[1]*(1-k[1])/(1+value*(k[1]-1))) + (z[2]*(1-k[2])/(1+value*(k[2]-1))) + (z[3]*(1-k[3])/(1+value*(k[3]-1))) )
        
    return psi,f_psi

def find_root_interval(given):
    i = 0
    for value in given:
        if value >=0:
            P_1 = i
            P_0 = i-1
        else: 
            i += 1
    return P_0,P_1

def interp(x_1,x_2,y_1,y_2,y_n):
    x_n = x_1 -((x_1-x_2)*(y_1-y_n)/(y_1-y_2))
    return x_n , y_n

def interp_y(x_1,x_2,y_1,y_2,x_n):
    y_n = y_1 + (y_2-y_1)*((x_n-x_1)/(x_2-x_1))
    return x_n , y_n

def fracc(z_i,Psi_c,k_i):
    x_i = []
    y_i = []
    i = 0
    
    for element in z_i:
        x_i.append(z_i[i]/(1+Psi_c*(k_i[i]-1)))
        y_i.append(k_i[i]*x_i[i])
        i += 1      
    return x_i,y_i