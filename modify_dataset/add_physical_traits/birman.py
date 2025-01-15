import pandas as pd
import random


def add_birman_traits(file_path):
    """
    Special Conditions for Birman cats:
        - **Coat Color**:
            - "Cream and Seal": 40%
            - "Cream and Chocolate": 30%
            - "Cream and Blue": 20%
            - "Cream and Lilac": 10%
    """

    dataset = pd.read_excel(file_path)

    coat_colors = {
        "Cream and Seal": 0.4,
        "Cream and Chocolate": 0.3,
        "Cream and Blue": 0.2,
        "Cream and Lilac": 0.1
    }

    def get_coat_color():
        return random.choices(list(coat_colors.keys()), weights=list(coat_colors.values()))[0]

    birman_mask = dataset["Breed"] == "Birman"

    dataset.loc[birman_mask, "Coat Color"] = [
        get_coat_color() for _ in range(birman_mask.sum())
    ]
    dataset.loc[birman_mask, "Coat Pattern"] = "Mitted"
    dataset.loc[birman_mask, "Coat Length"] = "Medium"
    dataset.loc[birman_mask, "Coat Texture"] = "Silky"
    dataset.loc[birman_mask, "Size"] = "Medium"
    dataset.loc[birman_mask, "Body Type"] = "Cobby"
    dataset.loc[birman_mask, "Leg Length"] = "Medium"
    dataset.loc[birman_mask, "Face Shape"] = "Rounded"
    dataset.loc[birman_mask, "Eye Shape"] = "Almond-shaped"
    dataset.loc[birman_mask, "Eye Color"] = "Blue"
    dataset.loc[birman_mask, "Ear Size"] = "Medium"
    dataset.loc[birman_mask, "Ear Shape"] = "Rounded"
    dataset.loc[birman_mask, "Tail Shape"] = "Plume and Straight"
    dataset.loc[birman_mask, "Tail Length"] = "Medium"

    dataset.to_excel(file_path, index=False)

    print(f"Birman traits added to the dataset")
