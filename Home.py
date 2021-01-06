#Flask imports
import flask as fl
from flask import redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#Import ScikitLearn
from sklearn.preprocessing import StandardScaler
import joblib

#Import tensorflow
import tensorflow.keras as k
from tensorflow.keras.layers import Dense

#Basic Imports
import numpy as np
import pandas as pd
import os
from flask.templating import render_template


app = fl.Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def result():
  if request.method == 'POST':
    #Recieve the Data from the flask application
    speed = request.form['speed']

    #Format the speed to a float32
    speed = np.float32(speed)

    #Pass the data into getSpeedPrediction
    power = getSpeedPrediction(speed)

    power = np.round_(power, 2)
    power = power[0][0]
    
    return render_template('Index.html', output=power)
   
  if request.method == 'GET':
    return render_template('Index.html', output = "...")

def getSpeedPrediction(x):   
    #Add to numpy array
    x = np.array([[x]])
    #Reshape x using (-1, 1) as its a single feature
    x = np.reshape(x, (-1, 1))
    value = speedPrediction(x)
    return(value)

def speedPrediction(x):
    #Get the model
    model = k.models.load_model("model.h")
    #Get the scaler
    scaler = joblib.load("scaler.save")
    x = scaler.transform(x)
    value = model.predict(x)

    return(value)

if __name__ == '__main__':
    app.run(debug = True)