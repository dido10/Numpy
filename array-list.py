#basic level array and list differences
import numpy as np
L=[1,2,3]
A=np.array([1,2,3])
L.append(4)
L=L+[8]  #L=[1,2,3,4,8]
A.append(4)  #hata alacak
A=A+[4] #hata alacak
A*2     #array([2, 4, 6])
L*2     # [1, 2, 3,4,8, 1, 2, 3,4,8]
L2=[]
for e in L:
    L2.append(e*e)  #L2=[1,4,9,16,64]
