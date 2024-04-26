import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template,redirect,url_for
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def handle_post():
    if request.method == 'POST':
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]
        output = model.predict(final_features)
        output = model.predict(final_features)[0]
        return render_template('index.html', page_name=" Resale Flat Price", result=request.form, prediction_text=f'Rescale Price should be {output:.2f}')
       
    else:
        return render_template('predict.html')


if __name__ == "__main__":
    app.run(debug=True)

