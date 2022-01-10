import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__) #Initialize the flask App
model = joblib.load("model.pkl")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fordbuy')
def fordbuy():
    return render_template('fordbuy.html')

@app.route('/fordsell')
def fordsell():
    return render_template('fordsell.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
@app.route('/sejarah')
def sejarah():
    return render_template('sejarah.html')

@app.route('/tim')
def tim():
    return render_template('tim.html')
    


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #convert the features into float type
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('fordsell.html', prediction_text='Prediksi Harga Penjualan : ${}'.format(output))





if __name__ == "__main__":
    app.run(debug=True)