import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template,redirect,url_for
import pickle

app = Flask(__name__)
sp_model = pickle.load(open('sp_model.pkl', 'rb'))
st_model = pickle.load(open('st_model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def handle_post():
    if request.method == 'POST':
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]
        output = sp_model.predict(final_features)
        output = sp_model.predict(final_features)[0]
        return render_template('index.html', page_name="Copper Selling Price", result=request.form, prediction_text=f'Selling Price should be {output:.2f}')
       
    else:
        return render_template('predict.html')



@app.route('/classify', methods=['GET','POST'])
def classify():
    if request.method == 'POST':
        
        country = request.form.get('Country') 
        Item_Type= request.form.get('Item_Type')
        Application= request.form.get('Application')
        Material= request.form.get('Material')
        Item_Year= request.form.get('Item-Year')
    
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]
        print(final_features)
        output = st_model.predict(final_features)
        result = ""
        if output == 0:
            result = "LOST"
        else:
            result = "WIN"
                    
        return render_template('index.html',page_name="Status Classification",result=request.form,prediction_text='Status should be  {}'.format(result))
    else:
        return render_template('classification.html')

if __name__ == "__main__":
    app.run(debug=True)

