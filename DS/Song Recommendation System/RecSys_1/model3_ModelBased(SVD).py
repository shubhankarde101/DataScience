# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:42:54 2020

@author: SHUBHANKAR
"""


import warnings

warnings.simplefilter(action = 'ignore', category=FutureWarning)
warnings.filterwarnings('ignore')
def ignore_warn(*args, **kwargs):
    pass

warnings.warn = ignore_warn #ignore annoying warning (from sklearn and seaborn)

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

from scipy.sparse import coo_matrix
import math as mt

from scipy.sparse.linalg import svds
from scipy.sparse import csc_matrix




import seaborn as sns
sns.set(style="ticks", color_codes=True, font_scale=1.5)
color = sns.color_palette()
sns.set_style('darkgrid')



def compute_svd(urm, K):
    U, s, Vt = svds(urm, K)

    dim = (len(s), len(s))
    S = np.zeros(dim, dtype=np.float32)
    for i in range(0, len(s)):
        S[i,i] = mt.sqrt(s[i])

    U = csc_matrix(U, dtype=np.float32)
    S = csc_matrix(S, dtype=np.float32)
    Vt = csc_matrix(Vt, dtype=np.float32)

    return U, S, Vt

def compute_estimated_matrix(urm, U, S, Vt, uTest, K, test):
    rightTerm = S*Vt
    max_recommendation = 250
    estimatedRatings = np.zeros(shape=(MAX_UID, MAX_PID), dtype=np.float16)
    recomendRatings = np.zeros(shape=(MAX_UID,max_recommendation ), dtype=np.float16)
    for userTest in uTest:
        prod = U[userTest, :]*rightTerm
        estimatedRatings[userTest, :] = prod.todense()
        recomendRatings[userTest, :] = (-estimatedRatings[userTest, :]).argsort()[:max_recommendation]
    return recomendRatings

buff_song = []


def show_recomendations(uTest, user_given, num_recomendations = 10):
    for user in uTest:
        print('-'*70)
        print("Recommendation for user id {}".format(user))
        rank_value = 1
        i = 0
        final_similar_songs = []
        while (rank_value <  num_recomendations + 1):
            so = uTest_recommended_items[user,i:i+1][0]
            if (small_set.user_id[(small_set.so_index_value == so) & (small_set.us_index_value == user)].count()==0):
                song_details = small_set[(small_set.so_index_value == so)].\
                    drop_duplicates('so_index_value')[['title','artist_name','song_id']]
                print("The number {} recommended song is {} BY {} with id {}".format(rank_value,
                                                                      list(song_details['title'])[0],
                                                                      list(song_details['artist_name'])[0],
                                                                      list(song_details['song_id'])[0]

                                                                      )

    ),

                final_similar_songs.append(list(song_details['song_id'])[0])
                rank_value+=1
            i += 1
        buff_song.append([user_given, [j for j in final_similar_songs]])


############-----Starting Point----###########

user_song_list_count = pd.read_csv('C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DataScience/DS/Recommendation System/RecSys_1/train.csv')
user_song_list_count['song'] = user_song_list_count['title'].map(str) + " - " + user_song_list_count['artist_name']


user_song_list_count.info()
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(user_song_list_count.listen_count,bins = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.show
#user_song_list_count = user_song_list_count.loc[user_song_list_count['listen_count']<=13]

user_song_list_listen = user_song_list_count[['user_id','listen_count']].groupby('user_id').sum().reset_index()
user_song_list_listen.info()
user_song_list_listen.rename(columns={'listen_count':'total_listen_count'},inplace=True)



user_song_list_count_merged = pd.merge(user_song_list_count,user_song_list_listen)



user_song_list_count_merged['fractional_play_count'] =  user_song_list_count_merged['listen_count']/user_song_list_count_merged['total_listen_count']
user_song_list_count_merged.info()



user_codes = user_song_list_count_merged.user_id.drop_duplicates().reset_index()
user_codes.rename(columns={'index':'user_index'}, inplace=True)
user_codes['us_index_value'] = list(user_codes.index)
user_codes.info()

song_codes = user_song_list_count_merged.song_id.drop_duplicates().reset_index()
song_codes.rename(columns={'index':'song_index'}, inplace=True)
song_codes['so_index_value'] = list(song_codes.index)

small_set = pd.merge(user_song_list_count_merged,song_codes,how='left')
small_set = pd.merge(small_set,user_codes,how='left')

small_set.info()


mat_candidate = small_set[['us_index_value','so_index_value','fractional_play_count']]
max(mat_candidate['so_index_value'])

data_array = mat_candidate.fractional_play_count.values
row_array = mat_candidate.us_index_value.values
col_array = mat_candidate.so_index_value.values

data_sparse = coo_matrix((data_array, (row_array, col_array)),dtype=float)



print('User used to performed the item similarity based recommendations earlie:.')

K=25
urm = data_sparse
MAX_PID = urm.shape[1]
MAX_UID = urm.shape[0]

U, S, Vt = compute_svd(urm, K)


df_test = pd.read_csv('C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DataScience/DS/Recommendation System/RecSys_1/test_local.csv',header=None)
df_test.columns = ['user_id']

for i in df_test['user_id']:
    uTest = []
    x = small_set[small_set['user_id']==i]['us_index_value'].unique()[0]
    uTest.append(x)
    #uTest = ['4,5,6,7,8,23']
    uTest_recommended_items = compute_estimated_matrix(urm, U, S, Vt, uTest, K, True)
    show_recomendations(uTest,i)

z = pd.DataFrame(buff_song,columns = ['userId','Songs'])
b = z.set_index('userId')
b.to_csv('file1.csv')


















































