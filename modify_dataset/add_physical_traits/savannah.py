import pandas as pd
import random


def add_savannah_traits(file_path):
    """
    Special Conditions for Savannah cats:
        - **Eye Color**:
            - If Coat Color is "Black", Eye Color distribution is as follows:
                - "Green": 40%
                - "Gold": 40%
                - "Yellow": 20%
            - If Coat Color is "Brown", Eye Color distribution is as follows:
                - "Green": 50%
                - "Gold": 30%
                - "Yellow": 10%
                - "Hazel": 10%
            - If Coat Color is "Silver", Eye Color distribution is as follows:
                - "Green": 60%
                - "Gold": 30%
                - "Yellow": 10%
        - **Size**:
            - If Sex is "M" (male), there is a 70% chance for "Very Big" and a 30% chance for "Big".
            - If Sex is "F" (female), there is a 60% chance for "Big" and a 40% chance for "Very Big".
    """

    dataset = pd.read_excel(file_path)

    coat_colors = ["Brown", "Black", "Silver"]
    sizes = ["Big", "Very Big"]
    eye_colors = {
        "conditions": {
            "Coat Color:Black": {"Green": 0.4, "Gold": 0.4, "Yellow": 0.2},
            "Coat Color:Brown": {"Green": 0.5, "Gold": 0.3, "Yellow": 0.1, "Hazel": 0.1},
            "Coat Color:Silver": {"Green": 0.6, "Gold": 0.3, "Yellow": 0.1}
        },
        "default": {"Green": 0.4, "Gold": 0.3, "Yellow": 0.2, "Hazel": 0.1}
    }
    tail_lengths = ["Medium", "Long"]

    def get_eye_color(coat_color):
        if coat_color == "Black":
            return random.choices(["Green", "Gold", "Yellow"], weights=[0.4, 0.4, 0.2])[0]
        elif coat_color == "Brown":
            return random.choices(["Green", "Gold", "Yellow", "Hazel"], weights=[0.5, 0.3, 0.1, 0.1])[0]
        elif coat_color == "Silver":
            return random.choices(["Green", "Gold", "Yellow"], weights=[0.6, 0.3, 0.1])[0]
        else:
            eye_distribution = eye_colors["default"]
            return random.choices(list(eye_distribution.keys()), weights=list(eye_distribution.values()))[0]

    def get_size(sex):
        if sex == "M":
            return random.choices(sizes, weights=[0.3, 0.7], k=1)[0]
        else:
            return random.choices(sizes, weights=[0.6, 0.4], k=1)[0]

    savannah_mask = dataset["Breed"] == "Savannah"

    dataset.loc[savannah_mask, "Coat Color"] = random.choices(coat_colors, k=savannah_mask.sum())
    dataset.loc[savannah_mask, "Coat Pattern"] = "Spotted"
    dataset.loc[savannah_mask, "Coat Length"] = "Short"
    dataset.loc[savannah_mask, "Coat Texture"] = "Sleek"
    dataset.loc[savannah_mask, "Size"] = [get_size(sex) for sex in dataset.loc[savannah_mask, "Sex"]]
    dataset.loc[savannah_mask, "Body Type"] = "Muscular and Athletic"
    dataset.loc[savannah_mask, "Leg Length"] = "Long"
    dataset.loc[savannah_mask, "Face Shape"] = "Wedge-shaped"
    dataset.loc[savannah_mask, "Eye Shape"] = "Almond-shaped"
    dataset.loc[savannah_mask, "Eye Color"] = [
        get_eye_color(coat_color) for coat_color in dataset.loc[savannah_mask, "Coat Color"]
    ]
    dataset.loc[savannah_mask, "Ear Size"] = "Very Big"
    dataset.loc[savannah_mask, "Ear Shape"] = "Pointed"
    dataset.loc[savannah_mask, "Tail Shape"] = "Straight and Tapered"
    dataset.loc[savannah_mask, "Tail Length"] = random.choices(tail_lengths, k=savannah_mask.sum())

    dataset.to_excel(file_path, index=False)

    print(f"Savannah traits added to the dataset")
