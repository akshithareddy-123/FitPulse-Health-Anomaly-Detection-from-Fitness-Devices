import pandas as pd
from tsfresh import extract_features
from sklearn.feature_selection import VarianceThreshold
from scipy.stats import skew, kurtosis

DATA_PATH = "/content/Milestone2/data/Clean.csv"
df = pd.read_csv(DATA_PATH)

print("Columns in dataset:", df.columns)

time_col = [c for c in df.columns if 'time' in c.lower() or 'date' in c.lower()][0]
hr_col = [c for c in df.columns if 'heart' in c.lower()][0]

df[time_col] = pd.to_datetime(df[time_col])

print("Detected time column:", time_col)
print("Detected heart rate column:", hr_col)

ts_data = df[[time_col, hr_col]].copy()
ts_data['id'] = 1
features = extract_features(
    ts_data,
    column_id='id',
    column_sort=time_col
)

print("TSFresh feature extraction completed")

stat_features = {
    "heart_rate_mean": df[hr_col].mean(),
    "heart_rate_std": df[hr_col].std(),
    "heart_rate_skewness": skew(df[hr_col]),
    "heart_rate_kurtosis": kurtosis(df[hr_col])
}

print("Statistical Features:")
print(stat_features)

if features.shape[0] > 1:
    selector = VarianceThreshold(threshold=0.01)
    selected_features = selector.fit_transform(features.fillna(0))
    print("Selected feature shape:", selected_features.shape)
else:
    print("Only one sample detected → skipping VarianceThreshold")
    selected_features = features

print("Feature extraction completed successfully")
