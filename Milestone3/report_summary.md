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
Fitbit Fitness Tracker Data (Kaggle – Mobius)

The following files were used:
- heartrate_seconds_merged.csv – Continuous heart rate time-series data
- sleepDay_merged.csv – Daily sleep duration data

These datasets provide timestamp-based health data required for anomaly detection.

---

## Steps Followed

### 1. Residual Analysis using Prophet
A Prophet time-series forecasting model was trained on heart rate data.
The model generated predicted values, and residuals were calculated as:

Residual = Actual Value − Predicted Value

Large residual values indicate deviations from normal behavior and were used to identify
potential anomalies.

---

### 2. Threshold-based Anomaly Detection
Domain-specific statistical thresholds were applied:
- Heart rate anomalies were detected when residuals exceeded 2 × standard deviation.
- Sleep anomalies were detected when sleep duration was less than 6 hours or greater than
  10 hours.

Data points crossing these thresholds were classified as anomalous.

---

### 3. Cluster-based Anomaly Detection
Outlier clusters identified during Milestone 2 were reused for anomaly detection.
Data points belonging to abnormal clusters were treated as potential anomalies and were
validated using residual-based and threshold-based detection methods.

---

### 4. Anomaly Labeling
Each data point was clearly labeled as either:
- Normal
- Anomaly

This ensured a clear distinction between normal and abnormal observations in the dataset.

---

### 5. Visualization of Anomalies
Time-series visualizations were created to highlight anomalies:
- Heart rate anomalies were marked in red on the heart rate time-series plot.
- Sleep anomalies were highlighted on the sleep pattern visualization.

Alert markers were used to visually distinguish anomalous points from normal data.

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
- Sudden spikes and drops in heart rate were successfully detected using Prophet residual analysis.
- Abnormal sleep durations were identified using domain-specific threshold rules.
- Combining residual-based, threshold-based, and cluster-based approaches improved anomaly
  detection reliability.
- Visualizations provided clear and intuitive insights into abnormal health patterns.

---

## Outputs Generated
- visualizations/heart_rate_anomalies.png
- visualizations/sleep_anomalies.png
- anomaly_detection.ipynb

---

## Conclusion
Milestone 3 successfully demonstrates anomaly detection and visualization using fitness device data.
The integration of Prophet-based residual analysis, statistical thresholding, cluster-based validation,
and clear visualizations provides an effective approach for identifying abnormal health patterns from
wearable devices.
