import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={"age":"27","capital-gain":"44","capital-loss":"89","education":"edu_9th","educational-num":"17","fnlwgt":"89898","gender":"Female","hours-per-week":"89","marital-status":"Married-civ-spouse","native-country":"India","occupation":"Sales","race":"Asian-Pac-Islander","relationship":"Wife"})
print(r.json())