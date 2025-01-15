import pandas as pd


def rename_behavior_columns(file_path):
    """
    Rename behavior columns in the dataset from French to English.

    Args:
        file_path (str): Path to the input Excel file.
    """

    column_mapping = {
        "Timide": "Shy",
        "Calme": "Calm",
        "Effrayé": "Fearful",
        "Intelligent": "Intelligent",
        "Vigilant": "Vigilant",
        "Perséverant": "Perseverant",
        "Affectueux": "Affectionate",
        "Amical": "Friendly",
        "Solitaire": "Solitary",
        "Brutal": "Brutal",
        "Dominant": "Dominant",
        "Agressif": "Aggressive",
        "Impulsif": "Impulsive",
        "Prévisible": "Predictable",
        "Distrait": "Distracted"
    }

    dataset = pd.read_excel(file_path)

    dataset = dataset.rename(columns=column_mapping)

    dataset.to_excel(file_path, index=False)

    print(f"Behavior columns renamed to English")


def update_behavior_columns(file_path):
    """
    Update behavior columns by converting values
    from 1-3 to 'No' and 4-5 to 'Yes' for each behavior trait.

    Args:
        file_path (str): Path to the input Excel file.
    """

    dataset = pd.read_excel(file_path)

    behavior_columns = [
        "Shy", "Calm", "Fearful", "Intelligent", "Vigilant", "Perseverant",
        "Affectionate", "Friendly", "Solitary", "Brutal", "Dominant", "Aggressive",
        "Impulsive", "Predictable", "Distracted"
    ]

    for column in behavior_columns:
        if column in dataset.columns:
            dataset[column] = dataset[column].apply(lambda x: 'Yes' if x >= 4 else 'No')

    dataset.to_excel(file_path, index=False)

    print(f"Behavior columns updated")
