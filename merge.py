import pandas as pd
import glob
import os

def merge_csv(folder, output_name):
    files = glob.glob(os.path.join(folder, "*.csv"))
    print(f"Found {len(files)} files in {folder}")

    dfs = []
    for f in files:
        df = pd.read_csv(f)
        dfs.append(df)

    merged = pd.concat(dfs, ignore_index=True)
    merged.to_csv(output_name, index=False)
    print(f"Saved {output_name} with {len(merged)} rows")
merge_csv("enrolment", "enrolment.csv")
merge_csv("biometric", "biometric.csv")
merge_csv("demographic", "demographic.csv")
