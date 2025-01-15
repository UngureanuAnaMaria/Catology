import pandas as pd
import random


def add_chartreux_traits(file_path):
    """
    Special Conditions for Chartreux cats:
        - **Eye Color**:
            - Can be "Copper", "Gold", or "Orange".
            - Distribution: "Copper" (40%), "Gold" (35%), "Orange" (25%).
    """

    dataset = pd.read_excel(file_path)

    eye_colors = ["Copper", "Gold", "Orange"]

    eye_color_distribution = {
        "Copper": 0.4,
        "Gold": 0.35,
        "Orange": 0.25
    }

    chartreux_mask = dataset["Breed"] == "Chartreux"

    dataset.loc[chartreux_mask, "Coat Color"] = "Blue-gray"
    dataset.loc[chartreux_mask, "Coat Pattern"] = "Solid"
    dataset.loc[chartreux_mask, "Coat Length"] = "Short"
    dataset.loc[chartreux_mask, "Coat Texture"] = "Dense and Woolly"
    dataset.loc[chartreux_mask, "Size"] = "Medium"
    dataset.loc[chartreux_mask, "Body Type"] = "Cobby"
    dataset.loc[chartreux_mask, "Leg Length"] = "Medium"
    dataset.loc[chartreux_mask, "Face Shape"] = "Rounded"
    dataset.loc[chartreux_mask, "Eye Color"] = random.choices(
        eye_colors, weights=[eye_color_distribution[color] for color in eye_colors], k=chartreux_mask.sum()
    )
    dataset.loc[chartreux_mask, "Eye Shape"] = "Round"
    dataset.loc[chartreux_mask, "Ear Size"] = "Medium"
    dataset.loc[chartreux_mask, "Ear Shape"] = "Rounded"
    dataset.loc[chartreux_mask, "Tail Shape"] = "Straight and Slightly Curved"
    dataset.loc[chartreux_mask, "Tail Length"] = "Medium"

    dataset.to_excel(file_path, index=False)

    print(f"Chartreux traits added to the dataset")
