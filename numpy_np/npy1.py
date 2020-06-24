import numpy as np
list1=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(list1)
print(arr)
r,c=arr.shape
print("no of rows:",r)
print("no of colms:",c)
print(arr.ndim)
print(arr.nbytes)
print(arr.itemsize)
print(arr.size)
print(len(arr))
print(sum(arr))
