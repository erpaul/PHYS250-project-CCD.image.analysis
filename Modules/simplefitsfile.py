#!/usr/bin/env python
# coding: utf-8

import numpy as np
import statistics   

def avgvalue(a, final):    
    value_list=[]
    for n in range(final):
        value_list.append(a[n])    
    avg=np.sum(value_list)/final
    return(avg)
            
def sigma(a, final, mean): 
    energies=[]
    for n in range(final):
        energies.append(a[n])
    sigma=statistics.stdev(energies, mean)
    return(sigma)
            
def new_fits(ary, mean, stdev):
    for y in range(len(ary)):
        for x in range(len(ary[0])):
            if ary[y,x]>mean+stdev:
                ary[y,x]=1
            else:
                ary[y,x]=0
    return(ary)



