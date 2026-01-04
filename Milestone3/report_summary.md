# Milestone 3: Anomaly Detection and Visualization  
## FitPulse Health Anomaly Detection from Fitness Devices

---

## Objective
The objective of Milestone 3 is to detect, label, and visualize anomalies in fitness device data.  
This milestone focuses on identifying abnormal patterns in heart rate and sleep behavior using time-series forecasting, statistical thresholding, and visual analysis.

---

## Dataset Used
Fitbit Fitness Tracker Data (Kaggle – Mobius)

Files used for analysis:
- heartrate_seconds_merged.csv – Heart rate time-series data
- sleepDay_merged.csv – Sleep duration data

---

## Steps Followed

### 1. Residual Analysis using Prophet
A Prophet time-series forecasting model was trained on heart rate data for a single user.  
Residuals were calculated as the difference between actual and predicted values to identify abnormal behavior.

---

### 2. Threshold-based Anomaly Detection
Statistical thresholds were applied:
- Heart rate anomalies: values exceeding 2 × standard deviation of residuals  
- Sleep anomalies: values deviating more than 1.5 × standard deviation from the mean  

Data points beyond these thresholds were marked as anomalies.

---

### 3. Anomaly Labeling
Each data point was labeled as either Normal or Anomaly, ensuring clear differentiation between regular and abnormal observations.

---

### 4. Visualization of Anomalies
Time-series plots were created with anomalies highlighted:
- Heart rate anomalies marked in red  
- Sleep duration anomalies highlighted on sleep pattern plots  

These visualizations help in easy interpretation of abnormal health patterns.

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
- Sudden spikes and drops in heart rate were successfully detected.  
- Abnormal sleep durations were identified when sleep time deviated from normal patterns.  
- Prophet-based modeling effectively captured time-dependent trends in health data.

---

## Outputs Generated
- visualizations/heart_rate_anomalies.png  
- visualizations/sleep_anomalies.png  
- anomaly_detection.ipynb  

---

## Conclusion
Milestone 3 successfully demonstrates anomaly detection and visualization using fitness device data.  
The approach provides an effective method for identifying abnormal health patterns from wearable devices.
