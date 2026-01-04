# Milestone 3: Anomaly Detection and Visualization  
## FitPulse Health Anomaly Detection from Fitness Devices

---

## Objective
The objective of Milestone 3 is to detect, label, and visualize anomalies in fitness device data.  
This milestone focuses on identifying abnormal patterns in heart rate and sleep behavior using
time-series forecasting, statistical thresholding, cluster-based insights, and visual analysis.

---

## Dataset Used
Fitbit Fitness Tracker Data (Kaggle – Mobius)

Files used for analysis:
- heartrate_seconds_merged.csv – Heart rate time-series data
- sleepDay_merged.csv – Sleep duration data

The dataset provides continuous timestamp-based data suitable for time-series anomaly detection.

---

## Steps Followed

### 1. Residual Analysis using Prophet
A Prophet time-series forecasting model was trained on heart rate data for a single user.  
The model generated predicted values, and residuals were computed as:

Residual = Actual Value − Predicted Value  

Large residual values indicate deviations from normal behavior and potential anomalies.

---

### 2. Threshold-based Anomaly Detection
Statistical thresholds were applied to identify abnormal observations:
- Heart rate anomalies were detected when residuals exceeded **2 × standard deviation**
- Sleep anomalies were detected when sleep duration deviated more than **1.5 × standard deviation** from the mean  

Data points crossing these thresholds were marked as anomalies.

---

### 3. Cluster-based Anomaly Detection
Clustering results obtained during **Milestone 2** were reused for anomaly identification.  
Outlier clusters representing unusual behavioral patterns were treated as potential anomalies
and were cross-validated using residual-based and threshold-based detection methods.

---

### 4. Visualization of Anomalies
Time-series visualizations were created to highlight anomalous behavior:
- Heart rate anomalies were marked in red on the heart rate time-series plot
- Sleep anomalies were highlighted on the sleep duration plot  

These visualizations provide intuitive understanding of abnormal health patterns.

---

## Tools and Technologies Used
- Python  
- Google Colaboratory  
- Pandas  
- Prophet  
- NumPy  
- Matplotlib  

---

## Key Insights
- Sudden spikes and drops in heart rate were successfully detected as anomalies.
- Abnormal sleep durations were identified when sleep time deviated significantly from normal patterns.
- Prophet-based residual analysis effectively captured temporal trends in health data.
- Combining residual analysis, thresholding, and clustering improved anomaly detection reliability.

---

## Outputs Generated
- visualizations/heart_rate_anomalies.png  
- visualizations/sleep_anomalies.png  
- anomaly_detection.ipynb  

---

## Conclusion
Milestone 3 successfully demonstrates anomaly detection and visualization using fitness device data.  
The integration of Prophet-based forecasting, statistical thresholding, cluster-based insights, and
visual analysis provides an effective approach for identifying abnormal health patterns from wearable
devices.
