import dill
import csv
Eval = dill.load(open("question/Evaluate.pik", 'rb'))
evaluate = dill.load(open("question/eval.pik", 'rb'))
print(int(round(evaluate.score("question/recommendations.csv"), 2)))
#print(90)
