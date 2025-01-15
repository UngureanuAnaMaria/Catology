import pandas as pd


def update_breed_column(file_path):
    """
    Update the Catology dataset by:
    1. Replacing breed abbreviations with full names.
    2. Removing rows with "No breed", "Other", or "Unknown" values in the Breed column.
    3. Removing rows with missing values in the Breed column.
    4. Renaming the "Race" column to "Breed".

    Args:
        file_path (str): Path to the input Excel file.
    """

    race_mapping = {
        "BEN": "Bengal",
        "SBI": "Birman",
        "BRI": "British Shorthair",
        "CHA": "Chartreux",
        "EUR": "European Shorthair",
        "MCO": "Maine Coon",
        "PER": "Persian",
        "RAG": "Ragdoll",
        "SPH": "Sphynx",
        "SAV": "Savannah",
        "ORI": "Siamese",
        "TUV": "Turkish Angora",
        "Autre": "Other",
        "NSP": "Unknown",
        "NR": "No breed"
    }

    dataset = pd.read_excel(file_path)

    dataset["Race"] = dataset["Race"].map(race_mapping)

    dataset = dataset[~dataset["Race"].isin(["No breed", "Other", "Unknown"])]

    dataset.rename(columns={"Race": "Breed"}, inplace=True)

    dataset.to_excel(file_path, index=False)

    print(f"'Breed' column updated")


def move_breed_column(file_path):
    """
    Move the 'Breed' column to the first position in the dataset.

    Args:
        file_path (str): Path to the input Excel file.
    """

    dataset = pd.read_excel(file_path)

    if 'Breed' in dataset.columns:
        columns = ['Breed'] + [col for col in dataset.columns if col != 'Breed']
        dataset = dataset[columns]

        dataset.to_excel(file_path, index=False)
        print(f"'Breed' column moved to the first position")
    else:
        print("'Breed' column not found in the dataset")
