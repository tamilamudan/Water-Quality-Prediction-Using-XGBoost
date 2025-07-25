from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("Wqp_model.pkl", "rb") as f:
    data = pickle.load(f)
    model = data["model"]
    scaler = data["Scaler"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        feature_names = [
            "ph", "hardness", "solids", "chloramines", "sulfate",
            "conductivity", "organic_carbon", "trihalomethanes", "turbidity"
        ]
        features = [float(request.form.get(name)) for name in feature_names]
        input_array = np.array([features])
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]
        if prediction == 1:
            result = "💧 Safe to Drink"
        else:
            result = "🚫 Not Safe to Drink"
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
