FitPulse – Health Anomaly Detection from Fitness Devices

## Milestone 1: Data Collection and Preprocessing

---

## Objective of the Milestone

The objective of this milestone is to understand and perform data ingestion,
cleaning, preprocessing, and time alignment of fitness data collected from
wearable devices. This processed data will serve as the foundation for detecting
health anomalies in future milestones.

---

## Dataset Source

**Dataset Name:** FitBase / FitBit Fitness Tracker Data  

**Source:** Kaggle  
https://www.kaggle.com/datasets/arashnic/fitbit  

**Dataset Description:**
The dataset contains fitness data collected from Fitbit wearable devices,
including:
- Minute-level step counts
- Daily activity summaries
- Sleep duration and sleep quality information

The data is collected for multiple users over several days and is suitable for
time-series analysis and health monitoring tasks.

---

## Steps Performed

1. **Data Upload**
   - Uploaded raw CSV files into the `data/` folder in Google Colab.

2. **Data Cleaning**
   - Removed unnecessary columns.
   - Handled missing values where required.
   - Ensured consistent column naming across datasets.

3. **Data Preprocessing**
   - Converted date and time columns into proper `datetime` format.
   - Aggregated minute-level steps data into daily step totals.
   - Aligned daily steps and sleep data based on date.

4. **Normalization / Structuring**
   - Ensured all datasets follow a common date-based structure.
   - Merged datasets into a single consolidated dataframe.

5. **Final Output Generation**
   - Generated a cleaned and merged dataset ready for anomaly detection.

---

## Tools Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Google Colab  

---

## Key Insights

- Minute-level activity data must be aggregated before meaningful analysis.
- Time alignment is critical when merging activity and sleep datasets.
- Data preprocessing significantly improves data consistency and usability.
- The merged dataset provides a clear daily overview of user activity and sleep
  behavior, which is essential for detecting anomalies.

---

## Screenshots of Outputs

Screenshots included in the `screenshots/` folder show:
- Successful execution of `app.py`
- Head of the processed and merged dataframe
- Folder structure and file organization
- Preprocessing logic execution in Google Colab

---

## How to Run the Code

1. Place the dataset CSV files inside the `data/` folder.
2. Install dependencies:
