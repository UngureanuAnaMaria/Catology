import json

behavioral_mapping = {
    "Shy": ["Yes", "No"],
    "Calm": ["Yes", "No"],
    "Fearful": ["Yes", "No"],
    "Intelligent": ["Yes", "No"],
    "Vigilant": ["Yes", "No"],
    "Perseverant": ["Yes", "No"],
    "Affectionate": ["Yes", "No"],
    "Friendly": ["Yes", "No"],
    "Solitary": ["Yes", "No"],
    "Brutal": ["Yes", "No"],
    "Dominant": ["Yes", "No"],
    "Aggressive": ["Yes", "No"],
    "Impulsive": ["Yes", "No"],
    "Predictable": ["Yes", "No"],
    "Distracted": ["Yes", "No"]
}

unique_physical_attribute_mapping = {
    "Coat Color": ["White", "Cream", "Snow", "Silver",
                   "Cream and Seal", "Cream and Chocolate", "Cream and Blue", "Cream and Lilac",
                   "Blue", "Blue-gray", "Red", "Tabby", "Brown Tabby", "Brown", "Black", "Tortoiseshell", "Skin-toned"],
    "Coat Pattern": ["Rosetted", "Spotted", "Mitted", "Color-Point", "Bicolor", "Solid",
                     "Tabby", "Harlequin", "Tortie", "No Pattern"],
    "Coat Length": ["Short", "Medium", "Long", "Hairless"],
    "Coat Texture": ["Sleek", "Silky", "Plush", "Dense and Plush", "Dense and Woolly",
                     "Slightly Coarse", "Luxurious", "Smooth"],
    "Size": ["Small", "Medium", "Big", "Very Big"],
    "Body Type": ["Muscular and Athletic", "Long and Lean", "Cobby"],
    "Leg Length": ["Short", "Medium", "Long"],
    "Face Shape": ["Flat", "Wedge-shaped", "Rounded", "Round", "Square"],
    "Eye Shape": ["Almond-shaped", "Oval", "Round"],
    "Eye Color": ["Blue", "Green", "Blue-green", "Gold", "Yellow", "Copper", "Orange", "Odd-eyed", "Hazel", "Amber"],
    "Ear Size": ["Small", "Medium", "Big", "Very Big"],
    "Ear Shape": ["Rounded", "Pointed", "Triangular", "Tufted"],
    "Tail Shape": ["Plume and Straight", "Straight and Whip-like", "Tapered and Whip-like",
                   "Straight and Slightly Curved", "Straight and Tapered"],
    "Tail Length": ["Short", "Medium", "Long"]
}


with open("most_common_values.json", "r") as file:
    most_common_values = json.load(file)


def fill_missing_traits(traits, most_common_attribute_values):
    return {
        key: (value if value != "Unknown" else most_common_attribute_values.get(key, "Unknown"))
        for key, value in traits.items()
    }


def generate_output(all_traits_filled, unique_physical_attribute_mapping_, behavioral_mapping_):
    output = {}

    # for trait, values in behavioral_mapping_.items():
    #    output[trait] = 1 if all_traits_filled.get(trait, "No") == "Yes" else 0

    for physical_trait, possible_values in unique_physical_attribute_mapping_.items():
        value = all_traits_filled.get(physical_trait, "Unknown")
        for possible_value in possible_values:
            column_name = f"{physical_trait}: {possible_value}"
            output[column_name] = 1 if value == possible_value else 0

    return output
