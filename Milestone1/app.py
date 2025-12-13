from preprocess import preprocess_data
if __name__ == "__main__":
    df = preprocess_data(
        "Milestone1/data/minuteSteps.csv",
        "Milestone1/data/dailySteps.csv",
        "Milestone1/data/sleepDay.csv"
    )

    print("Processed Data:")
    print(df.head())
