import pandas as pd


def update_age_column(file_path):
    """
    Update the 'Age' column in the dataset with clearer English values.

    Args:
        file_path (str): Path to the input Excel file.
    """

    age_mapping = {
        "Moinsde1": "Less than 1 year",
        "1a2": "1-2 years",
        "2a10": "2-10 years",
        "Plusde10": "More than 10 years"
    }

    dataset = pd.read_excel(file_path)

    dataset["Age"] = dataset["Age"].map(age_mapping)

    dataset.to_excel(file_path, index=False)

    print(f"'Age' column updated")
