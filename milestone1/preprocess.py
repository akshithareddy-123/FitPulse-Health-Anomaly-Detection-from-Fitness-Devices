mport pandas as pd

def preprocess_data(minute_steps_path, daily_steps_path, sleep_path):
    minute_steps = pd.read_csv(minute_steps_path)
    daily_steps = pd.read_csv(daily_steps_path)
    sleep = pd.read_csv(sleep_path)

    minute_steps['ActivityMinute'] = pd.to_datetime(minute_steps['ActivityMinute'])

    minute_steps['Date'] = minute_steps['ActivityMinute'].dt.date


    minute_daily = (
        minute_steps
        .groupby('Date')['Steps']
        .sum()
        .reset_index()
    )
    daily_steps['ActivityDay'] = pd.to_datetime(daily_steps['ActivityDay'])
    daily_steps['Date'] = daily_steps['ActivityDay'].dt.date

    daily_steps_clean = daily_steps[['Date', 'StepTotal']].rename(
        columns={'StepTotal': 'DailySteps'}
    )
    sleep['SleepDay'] = pd.to_datetime(sleep['SleepDay'])
    sleep['Date'] = sleep['SleepDay'].dt.date

    sleep_clean = sleep[['Date', 'TotalMinutesAsleep']]

    merged = minute_daily.merge(daily_steps_clean, on='Date', how='left')
    merged = merged.merge(sleep_clean, on='Date', how='left')

    return merged
