import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Task.pd.py
# Generate a synthetic healthcare dataset, impute missing values with column medians,
# and normalize numeric columns using Min-Max scaling.


np.random.seed(42)

# 1) Generate synthetic healthcare dataset
n_samples = 200
data = {
    "age": np.random.randint(20, 90, size=n_samples),
    "systolic_bp": np.random.normal(loc=125, scale=15, size=n_samples).round(0),
    "diastolic_bp": np.random.normal(loc=80, scale=10, size=n_samples).round(0),
    "cholesterol": np.random.normal(loc=200, scale=30, size=n_samples).round(0),
    "glucose": np.random.normal(loc=110, scale=25, size=n_samples).round(0),
    "gender": np.random.choice(["M", "F"], size=n_samples),
    "smoker": np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2]),
}
df = pd.DataFrame(data)

# Clip physiological values to realistic ranges
df["systolic_bp"] = df["systolic_bp"].clip(80, 200)
df["diastolic_bp"] = df["diastolic_bp"].clip(40, 140)
df["cholesterol"] = df["cholesterol"].clip(100, 400)
df["glucose"] = df["glucose"].clip(40, 400)

# 2) Introduce missing values randomly (~10% per numeric column)
numeric_cols = ["age", "systolic_bp", "diastolic_bp", "cholesterol", "glucose"]
for col in numeric_cols:
    mask = np.random.rand(n_samples) < 0.10  # 10% missing
    df.loc[mask, col] = np.nan

# Display missing counts before imputation
print("Missing values before imputation:")
print(df[numeric_cols].isna().sum())

# 3) Impute missing numeric values with column medians
medians = df[numeric_cols].median()
df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.median()))

print("\nMedians used for imputation:")
print(medians)

# Verify no missing values remain in numeric columns
print("\nMissing values after imputation:")
print(df[numeric_cols].isna().sum())

# 4) Min-Max scaling of numeric columns
# Prefer sklearn's MinMaxScaler if available; otherwise use a safe manual implementation.
try:
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    print("\nMin-Max scaling applied using sklearn.preprocessing.MinMaxScaler.")
except Exception as e:
    # Manual safe Min-Max scaling (handles constant columns)
    print(f"\nWarning: sklearn scaling failed ({e}), using manual fallback.")
    mins = df[numeric_cols].min()
    maxs = df[numeric_cols].max()
    denom = (maxs - mins).replace(0, 1)  # avoid division by zero for constant columns
    df[numeric_cols] = (df[numeric_cols] - mins) / denom
    print("Min-Max scaling applied using manual fallback implementation.")

# 5) Quick validation: show min and max after scaling
print("\nScaled numeric column ranges (min, max):")
for col in numeric_cols:
    print(f"{col}: min={df[col].min():.3f}, max={df[col].max():.3f}")

# 6) Output: show first rows and save to CSV
print("\nFirst 8 rows of the normalized dataset:")
print(df.head(8))

output_path = "normalized_healthcare_data.csv"
df.to_csv(output_path, index=False)
print(f"\nNormalized dataset saved to: {output_path}")