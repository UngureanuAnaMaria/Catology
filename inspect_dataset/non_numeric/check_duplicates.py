import pandas as pd


def check_duplicates(file_path):

    df = pd.read_excel(file_path)

    duplicates = df[df.duplicated()]

    df_cleaned = df.drop_duplicates()

    df_cleaned.to_excel(file_path, index=False)

    if not duplicates.empty:
        print("\nThe following duplicates found in the dataset and removed:")
        print(duplicates)
    else:
        print("\nNo duplicates found in the dataset.")
