# Milestone 3: Anomaly Detection and Visualization
## FitPulse Health Anomaly Detection from Fitness Devices

---

## Objective
The objective of Milestone 3 is to identify, label, and visualize anomalies in fitness device data.
This milestone focuses on detecting abnormal patterns in heart rate and sleep behavior using
time-series forecasting, statistical thresholding, cluster-based analysis, and visualization
techniques.

---

## Dataset Used
Fitbit Fitness Tracker Data (Kaggle)

Files used:
- heartrate_seconds_merged.csv – High-frequency heart rate data
- sleepDay_merged.csv – Daily sleep duration data

Heart rate data was resampled to one-minute intervals to improve computational efficiency while
preserving temporal trends.

---

## Steps Followed

### 1. Residual Analysis using Prophet
- Heart rate data was analyzed using Facebook Prophet time-series models.
- Separate Prophet models were trained for multiple users to maintain time-series continuity.
- Predicted heart rate values were generated, and residuals were calculated as:

Residual = Actual Value − Predicted Value

- Large residual values indicate deviations from normal behavior and were considered potential anomalies.

---

### 2. Threshold-based Anomaly Detection
- Domain-specific thresholds were applied to identify abnormal observations:
  - Heart rate anomalies were detected when residual values exceeded 2 × standard deviation.
  - Sleep anomalies were detected when sleep duration was less than 6 hours or greater than 10 hours.
- Data points exceeding these thresholds were marked as anomalies.

---

### 3. Cluster-based Anomaly Detection
- Clustering results obtained during Milestone 2 were reused.
- Outlier clusters representing unusual behavioral patterns were treated as potential anomalies.
- Cluster-based insights were used to support and validate anomalies detected using residual
  and threshold-based methods.

---

### 4. Anomaly Labeling
- Each data point in the dataset was labeled as:
  - Normal
  - Anomaly
- This ensured clear distinction between normal and abnormal observations.

---

### 5. Visualization of Anomalies
- Interactive time-series visualizations were created:
  - Heart rate time-series charts with anomalies highlighted using red markers.
  - Sleep pattern visualizations showing abnormal sleep segments.
- Alert markers were used to clearly distinguish anomalous data points from normal patterns.

---

## Tools and Technologies Used
- Python
- Google Colaboratory
- Pandas
- Prophet
- NumPy
- Matplotlib

---

## Key Insights and Visualizations
- Sudden spikes and drops in heart rate were successfully identified using Prophet residual analysis.
- Abnormal sleep durations were detected using domain-based threshold limits.
- Combining residual analysis, threshold-based detection, and cluster-based validation improved
  the reliability of anomaly detection.
- Visualizations provided clear and interpretable insights into abnormal health patterns.

---

## Outputs Generated
- visualizations/heart_rate_anomalies.png
- visualizations/sleep_anomalies.png
- anomaly_detection.ipynb

---

## Conclusion
Milestone 3 successfully demonstrates anomaly detection and visualization on fitness device data.
The use of Prophet-based residual analysis, statistical thresholding, cluster-based validation,
and clear time-series visualizations provides an effective approach for identifying abnormal
health patterns from wearable devices.

