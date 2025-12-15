from preprocess import preprocess_data

if __name__ == "__main__":
    df = preprocess_data(
        "data/minuteSteps.csv",
        "data/dailySteps.csv",
        "data/sleepDay.csv"
    )

    print("Processed Data:")
    print(df.head())
