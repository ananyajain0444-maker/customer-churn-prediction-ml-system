from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("models/churn_model.pkl")

@app.get("/")
def home():
    return {"message": "Customer Churn API is running"}

@app.post("/predict")
def predict(data: dict):
    values = np.array(list(data.values())).reshape(1, -1)

    prediction = model.predict(values)[0]
    probability = model.predict_proba(values)[0][1]

    return {
        "churn": int(prediction),
        "probability": float(probability)
    }