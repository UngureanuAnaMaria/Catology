import pandas as pd


def check_missing_values(file_path):

    df = pd.read_excel(file_path)

    missing_values = df.isnull().sum()

    if missing_values.any():
        print("\nThere are missing values in the following columns:")
        print(missing_values[missing_values > 0])
    else:
        print("\nNo missing values found in the dataset.")
