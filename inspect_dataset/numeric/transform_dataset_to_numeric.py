import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def transform_to_numeric_with_prefix(file_path):
    """
    This function transforms a dataset with categorical data into a fully numeric dataset.
    It uses OneHotEncoding for categorical attributes and includes prefixes for clarity.
    """

    data = pd.read_excel(file_path)

    sex_mapping = {"F": 0, "M": 1}
    age_mapping = {"Less than 1 year": 0, "1-2 years": 1, "2-10 years": 2, "More than 10 years": 3}
    data["Sex"] = data["Sex"].map(sex_mapping)
    data["Age"] = data["Age"].map(age_mapping)

    behavior_columns = ["Shy", "Calm", "Fearful", "Intelligent", "Vigilant", "Perseverant",
                        "Affectionate", "Friendly", "Solitary", "Brutal", "Dominant",
                        "Aggressive", "Impulsive", "Predictable", "Distracted"]
    for col in behavior_columns:
        data[col] = data[col].map({"Yes": 1, "No": 0})

    categories_with_prefixes = {
        "Coat Color": ["White", "Cream", "Snow", "Silver", "Cream and Seal", "Cream and Chocolate",
                       "Cream and Blue", "Cream and Lilac", "Blue", "Blue-gray", "Red", "Tabby",
                       "Brown Tabby", "Brown", "Black", "Tortoiseshell", "Skin-toned"],
        "Coat Pattern": ["Rosetted", "Spotted", "Mitted", "Color-Point", "Bicolor", "Solid", "Tabby",
                         "Harlequin", "Tortie", "No Pattern"],
        "Coat Length": ["Short", "Medium", "Long", "Hairless"],
        "Coat Texture": ["Sleek", "Silky", "Plush", "Dense and Plush", "Dense and Woolly", "Slightly Coarse",
                         "Luxurious", "Smooth"],
        "Size": ["Small", "Medium", "Big", "Very Big"],
        "Body Type": ["Muscular and Athletic", "Long and Lean", "Cobby"],
        "Leg Length": ["Short", "Medium", "Long"],
        "Face Shape": ["Flat", "Wedge-shaped", "Rounded", "Round", "Square"],
        "Eye Shape": ["Almond-shaped", "Oval", "Round"],
        "Eye Color": ["Blue", "Green", "Blue-green", "Gold", "Yellow", "Copper",
                      "Orange", "Odd-eyed", "Hazel", "Amber"],
        "Ear Size": ["Small", "Medium", "Big", "Very Big"],
        "Ear Shape": ["Rounded", "Pointed", "Triangular", "Tufted"],
        "Tail Shape": ["Plume and Straight", "Straight and Whip-like", "Tapered and Whip-like",
                       "Straight and Slightly Curved", "Straight and Tapered"],
        "Tail Length": ["Short", "Medium", "Long"]
    }

    for column, categories in categories_with_prefixes.items():
        prefix = column
        encoder = OneHotEncoder(categories=[categories], sparse_output=False)
        encoded = encoder.fit_transform(data[[column]])
        column_names = [f"{prefix}: {category}" for category in categories]
        encoded_df = pd.DataFrame(encoded, columns=column_names)
        data = pd.concat([data, encoded_df], axis=1).drop(columns=[column])

    breed_mapping = {"Bengal": 0, "Savannah": 1, "Siamese": 2, "Birman": 3, "Ragdoll": 4, "Chartreux": 5,
                     "British Shorthair": 6, "Turkish Angora": 7, "Persian": 8, "Maine Coon": 9,
                     "European Shorthair": 10, "Sphynx": 11}
    data["Breed"] = data["Breed"].map(breed_mapping)

    data.to_excel(file_path, index=False)

    print("The dataset successfully transformed from non-numeric to numeric")


transform_to_numeric_with_prefix(r"C:\\Users\\User\\Desktop\\Catology.xlsx")
