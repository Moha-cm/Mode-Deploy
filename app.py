import numpy as np
from flask import Flask, request, jsonify, render_template,redirect,url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def handle_post():
    if request.method == 'POST':
        country= request.form['Country']
        print( country)
        return render_template('index.html', prediction_text='Country $ {}'.format(country))

        
    else:
        return render_template('predict.html')
    
        
        
@app.route('/classify', methods=['GET','POST'])
def classify():
    if request.method == 'POST':
        country= request.form['Country']
        print( country)
        return render_template('index.html', prediction_text='Country $ {}'.format(country))
        
    else:
        return render_template('classification.html')


if __name__ == "__main__":
    app.run(debug=True)

