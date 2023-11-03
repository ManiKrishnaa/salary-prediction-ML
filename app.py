import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html', prediction='')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        experience = float(request.form['experience'])
        education_level = request.form.get('education_level')
        gender = request.form.get('gender')

        bachelors = 0
        masters = 0
        phd = 0
        male = 0
        female = 0
        if gender == 'Male':
            male = 1
        if gender == 'Female':
            female = 1
        if education_level == 'Bachelors':
            bachelors = 1
        if education_level == 'Masters':
            masters = 1
        if education_level == 'Phd':
            phd = 1

        input_data = np.array([[age,experience,female,male,bachelors,masters,phd]])
        print(input_data)
        prediction = model.predict(input_data)

        return render_template('index.html', prediction=f'{prediction[0]}')
    except Exception as e:
        return render_template('index.html', prediction='Error: Invalid input data')

if __name__ == '__main__':
    app.run(debug=True)
