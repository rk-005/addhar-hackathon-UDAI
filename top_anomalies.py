import pandas as pd

df = pd.read_csv("anomaly_scores.csv")

df["max_z"] = df[
    ["bio_rate_5_roll_z","bio_rate_17_roll_z","demo_rate_5_roll_z","demo_rate_17_roll_z"]
].max(axis=1)

top = (
    df.groupby(["state","district","pincode"])["max_z"]
      .max()
      .reset_index()
      .sort_values("max_z", ascending=False)
      .head(50)
)

top.to_csv("top_50_anomalous_pincodes.csv", index=False)
print("Top 50 anomalies saved")
