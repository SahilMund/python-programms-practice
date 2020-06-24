import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
df=pd.DataFrame({"category":["a","b","b","c","a","a","b","c","a","c","d"],"values":[2,6,4,2,5,7,5,3,3,2,9]})
cat=np.array(df["category"].tolist())
print(cat)
valcat=np.unique(cat)
print(valcat)
count=[]
for i in valcat:
	count.append(cat.tolist().count(i))
print(count)
plt.figure(figsize=(8,5))
plt.title("Bar Chart",color="m",fontsize=16)
plt.xlabel("category",color="b",fontsize=12)
plt.ylabel("value",color="b",fontsize=12)
plt.grid()
#plt.bar(valcat,count,color="cmyk")
plt.pie(count,labels=valcat)
plt.show()
