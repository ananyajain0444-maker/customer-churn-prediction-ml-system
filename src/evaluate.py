import pandas as pd
import joblib
from sklearn.metrics import classification_report

df = pd.read_csv("data/churn_data.csv")

X = df.drop("churn", axis=1)
y = df["churn"]

model = joblib.load("models/churn_model.pkl")

pred = model.predict(X)

print(classification_report(y, pred))