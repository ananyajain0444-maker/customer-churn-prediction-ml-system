import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/churn_data.csv")

# 1️⃣ Churn Distribution
plt.figure()
sns.countplot(x="churn", data=df)
plt.title("Churn Distribution")
plt.savefig("outputs/churn_distribution.png")
plt.close()

# 2️⃣ Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Feature Correlation")
plt.savefig("outputs/feature_correlation.png")
plt.close()

# 3️⃣ Monthly Charges vs Churn
plt.figure()
sns.boxplot(x="churn", y="monthly_charges", data=df)
plt.title("Charges vs Churn")
plt.savefig("outputs/charges_vs_churn.png")
plt.close()

# 4️⃣ Support Calls vs Churn
plt.figure()
sns.boxplot(x="churn", y="support_calls", data=df)
plt.title("Support Calls vs Churn")
plt.savefig("outputs/support_calls.png")
plt.close()

print("✅ All images generated successfully!")