import numpy as np
import pandas as pd

df1 = pd.read_csv("../Data/stu01",delimiter="::",engine='python')
df2 = pd.read_csv("../Data/stu02",delimiter="::",engine='python')

df3 = pd.merge(df1,df2,how="right")
df3 = df3.fillna(0)
# df3 = pd.DataFrame(df3,columns=['class','name','age','kor','eng','mat','bio'])
print(df3)

# help(pd.merge)