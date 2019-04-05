import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data = pd.read_csv("/Data/scores.csv")
df = pd.read_csv("../Data/scores.csv")
# print(df)

idx = df['class'] == 1
class1 = df[idx]
# print(class1)

# @@ 1반 학생의 과목별 평균
del class1['class']
class1.index = class1['name']
del class1['name']
print(class1)
# print(class1.mean())        #과목별 평균
# print(class1.mean(axis=1))  #학생별 평균

#---------------------------------
# totK = 0
# totE = 0
# totM = 0
# totB = 0
#
# for i in range(len(class1)):
#     totK += class1['kor'][i]
#     totE += class1['eng'][i]
#     totM += class1['mat'][i]
#     totB += class1['bio'][i]
#
# avgK = totK / len(class1)
# avgE = totE / len(class1)
# avgM = totM / len(class1)
# avgB = totB / len(class1)
#
# print(avgK)
# print(avgE)
# print(avgM)
# print(avgB)

# @@ 1반 생물성적 막대그래프
# print(class1['kor'])
# plt.bar(range(len(class1.index)),class1['kor'])
# plt.xticks(range(len(class1.index)),class1.index)
# plt.show()

class1.plot(kind='hist')
# plt.xticks(range(len(class1.index)),class1.index,rotation=45)
plt.show()
# help(pd.DataFrame.plot)




