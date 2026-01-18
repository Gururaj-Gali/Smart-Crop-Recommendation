import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset
data = {
    "N": [90, 40, 20, 80, 60],
    "P": [40, 60, 80, 20, 30],
    "K": [40, 20, 30, 60, 50],
    "temperature": [20, 25, 30, 22, 24],
    "humidity": [80, 60, 70, 75, 65],
    "ph": [6.5, 7.0, 6.0, 6.8, 7.2],
    "crop": ["Rice", "Maize", "Cotton", "Wheat", "Sugarcane"]
}

df = pd.DataFrame(data)

X = df.drop("crop", axis=1)
y = df["crop"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("crop_model.pkl", "wb"))
print("Crop recommendation model saved")
