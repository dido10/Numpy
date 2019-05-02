# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:27:29 2019

@author: didem.durmaz
"""
#vektörel çarpım a*b=a^T*b eşit benişlikteki arrayler için

#vektörel çarpım a*b=mutlak(a*b)*cos0(ab arasındaki açı) eşit benişlikteki arrayler için

#ve cos0=a^Tb/(mutlak(a*b))

import numpy as np
b=np.array([2,1])
a=np.array([1,2,])

dot=0
for e,f in zip(a,b):
    dot+=e*f    #dot=4
    
print(a*b)      #[2 2]

np.sum(a*b)     #4
(a*b).sum()     #4
np.dot(a,b)     #4
a.dot(b)     #4

a_magnitude=np.sqrt((a*a).sum())    #2.23606797749979

a_magnitude=np.linalg.norm(a)       #2.23606797749979
cosangle=a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b)) # 0.7999999999999998
angle=np.arccos(cosangle)       #0.6435011087932847
