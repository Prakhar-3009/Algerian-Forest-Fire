from flask import Flask, request,jsonify,render_template
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle

application = Flask(__name__)
app = application

linear_model = pickle.load(open("MODELS/model.pkl","rb"))
Sc = pickle.load(open("MODELS/Scaler.pkl","rb"))


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictdata',methods=['GET','POST'])
def predict_data():
    if request.method=='POST':
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))

        new_data = Sc.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        results = linear_model.predict(new_data)

        return render_template('result.html',results=results[0])
    
    else:
        return render_template("home.html")

if __name__ == '__main__':
    app.run()
