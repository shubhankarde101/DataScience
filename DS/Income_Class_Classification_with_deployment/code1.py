# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:13:27 2021

@author: SHUBHANKAR
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import os
import pickle

# Setting relative path
dirname = os.path.realpath('..')

# Initializing label encoder
le = LabelEncoder()

#path set
path_train = dirname+"/Income_Class_Classification_with_deployment/train.csv"
path_test = dirname+"/Income_Class_Classification_with_deployment/test.csv"
path_test_outcome = dirname+"/Income_Class_Classification_with_deployment/outcome.csv"

# Function definition
def frequency_encoding(colname,df):
    map1 = df[colname].value_counts()/len(df[colname])
    map2=map1.to_dict()
    df[colname]=df[colname].map(map2)

def frequency_encoding_test(colname,df):

    df_train_main = pd.read_csv(path_train)
    df_train_main[colname] = df_train_main.fillna('Others')[colname]
    map1_train = df_train_main[colname].unique()
    map1_test =  df[colname].unique()
    colToDrop = list(list(set(map1_train)-set(map1_test)) + list(set(map1_test)-set(map1_train)))
    print('------------------------'+str(colToDrop[0])+'-----------------------------')
    if(str(colToDrop[0]) not in 'nan'):
        map1 = df_train_main[colname].value_counts()/len(df_train_main[colname])
        print(colToDrop)
        for i in range(0,len(colToDrop)):
            map1[map1.index!=colToDrop[i]]
        map2=map1.to_dict()
        df[colname]=df[colname].map(map2)

    else:
      map1 = df_train_main[colname].value_counts()/len(df_train_main[colname])
      map2=map1.to_dict()
      df[colname]=df[colname].map(map2)



def mean_encoding(colname, target,df):
    mean_encode = df.groupby(colname)[target].mean()
    df[colname]=df[colname].map(mean_encode)


def label_encoding(colname, df):
    df[colname] = le.fit_transform(df[colname])


def one_hot_encoding(colname,prefix, df):
    df = pd.get_dummies(df, prefix = [prefix], columns = [colname])
    return df

# Start
df_train = pd.read_csv(path_train)
df_train.info()
df_train.describe()
columnsToExclude = ['workclass']
for feature in df_train.columns[:]:
    print(feature,":",len(df_train[feature].unique()),'labels')
df_train = df_train.drop(columns = columnsToExclude, axis=1)
df_train.info()

# Pre-Processing Training Data
df_train = one_hot_encoding('education','edu', df_train)
df_train['occupation'] = df_train.fillna('Others')['occupation']
frequency_encoding('occupation',df_train)
df_train['native-country'] = df_train.fillna('Others')['native-country']
frequency_encoding('native-country',df_train)
label_encoding('gender',df_train)
label_encoding('race',df_train)
label_encoding('relationship',df_train)
label_encoding('marital-status',df_train)
df_train.info()
pd.set_option('display.max_columns', None)
df_train.head(10)
df_y_train = df_train['income_>50K']
df_x_train = df_train.drop(columns = ['income_>50K'],axis=1)
df_x_train.info()

# Preprocessing- Test Data
df_test = pd.read_csv(path_test)
df_test.info()
df_test = df_test.drop(columns = columnsToExclude, axis=1)
df_test = one_hot_encoding('education','edu',df_test)
frequency_encoding_test('native-country',df_test)
frequency_encoding_test('occupation',df_test)
label_encoding('gender',df_test)
label_encoding('race',df_test)
label_encoding('relationship',df_test)
label_encoding('marital-status',df_test)
#df_test.to_csv('test.csv')

# Training
lr =  LogisticRegression(random_state = 0)
lr.fit(df_x_train,df_y_train)
lr.score(df_x_train,df_y_train)


# Testing and Accuracy calculation
df_y_pred= lr.predict(df_test)
#df_y_pred = pd.DataFrame(df_y_pred, columns = ['outcome']).reset_index()
#df_y_pred.rename(columns = {'index':'id,'}, inplace = True)
#df_y_pred['id,']=df_y_pred['id,'].apply(lambda x: str(x)+',')
#df_y_pred.to_csv('outcome.csv',index=False)
df_y_test = pd.read_csv(path_test_outcome)
df_y_test = df_y_test['outcome']
conf=confusion_matrix(df_y_test,df_y_pred)
print(conf)
accuracy=accuracy_score(df_y_test,df_y_pred)
print("Accuracy is: ")
print(accuracy*100)

# Saving model to disk
pickle.dump(lr, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
result = model.predict([[48,	212954,	14,	2,	0.131256952,	0,	4,	1,	15024,	0,	40,	0.911012236,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0]])
if(result[0] == 1):
    print('Income more than 50k, Financial assistance not required')
else:
    print('Income less than 50k, Financial assistance required')

# Mapping to Raw Test Data for Single Prediction through API

class mapToRawTestData():

    def __init__(self, dic, path_train):

           self.dic = dic
           self.df_train_main = pd.read_csv(path_train)



    def map_label_col(self,col):


        self.df_train_main[col] = self.df_train_main.fillna('Others')[col]
        index = self.df_train_main[self.df_train_main[col]==self.dic[col]].index
        label_encoding(col,self.df_train_main)
        return self.df_train_main[col].loc[index[0]]

    def map_frequency_col(self,col):


        self.df_train_main[col] = self.df_train_main.fillna('Others')[col]
        index = self.df_train_main[self.df_train_main[col]==self.dic[col]].index
        frequency_encoding(col,self.df_train_main)
        return self.df_train_main[col].loc[index[0]]

    def onehot_mapping_col(self,col):

        self.df_train_main = one_hot_encoding('education','edu',self.df_train_main)
        index = self.df_train_main[self.df_train_main[col]==1].index
        x = list(self.df_train_main.iloc[index[0]][14::1])
        return x


    def mapping(self):

        li = []
        li.append(self.dic['age'])
        li.append(self.dic['fnlwgt'])
        li.append(self.dic['educational-num'])
        li.append( mapToRawTestData.map_label_col(self,'marital-status'))
        li.append( mapToRawTestData.map_label_col(self,'occupation'))
        li.append( mapToRawTestData.map_label_col(self,'relationship'))
        li.append( mapToRawTestData.map_label_col(self,'race'))
        li.append( mapToRawTestData.map_label_col(self,'gender'))
        li.append( self.dic['capital-gain'])
        li.append( self.dic['capital-loss'])
        li.append( self.dic['hours-per-week'])
        li.append( mapToRawTestData.map_label_col(self,'native-country'))
        list_rel = mapToRawTestData.onehot_mapping_col(self,self.dic['education'])
        for i in list_rel:
            li.append(i)


        return li

'''di = {"age":"27","capital-gain":"44","capital-loss":"89","education":"edu_9th","educational-num":"17","fnlwgt":"89898","gender":"Female","hours-per-week":"89","marital-status":"Married-civ-spouse","native-country":"India","occupation":"Sales","race":"Asian-Pac-Islander","relationship":"Wife"}
x = mapToRawTestData(di,path_train)
li = x.mapping()
li = [int(x) for x in li]
result = model.predict([np.array(li)])'''













