from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# numeric columns (based on your dataset)
NUM_FEATURES = [
    "tenure",
    "monthly_charges",
    "support_calls",
    "internet_usage",
    "engagement_rate",
    "support_intensity",
    "charge_per_usage"
]

def get_preprocessor():

    numeric_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_pipeline, NUM_FEATURES)
    ])

    return preprocessor