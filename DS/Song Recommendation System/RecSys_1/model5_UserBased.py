# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:04:54 2020

@author: SHUBHANKAR
"""

import pandas as pd
import numpy as np
from itertools import chain
from matplotlib import pyplot as plt

user_song_list_count = pd.read_csv('C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DataScience/DS/Recommendation System/RecSys_1/train.csv')
user_song_list_count['song'] = user_song_list_count['title'].map(str) + " - " + user_song_list_count['artist_name']
user_song_list_count.info()

fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(user_song_list_count.listen_count,bins = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.show

#user_song_list_count = user_song_list_count.loc[(user_song_list_count['listen_count']<13) & (user_song_list_count['listen_count']>1)]
user_song_list_count = user_song_list_count.loc[(user_song_list_count['listen_count']<13)]

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

def get_user_items(user):
        user_data = small_set[small_set['user_id'] == user]
        user_items = list(user_data['song_id'].unique())
        return user_items


def get_item_count(song):
        item_data = small_set[small_set['song_id'] == song]
        totalcount = len(item_data['user_id'].unique())
        return totalcount


def intersection(l1, l2) :
    # Find the intersection of the two sets
    intersect = set(l1).intersection(set(l2))
    return intersect

def jaccard_index(l1, l2) :

    # Sizes of both the sets
    size_s1 = len(set(l1));
    size_s2 = len(set(l2));

    # Get the intersection set
    intersect = intersection(l1, l2);

    # Size of the intersection set
    size_in = len(intersect);

    # Calculate the Jaccard index
    # using the formula
    jaccard_in = size_in  / (size_s1 + size_s2 - size_in);
    # Return the Jaccard index
    return round(jaccard_in,6);


def construct_cooccurence_matrixa(all_users,given_user):

     cooccurence_matrix = np.matrix(np.zeros(shape=(1, len(all_users))), float)

     user_songs_For_Given_User = get_user_items(given_user)

     for i in range(0,len(all_users)):

          user_songs_iterate = get_user_items(all_users['user_id'][i])
          cooccurence_matrix[0,i] = jaccard_index(user_songs_For_Given_User,user_songs_iterate)
          #print("Jacard Index for user {} and {} is {}".format(given_user,all_users['user_id'][i],cooccurence_matrix[0,i]))

     return cooccurence_matrix


def top_n_similar_users(co_occ,givenuser,n=3):

     user_arr_reshaped = co_occ.reshape(-1,1)
     user_arr_df = pd.DataFrame(user_arr_reshaped, columns=['jacard_index'])
     user_arr_df_top_n = user_arr_df[user_arr_df['jacard_index']>0]
     user_arr_df_top_n =user_arr_df.sort_values('jacard_index',ascending=False).head(n)
     index = allusers[allusers['user_id']==givenuser].index
     user_arr_df_top_n_index=[indx for indx in user_arr_df_top_n.index if indx!=index]
     sim_users = {}
     index_li = list(user_arr_df_top_n_index)
     for i in index_li:
       user = allusers.iloc[i]['user_id']
       sim_users[user]=user_arr_df_top_n['jacard_index'].loc[i]
     return sim_users

def set_Diff(li1, li2):
    si1 = list(set(li1))
    si2 = list(set(li2))
    si_dif = [i for i in si1 + si2 if i in si2  and i not in si1]
    return si_dif

def Recommended_songs(user,simusers):

    recommended_songs = []
    for i in simusers.keys():
      user_songs_For_Given_User = get_user_items(user)
      user_songs_For_iterator = get_user_items(i)
      recommended_songs.append(set_Diff(user_songs_For_Given_User,user_songs_For_iterator))
    recommended_song_merged = list(map(str,chain.from_iterable(recommended_songs)))
    count = [get_item_count(x) for x in recommended_song_merged]
    dic = {'Song':recommended_song_merged,'Total_Listen_Count':count}
    count_df = pd.DataFrame(dic)
    count_df_sorted = count_df.sort_values('Total_Listen_Count',ascending=False)
    count_df_sorted = count_df_sorted[count_df_sorted['Total_Listen_Count']>1].head(10)
    return list(count_df_sorted['Song'])


allusers = user_song_list_count_merged.user_id.drop_duplicates().reset_index()
allusers.drop(columns={'index'},inplace=True)


df_test = pd.read_csv('C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DataScience/DS/Recommendation System/RecSys_1/test_local.csv',header=None)
df_test.columns = ['user_id']

buff_song = []
for i in df_test['user_id']:

   user_input = i
   print("-----------------Test User {}--------------------".format(i))
   co_occ_m = construct_cooccurence_matrixa(allusers,user_input)
   similar_users = top_n_similar_users(co_occ_m,user_input)
   print("------------------------**Similar Users**--------------------------------------------")
   print(similar_users)
   recSys=Recommended_songs(user_input,similar_users)
   print("------------------------**Recommended Songs**--------------------------------------------")
   print(recSys)
   buff_song.append([i, [j for j in recSys]])

z = pd.DataFrame(buff_song,columns = ['userId','Songs'])
b = z.set_index('userId')
b.to_csv('file1.csv')






