import pandas as pd


def sort_by_breed_sex_age(file_path):
    """
    Sort the dataset by the 'Breed' column in a specific order, then by 'Sex' (F first, then M),
    and finally by 'Age' in the order: Less than 1 year, 1-2 years, 2-10 years, More than 10 years.

    Args:
        file_path (str): Path to the input Excel file.
    """

    breed_order = [
        "Bengal", "Savannah", "Siamese", "Birman", "Ragdoll", "Chartreux",
        "British Shorthair", "Turkish Angora", "Persian", "Maine Coon",
        "European Shorthair", "Sphynx"
    ]

    age_order = [
        "Less than 1 year", "1-2 years", "2-10 years", "More than 10 years"
    ]

    dataset = pd.read_excel(file_path)

    dataset["Breed"] = pd.Categorical(dataset["Breed"], categories=breed_order, ordered=True)
    dataset["Age"] = pd.Categorical(dataset["Age"], categories=age_order, ordered=True)

    dataset = dataset.sort_values(by=["Breed", "Sex", "Age"], ascending=[True, True, True])

    dataset.to_excel(file_path, index=False)

    print(f"Dataset sorted by 'Breed', 'Sex', and 'Age'")
