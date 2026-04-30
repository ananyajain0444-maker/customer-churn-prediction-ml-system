# 📌 Customer Churn Prediction System

## 🧠 Project Overview
This project is an end-to-end Machine Learning system that predicts whether a customer is likely to churn based on behavioral, billing, and engagement data. It also provides business insights to help companies improve customer retention and reduce revenue loss.

The system includes:
- Data preprocessing & feature engineering  
- Machine learning model training (classification)  
- Model evaluation & visualization  
- FastAPI-based prediction API  
- Business-ready outputs for retention strategies  

---

## 🎯 Problem Statement
Customer churn is one of the biggest challenges in subscription-based businesses like:
- Telecom
- SaaS platforms
- OTT services
- Fintech apps

Losing customers directly impacts revenue. This project helps identify customers at risk of churning before they leave.

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn
- FastAPI
- Uvicorn
- Joblib

---

## 📊 Project Workflow
Data Collection → Data Cleaning → Feature Engineering → Model Training → Evaluation → API Deployment → Insights

---

## 📁 Project Structure
Customer-Churn-Prediction/
│
├── api/                  # FastAPI backend  
├── data/                 # Dataset  
├── models/               # Trained model  
├── notebooks/            # EDA & training notebooks  
├── outputs/              # Evaluation plots  
├── src/                  # Core ML pipeline code  
├── main.py               # Entry point  
├── requirements.txt      # Dependencies  
└── README.md  

---

## 🚀 How to Run the Project

### 1️⃣ Create Virtual Environment
python -m venv venv  
venv\Scripts\activate   # Windows  

### 2️⃣ Install Dependencies
pip install -r requirements.txt  

### 3️⃣ Run FastAPI Server
uvicorn api.main:app --reload  

---

## 📡 API Endpoints

### Predict Churn
POST /predict  

### Input Example
{
  "tenure": 12,
  "monthly_charges": 70,
  "total_charges": 900,
  "contract": "Month-to-month"
}

### Output Example
{
  "churn_probability": 0.82,
  "prediction": "Churn"
}

---

## 📊 Model Performance
- Accuracy: ~85–90%
- Optimized for recall on churn class
- Metrics used:
  - Confusion Matrix
  - ROC Curve
  - Feature Importance

---

## 📈 Business Impact
- Identify high-risk customers early  
- Reduce churn rate  
- Improve retention strategies  
- Increase revenue stability  

---

## 🧾 Key Features
- End-to-end ML pipeline  
- Automated feature engineering  
- REST API for predictions  
- Visual analytics  
- Business insights generation  

---

## 🧠 Future Improvements
- Deploy on cloud (AWS / Render / Azure)  
- Add Streamlit dashboard  
- SHAP explainability  
- Real-time prediction system  
- Database integration  

---

## 👨‍💻 Author
Ananya Jain  
---
