from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open("crop_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = [
        float(request.form["N"]),
        float(request.form["P"]),
        float(request.form["K"]),
        float(request.form["temperature"]),
        float(request.form["humidity"]),
        float(request.form["ph"])
    ]

    crop = model.predict([data])[0]
    return jsonify({"crop": crop})

if __name__ == "__main__":
    app.run(debug=True)
