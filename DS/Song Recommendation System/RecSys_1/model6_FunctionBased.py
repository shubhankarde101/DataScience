# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:58:57 2021

@author: SHUBHANKAR
"""
import pandas as pd


df=pd.read_csv("C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DS_Git/DS/Song Recommendation System/RecSys_1/train.csv")
rec=pd.read_csv("C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DS_Git/DS/Song Recommendation System/RecSys_1/recommendations.csv",names=['user_id'])

table1=df.pivot_table(index='user_id',columns='song_id',values='listen_count')

TableB = table1.corr(method='pearson')

user_corr=pd.Series()
recomend={}

user_ids=[x for x in rec['user_id']]
user_ids

def recomendationDict(user_corr,user):
    recomendSongs=[]
    #print(user_corr)
    #print(user)
    for songs in user_corr.sort_values(ascending=False).index[:10]:
        recomendSongs.append(songs)
    recomend[user]=recomendSongs
    return recomend

for user_id in user_ids:
    user_corr=pd.Series()

    for song in table1.loc[user_id].dropna().index:
        corr_list=TableB[song].dropna()*table1.loc[user_id][song]
        user_corr=user_corr.append(corr_list)
    #print(user_corr)

    user_corr=user_corr.groupby(user_corr.index).sum()
    user_corr.sort_values(ascending=False)

    songlistUnHeard=[]
    for each in range(len(table1.loc[user_id].dropna().index)):
        if table1.loc[user_id].dropna().index[each] in user_corr:
            songlistUnHeard.append(table1.loc[user_id].dropna().index[each])
    if len(user_corr)>1:
        user_corr=user_corr.drop(songlistUnHeard)
    else:
        pass
    recomendationDict(user_corr,user_id)

    #print("The list of songs that user {} has listened".format(table1.index[user_id]))
    #for songs in table1.iloc[user_id].dropna().index:
        #print(songs)

table1.loc['2151970107e08d58919003899f952b64af0ee0ec'].dropna()
TableB['SOZZWZV12A67AE140F'].dropna()
print(recomend['2151970107e08d58919003899f952b64af0ee0ec'])


















