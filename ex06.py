import numpy as np
import pandas as pd

# 영화::영화제목::장르
movies = pd.read_csv("../ml-1m/movies.dat",delimiter="::",engine='python',header=None,
                    names=['movieid','title','janre'])


# 사용자id::영화id::별점::시간
ratings = pd.read_csv("../ml-1m/ratings.dat",delimiter="::",engine='python',header=None,
                    names=['userid','movieid','rating','times'])


# 사용자::성별::나이::직업::우편
users = pd.read_csv("../ml-1m/users.dat",delimiter="::",engine='python',header=None,
                    names=['userid','gender','age','job','addr'])


# 공통되는부분이 있어야함 inner join 같은거
df = pd.merge(pd.merge(movies,ratings),users)

print(df.head())
