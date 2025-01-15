import pandas as pd
import random


def add_maine_coon_traits(file_path):
    """
    Special Conditions for Maine Coon cats:
        - **Coat Color**:
            - Can be "Brown Tabby", "Black", "Blue", "Red", "Cream", "Tortoiseshell".
            - Distribution: "Brown Tabby" (40%), others equally distributed (12% each).
        - **Coat Pattern**:
            - Can be "Tabby", "Solid", "Bicolor", "Tortie".
            - Distribution: "Tabby" (50%), others equally distributed (16.67% each).
        - **Eye Color**:
            - Can be "Green", "Gold", "Copper", "Blue", "Odd-eyed".
            - Distribution: "Green" (30%), "Gold" (25%), "Copper" (20%), "Blue" (15%), "Odd-eyed" (10%).
    """

    dataset = pd.read_excel(file_path)

    coat_colors = ["Brown Tabby", "Black", "Blue", "Red", "Cream", "Tortoiseshell"]
    coat_patterns = ["Tabby", "Solid", "Bicolor", "Tortie"]
    eye_colors = ["Green", "Gold", "Copper", "Blue", "Odd-eyed"]

    coat_color_distribution = {
        "Brown Tabby": 0.4,
        "Black": 0.12,
        "Blue": 0.12,
        "Red": 0.12,
        "Cream": 0.12,
        "Tortoiseshell": 0.12
    }
    coat_pattern_distribution = {
        "Tabby": 0.5,
        "Solid": 0.1667,
        "Bicolor": 0.1667,
        "Tortie": 0.1667
    }
    eye_color_distribution = {
        "Green": 0.3,
        "Gold": 0.25,
        "Copper": 0.2,
        "Blue": 0.15,
        "Odd-eyed": 0.1
    }

    maine_coon_mask = dataset["Breed"] == "Maine Coon"

    dataset.loc[maine_coon_mask, "Coat Color"] = random.choices(
        coat_colors, weights=[coat_color_distribution[color] for color in coat_colors],
        k=maine_coon_mask.sum()
    )
    dataset.loc[maine_coon_mask, "Coat Pattern"] = random.choices(
        coat_patterns, weights=[coat_pattern_distribution[pattern] for pattern in coat_patterns],
        k=maine_coon_mask.sum()
    )
    dataset.loc[maine_coon_mask, "Coat Length"] = "Long"
    dataset.loc[maine_coon_mask, "Coat Texture"] = "Slightly Coarse"
    dataset.loc[maine_coon_mask, "Size"] = "Very Big"
    dataset.loc[maine_coon_mask, "Body Type"] = "Muscular and Athletic"
    dataset.loc[maine_coon_mask, "Leg Length"] = "Long"
    dataset.loc[maine_coon_mask, "Face Shape"] = "Square"
    dataset.loc[maine_coon_mask, "Eye Color"] = random.choices(
        eye_colors, weights=[eye_color_distribution[color] for color in eye_colors], k=maine_coon_mask.sum()
    )
    dataset.loc[maine_coon_mask, "Eye Shape"] = "Oval"
    dataset.loc[maine_coon_mask, "Ear Size"] = "Very Big"
    dataset.loc[maine_coon_mask, "Ear Shape"] = "Tufted"
    dataset.loc[maine_coon_mask, "Tail Shape"] = "Plume and Straight"
    dataset.loc[maine_coon_mask, "Tail Length"] = "Long"

    dataset.to_excel(file_path, index=False)

    print(f"Maine Coon traits added to the dataset")
