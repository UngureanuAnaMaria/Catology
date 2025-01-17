import openai
import numpy as np
from colorama import Fore, Style
from classifiers.random_forest_classifier import *
from classifiers.neural_network import NeuralNetwork, predict_breed, preprocess_data
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

openai.api_key = "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"


def generate_breed_description(breed):
    prompt = (
        f"Write a precise, detailed description of the {breed} cat breed, including its physical traits such as coat color, "
        f"body structure, and eyes, as well as its personality, behavior, origin, and any distinct characteristics that "
        f"differentiate it from other cat breeds."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant specialized in cat breeds."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000,
        top_p=0.9,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )

    return response.choices[0].message['content']


def apply():
    current_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(current_dir, '..'))
    file_path = os.path.join(project_root, 'Catology.xlsx')
    dataset = pd.read_excel(file_path)

    breed_order = [
        "Bengal", "Savannah", "Siamese", "Birman", "Ragdoll", "Chartreux",
        "British Shorthair", "Turkish Angora", "Persian", "Maine Coon",
        "European Shorthair", "Sphynx"
    ]

    bengal_rf= np.array([
        0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0,
        0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0,
        0.0
    ])

    bengal_nn = np.array([
        0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0,
        0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0,
        0.0
    ])

    european_shorthair_rf = np.array([
        1.0, 2.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0
    ])

    european_shorthair_nn = np.array([
        0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0
    ])

    persian_rf = np.array([
        1.0, 2.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0,
        1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
    ])

    persian_nn = np.array([
        0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0,
        1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0
    ])

    while True:
        print(f"""
        {Fore.BLUE}1.{Style.RESET_ALL} Generate Breed Description Random Forest
        {Fore.BLUE}2.{Style.RESET_ALL} Generate Breed Description Neural Network
        {Fore.RED}3.{Style.RESET_ALL} Exit
        """)

        choice = input("Please choose the desired option: ")

        if choice == '1':
            rf_model = random_forest_classifier(dataset)
            predicted_breed_index = predict_breed_rf(rf_model, bengal_rf)

            predicted_breed = breed_order[int(predicted_breed_index)]
            print(f"The predicted breed is: {predicted_breed}")

            generated_description = generate_breed_description(predicted_breed)
            print(generated_description)
        elif choice == '2':
            X_scaled, y_encoded, encoder, scaler = preprocess_data(dataset)

            current_dir = os.path.dirname(__file__)
            project_root = os.path.abspath(os.path.join(current_dir, '..'))
            model_path = os.path.join(project_root, 'classifiers', 'neural_network_model.pkl')

            nn_model= NeuralNetwork.load_model(model_path)

            X_test_scaled = scaler.transform(bengal_nn.reshape(1, -1))

            predicted_breed_index = predict_breed(nn_model, encoder, X_test_scaled)

            predicted_breed = breed_order[int(predicted_breed_index)]

            print(f"The predicted breed is: {predicted_breed}")

            generated_description = generate_breed_description(predicted_breed)
            print(generated_description)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

apply()
