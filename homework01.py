import movieUtil
import pandas as pd

df = movieUtil.getMovie()



# @@ 여자가 더 좋아하는 영화
# 여자가 본 영화          >>>여자가 본 것 중에 영화별 평균평점
femeilMovie = df [ df['gender'] == 'F' ]
FeMovieR = femeilMovie.pivot_table(values='rating',index='title',aggfunc='mean')
a = pd.DataFrame(FeMovieR,range(len(FeMovieR)))
# FeMovieR.columns = ['Frating']
# FeMovieR = pd.DataFrame({"title":FeMovieR.index,"Frating":FeMovieR['Frating']})



# 남자가 본 영화          >>>남자가 본 것 중에 영화별 평균평점
meilMovie = df [ df['gender'] == 'M' ]
MeMovieR = meilMovie.pivot_table(values='rating',index='title',aggfunc='mean')
b = pd.DataFrame(MeMovieR,range(len(MeMovieR)))
# MeMovieR.columns = ['Mrating']
# MeMovieR = pd.DataFrame({"title":MeMovieR.index,"Mrating":MeMovieR['Mrating']})


# total_movie = df.pivot_table(values='movieid',index='title')
# total_movie = pd.DataFrame({"title":total_movie.index})

# 두개 합쳐서 non 없는거끼리 해서 비교 할라니까 안합쳐지네
# a = pd.merge(total_movie,MeMovieR,how="right")






# 남자도 보고 여자도 본 영화
# 여기까지 올 방법이 없네
# a = MeMovieR.index == FeMovieR.index
# print(a)

# 각각 비교해서 영화별로 여자 평균 평점이 높은 영화1







# @@ 남자가 더 좋아하는 영화
# @@ 나이대별 평점의 평균
# @@ 나이대별 성별별 평점의 평균
# @@ 나이대별 평점이 가장 높은 영화