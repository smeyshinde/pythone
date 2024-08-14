import pandas as pd
df=pd.read_csv('my.csv')
df.shape
df.sample(6)


import numpy as np 
l1=[1,2,3,4,5,6]
l2=[2,3,4,5,6,7]
na1=np.array(l1)
na2=np.array(l2)
na3=na1+na2
print("na3 : ",na3)
na4=na1+3
print("na4 : ",na4)
print("na1 size : ",na1.size)
