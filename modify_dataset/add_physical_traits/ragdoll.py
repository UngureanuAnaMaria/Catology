import pandas as pd
import random


def add_ragdoll_traits(file_path):
    """
    Special Conditions for Ragdoll cats:
        - **Coat Color**: Ragdoll cats can have four main coat color variations:
            Cream and Seal, Cream and Chocolate, Cream and Blue, and Cream and Lilac.
            - "Cream and Seal" is the most common color: 40%
            - "Cream and Chocolate" is also common: 30%
            - "Cream and Blue" is less common: 20%
            - "Cream and Lilac" is much rarer: 10%
    """

    dataset = pd.read_excel(file_path)

    coat_patterns = ["Color-Point", "Mitted", "Bicolor"]
    leg_lengths = ["Medium", "Long"]

    coat_colors = {
        "Cream and Seal": 0.4,
        "Cream and Chocolate": 0.3,
        "Cream and Blue": 0.2,
        "Cream and Lilac": 0.1
    }

    def get_coat_color():
        return random.choices(list(coat_colors.keys()), weights=list(coat_colors.values()))[0]

    def get_leg_length():
        return random.choices(leg_lengths, weights=[0.5, 0.5], k=1)[0]

    ragdoll_mask = dataset["Breed"] == "Ragdoll"

    dataset.loc[ragdoll_mask, "Coat Color"] = [
        get_coat_color() for _ in range(ragdoll_mask.sum())
    ]
    dataset.loc[ragdoll_mask, "Coat Pattern"] = random.choices(coat_patterns, k=ragdoll_mask.sum())
    dataset.loc[ragdoll_mask, "Coat Length"] = "Medium"
    dataset.loc[ragdoll_mask, "Coat Texture"] = "Plush"
    dataset.loc[ragdoll_mask, "Size"] = "Big"
    dataset.loc[ragdoll_mask, "Body Type"] = "Cobby"
    dataset.loc[ragdoll_mask, "Leg Length"] = [get_leg_length() for _ in range(ragdoll_mask.sum())]
    dataset.loc[ragdoll_mask, "Face Shape"] = "Rounded"
    dataset.loc[ragdoll_mask, "Eye Shape"] = "Oval"
    dataset.loc[ragdoll_mask, "Eye Color"] = "Blue"
    dataset.loc[ragdoll_mask, "Ear Size"] = "Medium"
    dataset.loc[ragdoll_mask, "Ear Shape"] = "Rounded"
    dataset.loc[ragdoll_mask, "Tail Shape"] = "Plume and Straight"
    dataset.loc[ragdoll_mask, "Tail Length"] = "Long"

    dataset.to_excel(file_path, index=False)

    print(f"Ragdoll traits added to the dataset")
