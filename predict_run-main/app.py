from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("ipl_individual.pickle")

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for predicting runs
@app.route('/predict_run', methods=['POST'])
def predict_run():
    # Get the input values from the form
    player = request.form['PLAYER']
    avg = float(request.form['Avg'])
    bf = int(request.form['BF'])
    sr = float(request.form['SR'])
    fours = int(request.form['Fours'])
    six = int(request.form['Six'])

    # Assume the model expects 104 features
    # Create a feature array with default values for missing features
    features = np.zeros(104)  # Create an array of zeros with length 104

    # Assign values to the features that you have
    features[0] = avg
    features[1] = bf
    features[2] = sr
    features[3] = fours
    features[4] = six

    # Make predictions
    prediction = model.predict(features.reshape(1, -1))  # Reshape the features array to be 2D

    # Render predict.html template and pass the prediction result
    return render_template('predict.html', player=player, prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
