import pandas as pd
from collections import Counter
from combine_attributes import *
from extract_character_attributes import extract_character_attributes
from classifiers.neural_network import *
from extract_physical_attributes import extract_physical_attributes
import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


breed_mapping = {
    0: "Bengal",
    1: "Savannah",
    2: "Siamese",
    3: "Birman",
    4: "Ragdoll",
    5: "Chartreux",
    6: "British Shorthair",
    7: "Turkish Angora",
    8: "Persian",
    9: "Maine Coon",
    10: "European Shorthair",
    11: "Sphynx"
}

# Savannah
savannah_description = (
    "This cat has a beautiful black coat. "
    "This cat has a sleek, short coat with a spotted pattern, which stands out against its muscular and "
    "athletic body. Its face is wedge-shaped, and it has almond-shaped eyes in a shade of green. "
    "The cat has very big ears and pointed ears, complementing its alert and energetic expression. "
    "The tail is straight and tapered, and it has long legs, giving the cat "
    "an elegant yet powerful stance. The cat is of a very big size, with an impressive presence. "
    "This cat has a long tail."
)

bengal_description = (
    """The Bengal cat has a striking coat with a pattern of rosettes or marbling, resembling a wild leopard's fur. 
    Its short, dense fur complements its muscular, athletic body. With a triangular face, sharp features, 
    and almond-shaped green or gold eyes, the Bengal has an intense gaze. Large, rounded ears enhance its 
    wild appearance. It moves with agility, thanks to its long legs and sleek, tapering tail. Medium to large 
    in size, the Bengal is energetic, playful, and curious, making it an engaging companion."""
)


# character_traits = extract_character_attributes(cat_description)
physical_traits = extract_physical_attributes(bengal_description)

# all_traits = {**character_traits, **physical_traits}
all_traits = {**physical_traits}
print(all_traits)

all_traits_filled = fill_missing_traits(all_traits, most_common_values)
print(all_traits_filled)

output_dict = generate_output(all_traits_filled, unique_physical_attribute_mapping, behavioral_mapping)

with open("cat_traits_output.txt", "w") as file:
    for key, value in output_dict.items():
        file.write(f"{key}: {value}\n")


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
file_path = os.path.join(project_root, 'Catology_identify_cat_breed.xlsx')
dataset = (pd.read_excel(file_path))
# X, y, scaler, encoder = preprocess_data(dataset)
#
# output_df = pd.DataFrame(output_dict, index=[0])
#
# X_test_instance = preprocess_single_instance(output_df.iloc[0], scaler, encoder)
#
# current_dir = os.path.dirname(__file__)
# project_root = os.path.abspath(os.path.join(current_dir, '..'))
# model_path = os.path.join(project_root, 'classifiers', 'neural_network_model.pkl')
#
# nn = NeuralNetwork.load_model(model_path)
#
# prediction = nn.predict(X_test_instance)
# predicted_class = encoder.inverse_transform([np.argmax(prediction)])
#
# predicted_breed = breed_mapping[predicted_class[0]]
# print("Predicted Breed for the test instance:", predicted_breed)

breed_order = [
        "Bengal", "Savannah", "Siamese", "Birman", "Ragdoll", "Chartreux",
        "British Shorthair", "Turkish Angora", "Persian", "Maine Coon",
        "European Shorthair", "Sphynx"
    ]

X_scaled, y_encoded, encoder, scaler = preprocess_data(dataset)

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
model_path = os.path.join(project_root, 'classifiers', 'neural_network_model.pkl')

nn_model= NeuralNetwork.load_model(model_path)

output_df = pd.DataFrame(output_dict, index=[0])

X_test_instance = preprocess_single_instance(output_df.iloc[0], scaler, encoder)

X_test_scaled = scaler.transform(X_test_instance.reshape(1, -1))

predicted_breed_index = predict_breed(nn_model, encoder, X_test_scaled)

predicted_breed = breed_order[int(predicted_breed_index)]

print(f"The predicted breed is: {predicted_breed}")


