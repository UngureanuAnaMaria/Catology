import pandas as pd
import random


def add_bengal_traits(file_path):
    """
    Special Conditions for Bengal cats:
        - **Size**:
            - If Sex is "M" (male), there is a 60% chance for "Big" and a 40% chance for "Medium".
            - If Sex is "F" (female), there is a 60% chance for "Medium" and a 40% chance for "Big".
        - **Eye Color**:
            - If Coat Color is "Snow", Eye Color is always "Blue" (100%).
            - If Coat Color is "Brown", Eye Color distribution is as follows:
                - "Green": 50%
                - "Gold": 30%
                - "Yellow": 20%
            - If Coat Color is "Silver", Eye Color distribution is as follows:
                - "Green": 40%
                - "Gold": 40%
                - "Yellow": 20%
            - Default distribution for other cases:
                - "Green": 40%
                - "Gold": 30%
                - "Yellow": 20%
                - "Blue": 10%
    """

    dataset = pd.read_excel(file_path)

    coat_colors = ["Brown", "Snow", "Silver"]
    coat_patterns = ["Rosetted", "Spotted"]
    sizes = ["Medium", "Big"]
    eye_colors = {
        "conditions": {
            "Coat Color:Brown": {"Green": 0.5, "Gold": 0.3, "Yellow": 0.2},
            "Coat Color:Snow": {"Blue": 1.0},
            "Coat Color:Silver": {"Green": 0.4, "Gold": 0.4, "Yellow": 0.2}
        },
        "default": {"Green": 0.4, "Gold": 0.3, "Yellow": 0.2, "Blue": 0.1}
    }
    ear_sizes = ["Medium", "Big"]
    tail_lengths = ["Medium", "Long"]

    def get_eye_color(coat_color):
        if coat_color == "Snow":
            return "Blue"
        else:
            eye_distribution = eye_colors["default"]
            return random.choices(list(eye_distribution.keys()), weights=list(eye_distribution.values()))[0]

    def get_size(sex):
        if sex == "M":
            return random.choices(sizes, weights=[0.4, 0.6], k=1)[0]
        else:
            return random.choices(sizes, weights=[0.6, 0.4], k=1)[0]

    bengal_mask = dataset["Breed"] == "Bengal"

    dataset.loc[bengal_mask, "Coat Color"] = random.choices(coat_colors, k=bengal_mask.sum())
    dataset.loc[bengal_mask, "Coat Pattern"] = random.choices(coat_patterns, k=bengal_mask.sum())
    dataset.loc[bengal_mask, "Coat Length"] = "Short"
    dataset.loc[bengal_mask, "Coat Texture"] = "Sleek"
    dataset.loc[bengal_mask, "Size"] = [get_size(sex) for sex in dataset.loc[bengal_mask, "Sex"]]
    dataset.loc[bengal_mask, "Body Type"] = "Muscular and Athletic"
    dataset.loc[bengal_mask, "Leg Length"] = "Medium"
    dataset.loc[bengal_mask, "Face Shape"] = "Wedge-shaped"
    dataset.loc[bengal_mask, "Eye Shape"] = "Oval"
    dataset.loc[bengal_mask, "Eye Color"] = [
        get_eye_color(coat_color) for coat_color in dataset.loc[bengal_mask, "Coat Color"]
    ]
    dataset.loc[bengal_mask, "Ear Size"] = random.choices(ear_sizes, k=bengal_mask.sum())
    dataset.loc[bengal_mask, "Ear Shape"] = "Rounded"
    dataset.loc[bengal_mask, "Tail Shape"] = "Straight and Tapered"
    dataset.loc[bengal_mask, "Tail Length"] = random.choices(tail_lengths, k=bengal_mask.sum())

    dataset.to_excel(file_path, index=False)

    print(f"Bengal traits added to the dataset")
