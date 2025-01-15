import pandas as pd
import random


def add_turkish_angora_traits(file_path):
    """
    Special Conditions for Turkish Angora cats:
        - **Coat Color**:
            - Can be "White", "Black", "Blue", "Red", or "Cream".
            - Distribution: "White" (50%), others equally distributed (12.5% each).
        - **Coat Pattern**:
            - Can be "Solid", "Tabby", or "Bicolor".
            - Distribution: "Solid" (60%), "Tabby" (25%), "Bicolor" (15%).
        - **Size**:
            - Can be "Small" or "Medium".
            - Distribution: "Small" (40%), "Medium" (60%).
        - **Eye Color**:
            - Can be "Blue", "Amber", "Green", or "Odd-eyed".
            - Distribution: "Blue" (30%), "Amber" (30%), "Green" (20%), "Odd-eyed" (20%).
    """

    dataset = pd.read_excel(file_path)

    coat_colors = ["White", "Black", "Blue", "Red", "Cream"]
    coat_patterns = ["Solid", "Tabby", "Bicolor"]
    sizes = ["Small", "Medium"]
    leg_lengths = ["Medium", "Long"]
    eye_colors = ["Blue", "Amber", "Green", "Odd-eyed"]

    coat_color_distribution = {
        "White": 0.5,
        "Black": 0.125,
        "Blue": 0.125,
        "Red": 0.125,
        "Cream": 0.125
    }
    coat_pattern_distribution = {
        "Solid": 0.6,
        "Tabby": 0.25,
        "Bicolor": 0.15
    }
    size_distribution = {"Small": 0.4, "Medium": 0.6}
    eye_color_distribution = {
        "Blue": 0.3,
        "Amber": 0.3,
        "Green": 0.2,
        "Odd-eyed": 0.2
    }

    turkish_angora_mask = dataset["Breed"] == "Turkish Angora"

    dataset.loc[turkish_angora_mask, "Coat Color"] = random.choices(
        coat_colors, weights=[coat_color_distribution[color] for color in coat_colors],
        k=turkish_angora_mask.sum()
    )
    dataset.loc[turkish_angora_mask, "Coat Pattern"] = random.choices(
        coat_patterns, weights=[coat_pattern_distribution[pattern] for pattern in coat_patterns],
        k=turkish_angora_mask.sum()
    )
    dataset.loc[turkish_angora_mask, "Coat Length"] = "Long"
    dataset.loc[turkish_angora_mask, "Coat Texture"] = "Silky"
    dataset.loc[turkish_angora_mask, "Size"] = random.choices(
        sizes, weights=[size_distribution[size] for size in sizes], k=turkish_angora_mask.sum()
    )
    dataset.loc[turkish_angora_mask, "Body Type"] = "Long and Lean"
    dataset.loc[turkish_angora_mask, "Leg Length"] = random.choices(leg_lengths, k=turkish_angora_mask.sum())
    dataset.loc[turkish_angora_mask, "Face Shape"] = "Wedge-shaped"
    dataset.loc[turkish_angora_mask, "Eye Color"] = random.choices(
        eye_colors, weights=[eye_color_distribution[color] for color in eye_colors], k=turkish_angora_mask.sum()
    )
    dataset.loc[turkish_angora_mask, "Eye Shape"] = "Almond-shaped"
    dataset.loc[turkish_angora_mask, "Ear Size"] = "Big"
    dataset.loc[turkish_angora_mask, "Ear Shape"] = "Pointed"
    dataset.loc[turkish_angora_mask, "Tail Shape"] = "Plume and Straight"
    dataset.loc[turkish_angora_mask, "Tail Length"] = "Long"

    dataset.to_excel(file_path, index=False)

    print(f"Turkish Angora traits added to the dataset")
