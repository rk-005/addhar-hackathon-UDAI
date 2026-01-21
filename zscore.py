import pandas as pd

df = pd.read_csv("rolling.csv", parse_dates=["date"])

for col in ["bio_rate_5_roll","bio_rate_17_roll","demo_rate_5_roll","demo_rate_17_roll"]:
    mean = df.groupby(["state","district","pincode"])[col].transform("mean")
    std  = df.groupby(["state","district","pincode"])[col].transform("std")
    df[f"{col}_z"] = (df[col] - mean) / std

df.to_csv("anomaly_scores.csv", index=False)
print("Z-scores computed")
