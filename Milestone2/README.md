# Milestone 2 – Feature Extraction and Modeling

## Objective
The objective of Milestone 2 is to extract meaningful features from fitness device data and model behavioral trends to support health anomaly detection in later milestones.

## Dataset Description
The dataset consists of time-series data collected from fitness devices. It includes metrics such as:
- Heart Rate
- Daily Steps
- Sleep Duration
- Timestamp
- Additional demographic and health-related attributes

The dataset used for this milestone is stored as `Clean.csv` inside the `data/` directory.

## Steps Performed

### 1. Feature Extraction
- Time-series features were extracted using **TSFresh** from heart rate data.
- Statistical features such as mean, standard deviation, skewness, and kurtosis were computed.
- Feature selection using Variance Threshold was applied conditionally. For single time-series samples, feature selection was skipped to avoid zero-variance issues.

### 2. Trend Modeling
- Seasonal and temporal trends in heart rate data were modeled using **Facebook Prophet**.
- Future values were forecasted and visualized along with confidence intervals.

### 3. Clustering Behavioral Patterns
- Behavioral patterns were analyzed using **KMeans clustering**.
- Features such as heart rate, steps, and sleep were standardized before clustering.
- **PCA (Principal Component Analysis)** was used for dimensionality reduction and visualization of clusters.

## Tools and Libraries Used
- Python
- Google Colab
- Pandas, NumPy
- TSFresh
- Facebook Prophet
- Scikit-learn
- Matplotlib, Seaborn
- SciPy

## Key Observations
- Heart rate data showed clear temporal trends and seasonal variations.
- Clustering helped identify distinct behavioral patterns that can represent normal and atypical behavior.
- Dimensionality reduction using PCA enabled effective visualization of behavioral clusters.

## Folder Structure
