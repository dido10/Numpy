import numpy as np
A=np.array([[1,2],[3,4]])
Ainv=np.linalg.inv(A) #inverse of A
Ainv.dot(A) #identity matrix
A.dot(Ainv) #identity matrix
np.linalg.det(A)    #determinant
np.diag(A)      #diagonal eleman
np.diag([1,2])  #2-D array
#outer product (önce hangisi ise ilk matrisin tek tek elemanı ile diğer matrisi çarpar)
a=np.array([1,2])
b=np.array([2,3])
np.outer(a,b)   #array([[2, 3],[4, 6]])=(1*[2,3],2*[2,3])
#inner product of a and b (aij nin bij ile çaarpımı-aynı ij ile)
np.inner(a,b)   #8=1*2+2*3
a.dot(b)    #=inner product 8
b.dot(a)    #=inner product 8
#sum of diagonal (matris orta elemanların toplamı)
np.diag(A).sum()  
np.trace(A) #same print =5
#eigenvectors
X=np.random.randn(100,3)    #3 column 100 row
cov=np.cov(X)
cov.shape#100,100
cov=np.cov(X.T)
np.linalg.eig(cov)  #=cov=np.cov(X.T)
