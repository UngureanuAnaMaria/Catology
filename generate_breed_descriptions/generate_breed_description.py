import openai
import pandas as pd
import numpy as np
from colorama import Fore, Style
from classifiers.random_forest_classifier import *
from classifiers.neural_network import NeuralNetwork, predict_breed, preprocess_data

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
    file_path = r"C:\Users\anaun\OneDrive\Desktop\CatologyProject\Catology.xlsx"
    dataset = pd.read_excel(file_path)

    breed_order = [
        "Bengal", "Savannah", "Siamese", "Birman", "Ragdoll", "Chartreux",
        "British Shorthair", "Turkish Angora", "Persian", "Maine Coon",
        "European Shorthair", "Sphynx"
    ]

    new_cat_features_0 = np.array([
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

    new_cat_features_10_2 = np.array([
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

    new_cat_features_10 = np.array([
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

    new_cat_features_8 = np.array([
        1.0, 2.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0,
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

    new_cat_features_8_2 = np.array([
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
            predicted_breed_index = predict_breed_rf(rf_model, new_cat_features_8)

            predicted_breed = breed_order[int(predicted_breed_index)]
            print(f"The predicted breed is: {predicted_breed}")

            generated_description = generate_breed_description(predicted_breed)
            print(generated_description)
        elif choice == '2':
            X_scaled, y_encoded, encoder, scaler = preprocess_data(dataset)

            input_size = X_scaled.shape[1]
            hidden_sizes = [64, 32]
            output_size = y_encoded.shape[1]

            nn_model = NeuralNetwork(input_size, hidden_sizes, output_size)
            nn_model.train(X_scaled, y_encoded, X_scaled, y_encoded, epochs=40, learning_rate=0.003)

            predicted_breed_index = predict_breed(nn_model, encoder, new_cat_features_10_2)

            predicted_breed = breed_order[int(predicted_breed_index)]

            print(f"The predicted breed is: {predicted_breed}")

            generated_description = generate_breed_description(predicted_breed)
            print(generated_description)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

apply()
