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
        customer= request.form['Customer']
        country= request.form['Country']
        print(customer, country)
        return render_template('index.html', customer=customer, country=country)

        
    else:
        return render_template('predict.html')
    
        
        
@app.route("/<cus>")
def user(Cus):
    return f"<h1>{Cus}</h1>"        


@app.route('/classify', methods=['GET','POST'])
def classify():
    if request.method == 'POST':
        customer= request.form['Customer']
        country= request.form['Country']
        print(customer, country)
    else:
        return render_template('classification.html')


if __name__ == "__main__":
    app.run(debug=True)

