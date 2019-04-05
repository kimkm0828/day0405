import numpy as np
import pandas as pd

df1 = pd.read_csv("../Data/student01",delimiter="::",engine='python')
df2 = pd.read_csv("../Data/student02",delimiter="::",engine='python')

print(df1)
print("-"*100)
print(df2)

df3 = pd.merge(df1,df2,how="right")
df3 = pd.DataFrame(df3,columns=['class','name','age','kor','eng','mat','bio'])
print(df3)