import movieUtil
import pandas as pd

df = movieUtil.getMovie()


#남자들의 평점의 평균
# meil = df[ df['gender'] == 'M' ]
# femeil = df[ df['gender'] == 'F' ]
# print("남",meil['rating'].mean())
# print("여",femeil['rating'].mean())
# pd.set_option(df, -1)
# print(df)

toy = df[ df['title'] == 'Toy Story (1995)']
# print(toy['rating'].mean())   # 토이스토리 평균 평점
# print(len(toy))               # 토이스토리 평가 수
# print(toy['age'].mean())      # 토이스토리 본 사람 평균나이


# @@ 영화별 평균 평점
#       오라클로 보자면 group by
#   select title, avg(rating) from df group by title
#       이런거 해주는게 pivot_table
# g = pd.DataFrame.pivot_table(df,values='rating',index='title',aggfunc='mean')
# print(g[g['rating']==5])

# @@영화별 평가수
h = pd.DataFrame.pivot_table(df,values='rating',index='title',aggfunc='count')
# print(h)
h1 = pd.DataFrame.sort_values(h,by='rating',ascending=False)
titles = h1.iloc[:100].index
# print(type(titles))
# help(pd.DataFrame.sort_values)
c = pd.DataFrame(titles,range(100))
d = pd.merge(df,c)
print(d)
e = d.pivot_table(values='rating',index='title',aggfunc='mean').sort_values(by='rating',ascending=False).head()
print(e)
# print(df['title'] == titles[:])



# @@ 여자가 더 좋아하는 영화
# 여자가 본 영화          >>>여자가 본 것 중에 영화별 평균평점
femeilMovie = df [ df['gender'] == 'F' ]
print(femeilMovie)
# 남자가 본 영화          >>>남자가 본 것 중에 영화별 평균평점
# 각각 비교해서 영화별로 여자 평균 평점이 높은 영화



# @@ 남자가 더 좋아하는 영화
# @@ 나이대별 평점의 평균
# @@ 나이대별 성별별 평점의 평균
# @@ 나이대별 평점이 가장 높은 영화
