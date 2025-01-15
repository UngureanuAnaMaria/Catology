import pandas as pd

def compare_breeds_by_traits(breed1, breed2):
    """
    Compares the traits of two cat breeds in the dataset and returns the comparison in natural language.

    :param breed1: The name of the first breed (e.g., "Bengal").
    :param breed2: The name of the second breed (e.g., "Birman").
    """
    file_path = r"C:\Users\anaun\OneDrive\Desktop\CatologyProject\CatologyDatas.xlsx"
    dataset = pd.read_excel(file_path)

    breed1_traits = dataset[dataset["Breed"] == breed1]
    breed2_traits = dataset[dataset["Breed"] == breed2]

    if breed1_traits.empty or breed2_traits.empty:
        return f"The dataset does not contain enough data for a meaningful comparison between {breed1} and {breed2}."

    traits = [
        "Coat Color", "Coat Pattern", "Coat Length", "Coat Texture", "Size", "Body Type",
        "Leg Length", "Face Shape", "Eye Shape", "Eye Color", "Ear Size", "Ear Shape",
        "Tail Shape", "Tail Length"
    ]

    summary = f"Here is a detailed comparison between {breed1} and {breed2} cats:\n"

    for trait in traits:
        breed1_values = breed1_traits[trait].value_counts(normalize=True)
        breed2_values = breed2_traits[trait].value_counts(normalize=True)

        summary += f"\n**{trait}:**\n"
        if not breed1_values.empty:
            summary += f"- {breed1} cats typically have: " + ", ".join(
                [f"{value} ({int(percentage * 100)}%)" for value, percentage in breed1_values.items()]
            ) + ".\n"
        else:
            summary += f"- {breed1} cats do not have data available for this trait.\n"

        if not breed2_values.empty:
            summary += f"- {breed2} cats typically have: " + ", ".join(
                [f"{value} ({int(percentage * 100)}%)" for value, percentage in breed2_values.items()]
            ) + ".\n"
        else:
            summary += f"- {breed2} cats do not have data available for this trait.\n"

        breed1_set = set(breed1_values.keys())
        breed2_set = set(breed2_values.keys())
        unique_to_breed1 = breed1_set - breed2_set
        unique_to_breed2 = breed2_set - breed1_set

        if unique_to_breed1 or unique_to_breed2:
            summary += "  Key differences:\n"
            if unique_to_breed1:
                summary += f"    - Unique to {breed1}: {', '.join(unique_to_breed1)}.\n"
            if unique_to_breed2:
                summary += f"    - Unique to {breed2}: {', '.join(unique_to_breed2)}.\n"

    return summary