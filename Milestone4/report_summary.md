# Milestone 4: Dashboard for Insights

## Objective
The objective of Milestone 4 is to design and develop an interactive dashboard to visualize and analyze health anomalies detected from fitness device data. The dashboard helps users understand abnormal patterns in heart rate, sleep duration, and step count through interactive visualizations and downloadable reports.

---

## Dashboard Workflow
1. The dashboard is executed using **Streamlit in Google Colaboratory**.
2. Users upload fitness data files in **CSV or JSON format**.
3. The data is preprocessed and relevant health metrics are extracted.
4. Anomaly detection is performed dynamically for:
   - Heart rate
   - Sleep duration
   - Step count
5. Interactive charts display health trends with highlighted anomalies.
6. Users can filter data based on selected date ranges.
7. A summarized anomaly report can be downloaded in **CSV format**.

---

## Tools & Libraries Used
- **Python**
- **Streamlit** – Interactive dashboard development
- **Pandas** – Data preprocessing and analysis
- **Plotly** – Interactive visualizations
- **Google Colaboratory** – Execution environment

---

## Key Insights from the Dashboard
- Heart rate trends highlight abnormal spikes using anomaly markers.
- Sleep duration analysis identifies insufficient or abnormal sleep patterns.
- Step count behavior detects unusually low activity days.
- Date-wise filtering allows users to analyze specific time periods.
- The anomaly summary report provides metric-level insights with timestamps.

---

## Screenshot References
- **dashboard_ui.png** – Displays the running Streamlit dashboard with interactive health anomaly visualizations.
- **report_download.png** – Shows the anomaly summary report download functionality.

---

## Conclusion
The dashboard successfully integrates data upload, anomaly detection, visualization, and report generation into a single interactive interface. This milestone enhances interpretability of health data and supports better understanding of fitness-related anomalies.
