import numpy as np
import os
import cv2
import tkinter as tk
from tkinter import filedialog
from colorama import Fore, Style
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

IMAGE_SIZE = (64, 64)
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
IMAGE_DIR = os.path.join(project_root, 'image_based_breed_classification', 'breed_images_dataset', 'images')
MODEL_FILE = os.path.join(project_root, 'image_based_breed_classification', 'cat_breed_classifier.keras')
SAVE_FILE = os.path.join(project_root, 'image_based_breed_classification', 'cat_images_data.npy')


def load_and_save_images(image_dir, save_file):
    if os.path.exists(save_file):
        print(f"Loading data from {save_file}...")
        data = np.load(save_file, allow_pickle=True).item()
        X = data['X']
        y_labels = data['y_labels']
    else:
        print(f"Loading data from scratch...")
        images = []
        y = []
        breeds = [breed for breed in os.listdir(image_dir) if os.path.isdir(os.path.join(image_dir, breed))]

        for breed in breeds:
            breed_dir = os.path.join(image_dir, breed)
            if not os.path.exists(breed_dir):
                continue
            for image_name in os.listdir(breed_dir):
                image_path = os.path.join(breed_dir, image_name)
                img = cv2.imread(image_path)
                print(image_path)
                if img is not None:
                    img = cv2.resize(img, IMAGE_SIZE)
                    images.append(img / 255.0)
                    y.append(breed)
                else:
                    print(f"Cannot read image: {image_path}")
                    continue
        X = np.array(images)
        y_labels = np.array(y)

        np.save(save_file, {'X': X, 'y_labels': y_labels})
        print(f"Data saved to {save_file}")

    return X, y_labels


X, y_labels = load_and_save_images(IMAGE_DIR, SAVE_FILE)

unique_labels = sorted(set(y_labels))
label_to_index = {label: index for index, label in enumerate(unique_labels)}
y = np.array([label_to_index[label] for label in y_labels])
print(y)

y_one_hot = to_categorical(y, num_classes=len(unique_labels))
print(y_one_hot)

X_train, X_temp, y_train, y_temp = train_test_split(X, y_one_hot, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

if os.path.exists(MODEL_FILE):
    print(f"Loading model from {MODEL_FILE}...")
    model = load_model(MODEL_FILE)
else:
    print(f"Construct model...")

    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(len(unique_labels), activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=20,
        batch_size=32
    )

    model.save(MODEL_FILE)
    print(f"Model saved to {MODEL_FILE}")

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy * 100:.2f}%")


def predict_image(image_path, model, label_map):
    img = cv2.imread(image_path)
    img = cv2.resize(img, IMAGE_SIZE)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    predicted_label = label_map[np.argmax(prediction)]
    return predicted_label


def select_and_predict():
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;")]
    )

    if not image_path:
        print("No image selected!")
        return

    print(f"Selected image: {image_path}")

    predicted_breed = predict_image(image_path, model, {index: label for label, index in label_to_index.items()})
    print(f"Predicted race: {predicted_breed}")


def breed_by_image():
    while True:
        print(f"""
        {Fore.BLUE}1.{Style.RESET_ALL} Predict breed by image
        {Fore.RED}2. {Style.RESET_ALL} Exit
        """)

        choice = input("Please choose the desired option: ")

        if choice == '1':
            select_and_predict()
        elif choice == '2':
            break
        else:
            print("Invalid option. Please choose again.")

breed_by_image()

