import pandas as pd

df = pd.read_csv("rates.csv", parse_dates=["date"])

df = df.sort_values(["state","district","pincode","date"])

for col in ["bio_rate_5","bio_rate_17","demo_rate_5","demo_rate_17"]:
    df[f"{col}_roll"] = (
        df.groupby(["state","district","pincode"])[col]
          .transform(lambda x: x.rolling(7, min_periods=3).mean())
    )

df.to_csv("rolling.csv", index=False)
print("Rolling averages done")
