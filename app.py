from flask import Flask, render_template, request 
import os
import numpy as np 
import pandas as pd
from CarPrediction.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Completed"

@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            fixed_acidity = request.form['fixed_acidity']
            volatile_acidity = request.form['volatile_acidity']
            citric_acid = request.form['citric_acid']
            residual_sugar =request.form['residual_sugar']
            chlorides =request.form['chlorides']

            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides]
            data = np.array(data).reshape(1,5)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))
        
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
