import pandas as pd


def update_sex_column(file_path):
    """
    Rename the 'Sexe' column to 'Sex' and remove rows where 'Sex' has the value 'NSP'.

    Args:
        file_path (str): Path to the input Excel file.
    """

    dataset = pd.read_excel(file_path)

    if 'Sexe' in dataset.columns:
        dataset = dataset.rename(columns={'Sexe': 'Sex'})
        print("Column 'Sexe' renamed to 'Sex'")
    else:
        print("Column 'Sexe' not found. Checking for 'Sex' column")

    if 'Sex' in dataset.columns:
        original_row_count = len(dataset)
        dataset = dataset[dataset['Sex'] != 'NSP']
        cleaned_row_count = len(dataset)
        print(f"Removed {original_row_count - cleaned_row_count} rows where 'Sex' was 'NSP'")
    else:
        print("Column 'Sex' not found in the dataset")

    dataset.to_excel(file_path, index=False)

    print(f"'Sex' column updated")
