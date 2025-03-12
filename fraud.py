import pandas as pd
import numpy as np
import joblib
import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load trained models
try:
    with open("logistic_model.pkl", "rb") as f:
        logistic_model = pickle.load(f)
    with open("rf_model.pkl", "rb") as f:
        rf_model = pickle.load(f)
    with open("xgb_model.pkl", "rb") as f:
        xgb_model = pickle.load(f)
except Exception as e:
    print(f"Error loading models: {e}")

# Load scaler (if applicable)
try:
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
except Exception as e:
    print(f"Error loading scaler: {e}")
    scaler = None

# Define feature names based on dataset
FEATURE_COLUMNS = [
    "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE",
    "PAY_0", "PAY_2", "PAY_3", "PAY_4", "BILL_AMT4",
    "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2",
    "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract input data from form
        input_data = [float(request.form.get(feature, 0)) for feature in FEATURE_COLUMNS]
        input_array = np.array(input_data).reshape(1, -1)

        # Scale the input if scaler is available
        if scaler:
            input_array = scaler.transform(input_array)

        # Choose model
        model_name = request.form.get("model", "logistic")
        if model_name == "logistic":
            model = logistic_model
        elif model_name == "rf":
            model = rf_model
        elif model_name == "xgb":
            model = xgb_model
        else:
            return jsonify({"error": "Invalid model name"}), 400

        # Make prediction
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[:, 1][0]  # Get fraud probability

        return render_template(
            "predict.html",
            prediction=int(prediction),
            probability=round(float(probability), 2),
        )

    except ValueError:
        return "Please enter valid numerical values."

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
