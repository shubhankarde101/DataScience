# -*- coding: utf-8 -*-
"""
@author: SHUBHANKAR
"""
import pandas as pd


df_train = pd.read_csv('C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DataScience/DS/Recommendation System/RecSys_1/train.csv')
df_train.head()
df_train.info()
df_test = pd.read_csv('C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DataScience/DS/Recommendation System/RecSys_1/test_local.csv',header=None)
df_test.columns = ['user_id']


ratings_pivot = df_train.pivot(index='user_id', columns='song_id',values='listen_count').fillna(0)

def add_to_dict(df,di):

    for i in list(df.index):

        if i in di:
            if di[i]>=df.loc[i]['Correlation']:
                 pass
            else:
               di[i]= df.loc[i]['Correlation']
        else:
          di[i]= df.loc[i]['Correlation']


transactions = []
for k in df_test['user_id']:

    user_songs_row = df_train[df_train['user_id']==k]
    user_songs = user_songs_row.sort_values('listen_count',ascending=False)
    user_songs = pd.DataFrame(user_songs['song_id']).reset_index(drop=True)
    user_songs.columns = ['song_selected_for_particular_user']
    user_songs.info()
    print('user is----------------------- {}'.format(k))
    di = {}

    for i in user_songs['song_selected_for_particular_user']:

        slctd_song = i
        All_Users_for_song = ratings_pivot[slctd_song]
        corr_songs = ratings_pivot.corrwith(All_Users_for_song)
        similar_to_songs = pd.DataFrame(corr_songs,columns=['Correlation'])
        similar_to_songs.dropna(inplace=True)
        similar_to_songs = similar_to_songs.drop(slctd_song).sort_values('Correlation',ascending=False)
        #similar_to_songs1 = similar_to_songs[similar_to_songs['Correlation']]
        add_to_dict(similar_to_songs,di)

    final = pd.DataFrame(columns = ['song_id','corr_val'])
    final['song_id']=di.keys()
    final['corr_val']=di.values()
    final
    user_songs
    final.info()
    user_songs.info()

    for i in final['song_id']:
        if str(i) in str(user_songs_row['song_id']):
             index = final[final['song_id']==i].index
             final = final.drop(index)


    final_similar_songs = final.sort_values('corr_val',ascending=False).head(10)
    print('---Similar songs are:----')
    print(final_similar_songs)
    transactions.append([k, [j for j in final_similar_songs['song_id']]])

z = pd.DataFrame(transactions,columns = ['userId','Songs'])
b = z.set_index('userId')
b.to_csv('file1.csv')




























