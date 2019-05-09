import pandas as pd
import re

df_1 = pd.read_csv("imdb_test.csv",error_bad_lines=False)
df_2 = pd.read_csv("boxoffice_test.csv",error_bad_lines=False)


# fn,tid,title,wordsInTitle,url,imdbRating,ratingCount,duration,year_x,type,nrOfWins,nrOfNominations,nrOfPhotos,nrOfNewsArticles,nrOfUserReviews,nrOfGenre,Action,Adult,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,FilmNoir,GameShow,History,Horror,Music,Musical,Mystery,News,RealityTV,Romance,SciFi,Short,Sport,TalkShow,Thriller,War,Western,rank,studio,lifetime_gross,year_y
df = pd.DataFrame(columns = ["fn", "tid", "title", "wordsInTitle","url","imdbRating","ratingCount","duration","year_x","type","nrOfWins","nrOfNominations","nrOfPhotos","nrOfNewsArticles","nrOfUserReviews","nrOfGenre","Action","Adult","Adventure","Animation","Biography","Comedy","Crime","Documentary","Drama","Family","Fantasy","FilmNoir","GameShow","History","Horror","Music","Musical","Mystery","News","RealityTV","Romance","SciFi","Short","Sport","TalkShow","Thriller","War","Western","lifetime_gross"]) #创建一个空的dataframe

for i in range(len(df_1['title'])):
    for j in range(len(df_2['title'])):
        title_1 = df_1['title'][i]
        year_1 = int(df_1['year'][i])

        title_2 = df_2['title'][j]
        year_2 = int(df_2['year'][j])

        # print("title 1 = %s, title 2 = %s" %(title_1, title_2))
        if title_1 == title_2:
            print("year 1 = %d, year 2 = %d" %(year_1, year_2))
            if year_1 == year_2:
                print('title ----> %s' % title_2)
                # print('df_1 %s' %df_1[i])
                # print('df_1 %s' % df_2[i])
                df = df.append([df_1['title'].loc[title_1],df_2['lifetime_gross'][j]], ignore_index= True)


#
# result = pd.merge(df_1, df_2, how='inner', on = 'title')
# print(result)

# a=r'\(.*?\)'
# for i in range(len(df_1['title'])):
#     pre = df_1['title'][i]
#     res = re.sub(a, '', pre)
#     df_1['title'][i] = ''.join(list(filter(str.isalpha, res))).lower()
#     # print(i)
#
print(df)
df.to_csv("res.csv",index=False)
# result.to_csv("res.csv",index=False)