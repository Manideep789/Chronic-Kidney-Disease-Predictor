"""
Created on Mon Apr 27 09:05:39 2020

@author: MANIDEEP
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, url_for, request
import sklearn
from sklearn import tree
import numpy as np
import pandas as pd
from statistics import mode
app = Flask(__name__, static_folder='./static/')


dataset = pd.read_csv("/static/kidney_disease.csv")
dataset.drop('id', axis=1, inplace=True)
dataset['rbc'] = dataset['rbc'].fillna(value=dataset['rbc'].mode().iloc[0])
dataset['pc'] = dataset['pc'].fillna(value=dataset['pc'].mode().iloc[0])
dataset['pcc'] = dataset['pcc'].fillna(value=dataset['pcc'].mode().iloc[0])
dataset['ba'] = dataset['ba'].fillna(value=dataset['ba'].mode().iloc[0])
dataset['htn'] = dataset['htn'].fillna(value=dataset['htn'].mode().iloc[0])
dataset['dm'] = dataset['dm'].fillna(value=dataset['dm'].mode().iloc[0])
dataset['cad'] = dataset['cad'].fillna(value=dataset['cad'].mode().iloc[0])
dataset['appet'] = dataset['appet'].fillna(
    value=dataset['appet'].mode().iloc[0])
dataset['pe'] = dataset['pe'].fillna(value=dataset['pe'].mode().iloc[0])
dataset['ane'] = dataset['ane'].fillna(value=dataset['ane'].mode().iloc[0])
dataset['age'] = dataset['age'].fillna(value=dataset['age'].mean())
dataset['bp'] = dataset['bp'].fillna(value=dataset['bp'].mean())
dataset['sg'] = dataset['sg'].fillna(value=dataset['sg'].mean())
dataset['al'] = dataset['al'].fillna(value=dataset['al'].mean())
dataset['su'] = dataset['su'].fillna(value=dataset['su'].mean())
dataset['bgr'] = dataset['bgr'].fillna(value=dataset['bgr'].mean())
dataset['bu'] = dataset['bu'].fillna(value=dataset['bu'].mean())
dataset['sc'] = dataset['sc'].fillna(value=dataset['sc'].mean())
dataset['sod'] = dataset['sod'].fillna(value=dataset['sod'].mean())
dataset['pot'] = dataset['pot'].fillna(value=dataset['pot'].mean())
dataset['hemo'] = dataset['hemo'].fillna(value=dataset['hemo'].mean())
dataset['pcv'] = dataset['pcv'].fillna(value=dataset['pcv'].mode().iloc[0])
dataset['wc'] = dataset['wc'].fillna(value=dataset['wc'].mode().iloc[0])
dataset['rc'] = dataset['rc'].fillna(value=dataset['rc'].mode().iloc[0])
dataset.wc = dataset.wc.replace("\t6200", 6200)
dataset.wc = dataset.wc.replace("\t8400", 8400)
dataset.wc = dataset.wc.replace("\t?", 9800)
dataset.pcv = dataset.pcv.replace("\t43", 43)
dataset.pcv = dataset.pcv.replace("\t?", 41)
dataset.rc = dataset.rc.replace("\t?", 5.2)
dataset.pcv = dataset.pcv.astype(int)
dataset.wc = dataset.wc.astype(int)
dataset.rc = dataset.rc.astype(float)
dataset.classification = dataset.classification.replace('ckd\t', 'ckd')
dataset.classification = [1 if each ==
                          "ckd" else 0 for each in dataset.classification]
dataset.rbc = [1 if each == "abnormal" else 0 for each in dataset.rbc]
dataset.pc = [1 if each == "abnormal" else 0 for each in dataset.pc]
dataset.pcc = [1 if each == "present" else 0 for each in dataset.pcc]
dataset.ba = [1 if each == "present" else 0 for each in dataset.ba]
dataset.pcc = [1 if each == "present" else 0 for each in dataset.pcc]
dataset.htn = [1 if each == "present" else 0 for each in dataset.htn]
dataset.dm = [1 if each == "present" else 0 for each in dataset.dm]
dataset.cad = [1 if each == "present" else 0 for each in dataset.cad]
dataset.appet = [1 if each == "present" else 0 for each in dataset.appet]
dataset.pe = [1 if each == "present" else 0 for each in dataset.pe]
dataset.ane = [1 if each == "present" else 0 for each in dataset.ane]
x = dataset.iloc[:, :24]
y = dataset.iloc[:, 24:]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=1)
dt = DecisionTreeClassifier(criterion='entropy', random_state=0)
dt.fit(x_train, y_train)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/model', methods=['POST', 'GET'])
def runModel():
    data = request.get_json()['fields']
    result = dt.predict([data])
    print(result)
    return str(result).split('[')[1].split(']')[0]


if __name__ == "__main__":
    app.run(debug=True)
