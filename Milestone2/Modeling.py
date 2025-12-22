import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

DATA_PATH = "/content/Milestone2/data/Clean.csv"
df = pd.read_csv(DATA_PATH)

print("Columns in dataset:")
print(df.columns)

time_col = [c for c in df.columns if 'time' in c.lower() or 'date' in c.lower()][0]
hr_col = [c for c in df.columns if 'heart' in c.lower()][0]
steps_col = [c for c in df.columns if 'step' in c.lower()][0]
sleep_col = [c for c in df.columns if 'sleep' in c.lower()][0]

df[time_col] = pd.to_datetime(df[time_col])

print("\nDetected Columns:")
print("Time:", time_col)
print("Heart Rate:", hr_col)
print("Steps:", steps_col)
print("Sleep:", sleep_col)


prophet_df = df[[time_col, hr_col]].copy()
prophet_df.columns = ['ds', 'y']

model = Prophet()
model.fit(prophet_df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

model.plot(forecast)
plt.title("Heart Rate Trend Forecast")
plt.show()

X = df[[hr_col, steps_col, sleep_col]].dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

print("\nClustering completed")

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(6, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Behavioral Clustering using PCA")
plt.show()

print("Modeling completed successfully")
