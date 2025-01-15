import pandas as pd
import random


def add_british_shorthair_traits(file_path):
    """
    Special Conditions for British Shorthair cats:
        - **Coat Color**:
            - Can be "Blue", "Black", "White", "Cream", "Tabby", or "Tortoiseshell".
            - Distribution: "Blue" (40%), others equally distributed (12% each).
        - **Coat Pattern**:
            - Can be "Solid", "Tabby", "Bicolor", "Color-Point", or "Harlequin".
            - Distribution: "Solid" (50%), others equally distributed (12.5% each).
        - **Size**:
            - Can be "Medium" or "Big".
            - Distribution: "Medium" (60%), "Big" (40%).
        - **Eye Color**:
            - Can be "Copper", "Gold", or "Blue-green".
            - Distribution: "Copper" (50%), "Gold" (30%), "Blue-green" (20%).
    """

    dataset = pd.read_excel(file_path)

    coat_colors = ["Blue", "Black", "White", "Cream", "Tabby", "Tortoiseshell"]
    coat_patterns = ["Solid", "Tabby", "Bicolor", "Color-Point", "Harlequin"]
    sizes = ["Medium", "Big"]
    eye_colors = ["Copper", "Gold", "Blue-green"]
    ear_sizes = ["Small", "Medium"]
    tail_lengths = ["Short", "Medium"]

    coat_color_distribution = {
        "Blue": 0.4,
        "Black": 0.12,
        "White": 0.12,
        "Cream": 0.12,
        "Tabby": 0.12,
        "Tortoiseshell": 0.12
    }
    coat_pattern_distribution = {
        "Solid": 0.5,
        "Tabby": 0.125,
        "Bicolor": 0.125,
        "Color-Point": 0.125,
        "Harlequin": 0.125
    }
    size_distribution = {"Medium": 0.6, "Big": 0.4}
    eye_color_distribution = {"Copper": 0.5, "Gold": 0.3, "Blue-green": 0.2}

    british_shorthair_mask = dataset["Breed"] == "British Shorthair"

    dataset.loc[british_shorthair_mask, "Coat Color"] = random.choices(
        coat_colors, weights=[coat_color_distribution[color] for color in coat_colors],
        k=british_shorthair_mask.sum()
    )
    dataset.loc[british_shorthair_mask, "Coat Pattern"] = random.choices(
        coat_patterns, weights=[coat_pattern_distribution[pattern] for pattern in coat_patterns],
        k=british_shorthair_mask.sum()
    )
    dataset.loc[british_shorthair_mask, "Coat Length"] = "Short"
    dataset.loc[british_shorthair_mask, "Coat Texture"] = "Dense and Plush"
    dataset.loc[british_shorthair_mask, "Size"] = random.choices(
        sizes, weights=[size_distribution[size] for size in sizes],
        k=british_shorthair_mask.sum()
    )
    dataset.loc[british_shorthair_mask, "Body Type"] = "Cobby"
    dataset.loc[british_shorthair_mask, "Leg Length"] = "Short"
    dataset.loc[british_shorthair_mask, "Face Shape"] = "Round"
    dataset.loc[british_shorthair_mask, "Eye Color"] = random.choices(
        eye_colors, weights=[eye_color_distribution[color] for color in eye_colors], k=british_shorthair_mask.sum()
    )
    dataset.loc[british_shorthair_mask, "Eye Shape"] = "Round"
    dataset.loc[british_shorthair_mask, "Ear Size"] = random.choices(ear_sizes, k=british_shorthair_mask.sum())
    dataset.loc[british_shorthair_mask, "Ear Shape"] = "Rounded"
    dataset.loc[british_shorthair_mask, "Tail Shape"] = "Straight and Slightly Curved"
    dataset.loc[british_shorthair_mask, "Tail Length"] = random.choices(tail_lengths, k=british_shorthair_mask.sum())

    dataset.to_excel(file_path, index=False)

    print(f"British Shorthair traits added to the dataset")
