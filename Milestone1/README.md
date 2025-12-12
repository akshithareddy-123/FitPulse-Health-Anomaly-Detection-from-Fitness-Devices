FitPulse Health Anomaly Detection from Fitness Devices 
Prepare a clean, time-aligned dataset from fitness device logs (steps, activity, sleep) to be used for anomaly detection.

**Fit Base Data by Monica MD (Kaggle)**  
Includes: minute-level steps, daily steps, and sleep logs.  
1. Created project folder structure in Google Colab  
2. Uploaded raw CSVs (minute steps, daily steps, sleep)  
3. Validated data formats and timestamp columns  
4. Converted timestamps to UTC using Pandas  
5. Resampled all datasets to **1-minute frequency**  
6. Merged into a consolidated dataframe  
7. Handled missing data using forward-fill and back-fill  
8. Exported final dataset → `cleaned_fitness_data.csv`
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Google Colab  
- Minute Steps Trend  
- Sleep Duration Trend  
- Daily Steps Trend  

Screenshots are included in this notebook.
A fully cleaned dataset with minute-level aligned:  
- Steps  
- Daily Steps  
- Sleep metrics

This dataset is ready for Milestone 2 analysis.
