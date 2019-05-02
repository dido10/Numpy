
import numpy as np

L=[[1,2],[2,3]]
M=np.array([[1,2],[3,4]])


M[0]        #array([1, 2])
M[0][0]        #1

L[1]        #array([2, 3])
M[1][1]     #4


M2=np.matrix([[1,2],[3,4]])

A=np.array(M2)
A.T   #array([[1, 3],
     #        [2, 4]])
