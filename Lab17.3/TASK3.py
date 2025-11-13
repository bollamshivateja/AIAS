import pandas as pd, numpy as np, os

# Load from this project folder
paths = [
    "iot_sensor.csv",
    r"C:\\Users\\pooda\\OneDrive\\Desktop\\AIAC\\LAB 17.3\\iot_sensor.csv",
]
path = next((p for p in paths if os.path.exists(p)), None)
if not path:
    raise FileNotFoundError(f"Missing iot_sensor.csv. Checked {paths}; CWD={os.getcwd()}")
df = pd.read_csv(path, encoding="utf-8", encoding_errors="ignore")

# Coerce numeric types
for col in ["temperature", "humidity"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# 1) Forward fill
df = df.ffill()

# 2) Rolling mean (drift removal)
if "temperature" in df.columns:
    df["temperature"] = df["temperature"].rolling(window=5, min_periods=1, center=True).mean()
if "humidity" in df.columns:
    df["humidity"] = df["humidity"].rolling(window=5, min_periods=1, center=True).mean()

# 3) Standard scaling (z-score)
for col in ["temperature", "humidity"]:
    if col in df.columns:
        m = df[col].mean()
        sd = df[col].std(ddof=0)
        df[col + "_scaled"] = (df[col] - m) / (sd if sd not in (0, np.nan) else 1.0)

# 4) Encode sensor IDs
if "sensor_id" in df.columns:
    df["sensor_id_encoded"] = df["sensor_id"].astype("category").cat.codes

# Save to current project folder
out_path = "iot_sensor_preprocessed.csv"
alt_out_path = "iot_updated.csv"
df.to_csv(out_path, index=False)
df.to_csv(alt_out_path, index=False)
print({'csv_written_primary': out_path, 'csv_written_secondary': alt_out_path, 'rows': int(len(df)), 'cols': int(len(df.columns))})