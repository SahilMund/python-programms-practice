import numpy as np
arr=np.array([[2,5,7],[7,6,2],[5,8,9]])
i=0
for i in range(len(arr)):
     print("sum is:",np.sum(arr[i]))
     print("max is:",np.max(arr[i]))
     print("min is: ",np.min(arr[i]),"\n")

