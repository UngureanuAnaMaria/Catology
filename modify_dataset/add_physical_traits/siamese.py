import pandas as pd
import random


def add_siamese_traits(file_path):
    """
    Special Conditions for Siamese cats:
        - **Size**:
            - If Sex is "M" (male), there is a 60% chance for "Medium" and a 40% chance for "Small".
            - If Sex is "F" (female), there is a 60% chance for "Small" and a 40% chance for "Medium".
        - **Coat Color**: Siamese cats can have four main coat color variations:
            Cream and Seal, Cream and Chocolate, Cream and Blue, and Cream and Lilac.
            - "Cream and Seal" is the most common color: 50%
            - "Cream and Chocolate" is also common: 30%
            - "Cream and Blue" is less common: 15%
            - "Cream and Lilac" is very rare: 5%
    """

    dataset = pd.read_excel(file_path)

    sizes = ["Small", "Medium"]
    tail_lengths = ["Medium", "Long"]

    coat_colors = {
        "Cream and Seal": 0.5,
        "Cream and Chocolate": 0.3,
        "Cream and Blue": 0.15,
        "Cream and Lilac": 0.05
    }

    def get_coat_color():
        return random.choices(list(coat_colors.keys()), weights=list(coat_colors.values()))[0]

    def get_size(sex):
        if sex == "M":
            return random.choices(sizes, weights=[0.4, 0.6], k=1)[0]
        else:
            return random.choices(sizes, weights=[0.6, 0.4], k=1)[0]

    siamese_mask = dataset["Breed"] == "Siamese"

    dataset.loc[siamese_mask, "Coat Color"] = [
        get_coat_color() for _ in range(siamese_mask.sum())
    ]
    dataset.loc[siamese_mask, "Coat Pattern"] = "Color-Point"
    dataset.loc[siamese_mask, "Coat Length"] = "Short"
    dataset.loc[siamese_mask, "Coat Texture"] = "Sleek"
    dataset.loc[siamese_mask, "Size"] = [get_size(sex) for sex in dataset.loc[siamese_mask, "Sex"]]
    dataset.loc[siamese_mask, "Body Type"] = "Long and Lean"
    dataset.loc[siamese_mask, "Leg Length"] = "Long"
    dataset.loc[siamese_mask, "Face Shape"] = "Wedge-shaped"
    dataset.loc[siamese_mask, "Eye Shape"] = "Almond-shaped"
    dataset.loc[siamese_mask, "Eye Color"] = "Blue"
    dataset.loc[siamese_mask, "Ear Size"] = "Big"
    dataset.loc[siamese_mask, "Ear Shape"] = "Triangular"
    dataset.loc[siamese_mask, "Tail Shape"] = "Tapered and Whip-like"
    dataset.loc[siamese_mask, "Tail Length"] = random.choices(tail_lengths, k=siamese_mask.sum())

    dataset.to_excel(file_path, index=False)

    print(f"Siamese traits added to the dataset")
