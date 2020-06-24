import numpy as np
l1=[1,2,3,4,5,6,7,8,9]
l2=[[1,2,3],[4,5,6],[7,8,9]]
a1=np.array(l1)
a2=np.array(l2)
print(l1,l2,a1,a2)
#print(a1+a2)  ------not possible bcz dimension is different
a3=a2.flatten()#----conversion of N-D array to 1-D array
print(a1+a3)
#to convert 1-D to N-D array
a2shape=a2.shape
a4=a2.reshape(a2shape)
print(a2)
