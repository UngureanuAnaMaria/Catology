import pandas as pd
import random


def add_sphynx_traits(file_path):
    """
    Special Conditions for Sphynx cats:
        - **Eye Color**:
            - Can be "Blue", "Green", "Gold", "Copper".
            - Distribution: Equal distribution among all colors (25% each).
    """

    dataset = pd.read_excel(file_path)

    eye_colors = ["Blue", "Green", "Gold", "Copper"]

    eye_color_distribution = {color: 0.25 for color in eye_colors}

    sphynx_mask = dataset["Breed"] == "Sphynx"

    dataset.loc[sphynx_mask, "Coat Color"] = "Skin-toned"
    dataset.loc[sphynx_mask, "Coat Pattern"] = "No Pattern"
    dataset.loc[sphynx_mask, "Coat Length"] = "Hairless"
    dataset.loc[sphynx_mask, "Coat Texture"] = "Smooth"
    dataset.loc[sphynx_mask, "Size"] = "Medium"
    dataset.loc[sphynx_mask, "Body Type"] = "Muscular and Athletic"
    dataset.loc[sphynx_mask, "Leg Length"] = "Medium"
    dataset.loc[sphynx_mask, "Face Shape"] = "Wedge-shaped"
    dataset.loc[sphynx_mask, "Eye Color"] = random.choices(
        eye_colors, weights=[eye_color_distribution[color] for color in eye_colors],
        k=sphynx_mask.sum()
    )
    dataset.loc[sphynx_mask, "Eye Shape"] = "Almond-shaped"
    dataset.loc[sphynx_mask, "Ear Size"] = "Very Big"
    dataset.loc[sphynx_mask, "Ear Shape"] = "Pointed"
    dataset.loc[sphynx_mask, "Tail Shape"] = "Straight and Whip-like"
    dataset.loc[sphynx_mask, "Tail Length"] = "Medium"

    dataset.to_excel(file_path, index=False)

    print(f"Sphynx traits added to the dataset")
