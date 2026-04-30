import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

df = pd.DataFrame({
    "tenure": np.random.randint(1, 60, n),
    "monthly_charges": np.random.randint(20, 120, n),
    "support_calls": np.random.randint(0, 10, n),
    "contract_type": np.random.choice([0, 1], n),
    "internet_usage": np.random.randint(1, 100, n)
})

df["churn"] = ((df["contract_type"] == 0) & (df["support_calls"] > 5)).astype(int)

df.to_csv("data/churn_data.csv", index=False)

print("Dataset created successfully!")