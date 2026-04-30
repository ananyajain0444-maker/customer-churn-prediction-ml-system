import pandas as pd
import numpy as np

def create_features(df):
    df = df.copy()

    # 📊 Engagement level
    df["engagement_rate"] = df["internet_usage"] / (df["tenure"] + 1)

    # 📞 Support burden
    df["support_intensity"] = df["support_calls"] * df["monthly_charges"]

    # 💰 Price sensitivity
    df["charge_per_usage"] = df["monthly_charges"] / (df["internet_usage"] + 1)

    # ⏳ Risk indicator
    df["high_support_flag"] = (df["support_calls"] > 5).astype(int)

    # 📉 Low usage flag
    df["low_usage_flag"] = (df["internet_usage"] < 20).astype(int)

    return df