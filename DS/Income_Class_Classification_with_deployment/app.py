import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from code1 import mapToRawTestData
import os

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
dirname = os.path.realpath('..')
path_train = dirname+"/Income_Class_Classification_with_deployment/train.csv"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = request.form
    ref = mapToRawTestData(features,path_train)
    li = ref.mapping()
    li = [int(x) for x in li]
    result = model.predict([np.array(li)])
    msg = ""
    if(result[0] == 1):
       msg = 'Income more than 50k, Financial assistance not required'
    else:
        msg = 'Income less than 50k, Financial assistance required'
    return render_template('index.html', prediction_text=msg)


@app.route('/predict_api',methods=['POST'])
def predict_api():

    #For direct API calls trought request
    data = request.get_json(force=True)
    ref = mapToRawTestData(data,path_train)
    li = ref.mapping()
    li = [int(x) for x in li]
    result = model.predict([np.array(li)])

    msg = ""
    if(result[0] == 1):
       msg = {'msg': 'Income more than 50k, Financial assistance not required'}
    else:
        msg = {'msg': 'Income less than 50k, Financial assistance required'}
    return msg
    #return data

if __name__ == "__main__":
    app.run()















