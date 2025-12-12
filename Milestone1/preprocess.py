import pandas as pd

def normalize_timestamp(df, col):
    df[col] = pd.to_datetime(df[col], errors='coerce', utc=True)
    df = df.dropna(subset=[col])        
    df = df.sort_values(col)            
    return df

def resample_1min(df, time_col, agg='sum'):
    df = df.set_index(time_col)
    if agg == 'sum':
        df = df.resample("1T").sum()
    else:
        df = df.resample("1T").mean()
    return df.reset_index()

def preprocess_data(minute_steps_file, daily_steps_file, sleep_file):

    minute_steps = pd.read_csv(minute_steps_file)
    daily_steps = pd.read_csv(daily_steps_file)
    sleep = pd.read_csv(sleep_file)

    minute_steps = minute_steps.rename(columns={"ActivityMinute": "Timestamp"})
    daily_steps = daily_steps.rename(columns={"ActivityDay": "Timestamp"})
    sleep = sleep.rename(columns={"SleepDay": "Timestamp"})

    minute_steps = normalize_timestamp(minute_steps, "Timestamp")
    daily_steps = normalize_timestamp(daily_steps, "Timestamp")
    sleep = normalize_timestamp(sleep, "Timestamp")

    minute_steps = resample_1min(minute_steps, "Timestamp", agg='sum')
    daily_steps = resample_1min(daily_steps, "Timestamp", agg='sum')
    sleep = resample_1min(sleep, "Timestamp", agg='mean')

    df = minute_steps.merge(daily_steps, on="Timestamp", how="outer")
    df = df.merge(sleep, on="Timestamp", how="outer")

    df = df.ffill().bfill()

    df = df.sort_values("Timestamp")

    df.to_csv("Milestone1/cleaned_fitness_data.csv", index=False)

    return df
