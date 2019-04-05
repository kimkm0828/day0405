import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Data/scores.csv")

#데이터가 짱짱 많을때
# print(df.head()) # 앞에 몇개만 보여줘
# print(df.tail()) # 뒤에 몇개만 보여줘


del df['class']
df.index = df['name']
del df['name']
mean_down_idx = df['mat'] <= df['mat'].mean()
print(df[mean_down_idx])
# 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
df[mean_down_idx].plot(kind = 'bar',cmap=plt.get_cmap('inferno'))
# plt.xticks(range(df.idx),df.idx,rotation=45)
plt.show()

help(pd.DataFrame.plot)