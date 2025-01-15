import pandas as pd
import random


def add_persian_traits(file_path):
    """
    Special Conditions for Persian cats:
        - **Coat Color**:
            - Can be "White", "Black", "Blue", "Cream", "Red", "Tabby", "Tortoiseshell".
            - Distribution: "White" (30%), others equally distributed (11.67% each).
        - **Coat Pattern**:
            - Can be "Solid", "Tabby", "Bicolor", or "Color-Point".
            - Distribution: "Solid" (50%), "Tabby" (20%), "Bicolor" (20%), "Color-Point" (10%).
        - **Size**:
            - Can be "Medium" or "Big".
            - Distribution: "Medium" (40%), "Big" (60%).
        - **Eye Color**:
            - Can be "Blue", "Copper", "Green", or "Odd-eyed".
            - Distribution: "Blue" (25%), "Copper" (35%), "Green" (20%), "Odd-eyed" (20%).
        - **Tail Length**:
            - Can be "Short" or "Medium".
            - Distribution: "Short" (60%), "Medium" (40%).
    """

    dataset = pd.read_excel(file_path)

    coat_colors = ["White", "Black", "Blue", "Cream", "Red", "Tabby", "Tortoiseshell"]
    coat_patterns = ["Solid", "Tabby", "Bicolor", "Color-Point"]
    sizes = ["Medium", "Big"]
    eye_colors = ["Blue", "Copper", "Green", "Odd-eyed"]
    tail_lengths = ["Short", "Medium"]

    coat_color_distribution = {
        "White": 0.3,
        "Black": 0.1167,
        "Blue": 0.1167,
        "Cream": 0.1167,
        "Red": 0.1167,
        "Tabby": 0.1167,
        "Tortoiseshell": 0.1167
    }
    coat_pattern_distribution = {
        "Solid": 0.5,
        "Tabby": 0.2,
        "Bicolor": 0.2,
        "Color-Point": 0.1
    }
    size_distribution = {"Medium": 0.4, "Big": 0.6}
    eye_color_distribution = {
        "Blue": 0.25,
        "Copper": 0.35,
        "Green": 0.2,
        "Odd-eyed": 0.2
    }
    tail_length_distribution = {"Short": 0.6, "Medium": 0.4}

    persian_mask = dataset["Breed"] == "Persian"

    dataset.loc[persian_mask, "Coat Color"] = random.choices(
        coat_colors, weights=[coat_color_distribution[color] for color in coat_colors],
        k=persian_mask.sum()
    )
    dataset.loc[persian_mask, "Coat Pattern"] = random.choices(
        coat_patterns, weights=[coat_pattern_distribution[pattern] for pattern in coat_patterns],
        k=persian_mask.sum()
    )
    dataset.loc[persian_mask, "Coat Length"] = "Long"
    dataset.loc[persian_mask, "Coat Texture"] = "Luxurious"
    dataset.loc[persian_mask, "Size"] = random.choices(
        sizes, weights=[size_distribution[size] for size in sizes],
        k=persian_mask.sum()
    )
    dataset.loc[persian_mask, "Body Type"] = "Cobby"
    dataset.loc[persian_mask, "Leg Length"] = "Short"
    dataset.loc[persian_mask, "Face Shape"] = "Flat"
    dataset.loc[persian_mask, "Eye Color"] = random.choices(
        eye_colors, weights=[eye_color_distribution[color] for color in eye_colors],
        k=persian_mask.sum()
    )
    dataset.loc[persian_mask, "Eye Shape"] = "Round"
    dataset.loc[persian_mask, "Ear Size"] = "Small"
    dataset.loc[persian_mask, "Ear Shape"] = "Rounded"
    dataset.loc[persian_mask, "Tail Shape"] = "Plume and Straight"
    dataset.loc[persian_mask, "Tail Length"] = random.choices(
        tail_lengths, weights=[tail_length_distribution[length] for length in tail_lengths],
        k=persian_mask.sum()
    )

    dataset.to_excel(file_path, index=False)

    print(f"Persian traits added to the dataset")
