import pandas as pd
import random


def add_european_shorthair_traits(file_path):
    """
    Special Conditions for European Shorthair cats:
        - **Coat Color**:
            - Can be "Black", "White", "Blue", "Tabby", "Tortoiseshell".
            - Distribution: Equal distribution among all colors (20% each).
        - **Coat Pattern**:
            - Can be "Solid", "Tabby", "Bicolor", "Spotted".
            - Distribution: Equal distribution among all patterns (25% each).
        - **Eye Color**:
            - Can be "Green", "Blue", "Yellow", "Gold".
            - Distribution: Equal distribution among all colors (25% each).
    """

    dataset = pd.read_excel(file_path)

    coat_colors = ["Black", "White", "Blue", "Tabby", "Tortoiseshell"]
    coat_patterns = ["Solid", "Tabby", "Bicolor", "Spotted"]
    eye_colors = ["Green", "Blue", "Yellow", "Gold"]

    coat_color_distribution = {color: 0.2 for color in coat_colors}
    coat_pattern_distribution = {pattern: 0.25 for pattern in coat_patterns}
    eye_color_distribution = {color: 0.25 for color in eye_colors}

    european_shorthair_mask = dataset["Breed"] == "European Shorthair"

    dataset.loc[european_shorthair_mask, "Coat Color"] = random.choices(
        coat_colors, weights=[coat_color_distribution[color] for color in coat_colors],
        k=european_shorthair_mask.sum()
    )
    dataset.loc[european_shorthair_mask, "Coat Pattern"] = random.choices(
        coat_patterns, weights=[coat_pattern_distribution[pattern] for pattern in coat_patterns],
        k=european_shorthair_mask.sum()
    )
    dataset.loc[european_shorthair_mask, "Coat Length"] = "Short"
    dataset.loc[european_shorthair_mask, "Coat Texture"] = "Sleek"
    dataset.loc[european_shorthair_mask, "Size"] = "Medium"
    dataset.loc[european_shorthair_mask, "Body Type"] = "Cobby"
    dataset.loc[european_shorthair_mask, "Leg Length"] = "Medium"
    dataset.loc[european_shorthair_mask, "Face Shape"] = "Rounded"
    dataset.loc[european_shorthair_mask, "Eye Color"] = random.choices(
        eye_colors, weights=[eye_color_distribution[color] for color in eye_colors], k=european_shorthair_mask.sum()
    )
    dataset.loc[european_shorthair_mask, "Eye Shape"] = "Round"
    dataset.loc[european_shorthair_mask, "Ear Size"] = "Medium"
    dataset.loc[european_shorthair_mask, "Ear Shape"] = "Rounded"
    dataset.loc[european_shorthair_mask, "Tail Shape"] = "Straight and Slightly Curved"
    dataset.loc[european_shorthair_mask, "Tail Length"] = "Medium"

    dataset.to_excel(file_path, index=False)

    print(f"European Shorthair traits added to the dataset")
