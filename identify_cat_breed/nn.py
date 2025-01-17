import os
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

def sigmoid(Z):
    return 1 / (1 + np.exp(-np.clip(Z, -500, 500)))


def relu(Z):
    return np.maximum(0, Z)


def sigmoid_derivative(Z):
    return Z * (1 - Z)


def relu_derivative(Z):
    return Z > 0


def initialize_parameters(layer_dims):
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)
    for i in range(1, L):
        parameters['W' + str(i)] = np.random.randn(layer_dims[i], layer_dims[i - 1]) * np.sqrt(2 / layer_dims[i - 1])
        parameters['b' + str(i)] = np.zeros((layer_dims[i], 1))
    return parameters


def linear_forward(A_prev, W, b):
    Z = np.dot(W, A_prev) + b
    return Z


def L_layer_forward(X, parameters):
    A = X
    caches = []
    L = len(parameters) // 2
    for i in range(1, L):
        A_prev = A
        W = parameters['W' + str(i)]
        b = parameters['b' + str(i)]
        Z = linear_forward(A_prev, W, b)
        A = relu(Z)
        cache = (A_prev, W, b, Z)
        caches.append(cache)

    W_out = parameters['W' + str(L)]
    b_out = parameters['b' + str(L)]
    Z_out = linear_forward(A, W_out, b_out)
    AL = sigmoid(Z_out)
    return AL, caches


class NeuralNetwork:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes
        self.output_size = output_size
        self.weights = []
        self.biases = []

        self.weights.append(np.random.randn(self.input_size, self.hidden_sizes[0]))
        self.biases.append(np.zeros((1, self.hidden_sizes[0])))

        for i in range(len(self.hidden_sizes) - 1):
            self.weights.append(np.random.randn(self.hidden_sizes[i], self.hidden_sizes[i + 1]))
            self.biases.append(np.zeros((1, self.hidden_sizes[i + 1])))

        self.weights.append(np.random.randn(self.hidden_sizes[-1], self.output_size))
        self.biases.append(np.zeros((1, self.output_size)))

    def feedforward(self, X):
        self.hidden_outputs = []
        activation = X

        for i in range(len(self.hidden_sizes)):
            activation = relu(np.dot(activation, self.weights[i]) + self.biases[i])
            self.hidden_outputs.append(activation)

        output_activation = np.dot(activation, self.weights[-1]) + self.biases[-1]
        self.predicted_output = sigmoid(output_activation)

        return self.predicted_output

    def backward(self, X, y, learning_rate):
        output_error = self.predicted_output - y
        output_delta = output_error

        deltas = [output_delta]
        for i in range(len(self.hidden_sizes) - 1, -1, -1):
            hidden_error = np.dot(deltas[-1], self.weights[i + 1].T)
            hidden_delta = hidden_error * relu_derivative(self.hidden_outputs[i])
            deltas.append(hidden_delta)

        deltas.reverse()

        for i in range(1, len(self.weights)):
            self.weights[i] -= np.dot(self.hidden_outputs[i - 1].T if i > 0 else X.T, deltas[i]) * learning_rate
            self.biases[i] -= np.sum(deltas[i], axis=0, keepdims=True) * learning_rate

    def calculate_loss(self, y_true, y_pred):
        return -np.mean(np.sum(y_true * np.log(y_pred + 1e-9), axis=1))

    def calculate_accuracy(self, y_true, y_pred):
        predictions = np.argmax(y_pred, axis=1)
        labels = np.argmax(y_true, axis=1)
        return np.mean(predictions == labels)

    def train(self, X_train, y_train, X_test, y_test, batch_size=32, X_val=None, y_val=None, epochs=40,
              learning_rate=0.1):
        train_losses = []
        val_losses = []
        test_losses = []
        test_accuracies = []

        for epoch in range(epochs):
            X_train, y_train = shuffle(X_train, y_train)
            for i in range(0, len(X_train), batch_size):
                X_batch = X_train[i:i + batch_size]
                y_batch = y_train[i:i + batch_size]
                self.feedforward(X_batch)
                self.backward(X_batch, y_batch, learning_rate)

            train_loss = self.calculate_loss(y_train, self.feedforward(X_train))
            train_losses.append(train_loss)

            test_loss = self.calculate_loss(y_test, self.feedforward(X_test))
            test_accuracy = self.calculate_accuracy(y_test, self.feedforward(X_test))
            test_losses.append(test_loss)
            test_accuracies.append(test_accuracy)

            if X_val is not None and y_val is not None:
                val_loss = self.calculate_loss(y_val, self.feedforward(X_val))
                val_losses.append(val_loss)

    def predict(self, X):
        return self.feedforward(X)

    def save_model(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)
        print(f"Model saved to {file_path}.")

    @staticmethod
    def load_model(file_path):
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        print(f"Model loaded from {file_path}.")
        return model


def preprocess_data(dataset):
    X = dataset.drop(
        columns=['Breed', 'Sex', 'Age', 'Shy', 'Calm', 'Fearful', 'Intelligent', 'Vigilant',
                 'Perseverant', 'Affectionate', 'Friendly', 'Solitary', 'Brutal', 'Dominant',
                 'Aggressive', 'Impulsive', 'Predictable', 'Distracted']).values
    y = dataset['Breed'].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    y_encoded = np.eye(len(np.unique(y_encoded)))[y_encoded]

    return X_scaled, y_encoded, scaler, encoder


def preprocess_single_instance(instance, scaler, encoder):
    instance_scaled = scaler.transform([instance])
    return instance_scaled


# current_dir = os.path.dirname(__file__)
# project_root = os.path.abspath(os.path.join(current_dir, '..'))
# file_path = os.path.join(project_root, 'Catology.xlsx')
#
# dataset = pd.read_excel(file_path)
# X, y, encoder, scaler = preprocess_data(dataset)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
#
# input_size = X_train.shape[1]
# hidden_sizes = [64, 32]
# output_size = y_train.shape[1]
#
# nn = NeuralNetwork(input_size, hidden_sizes, output_size)
# nn.train(X_train, y_train, X_test, y_test, epochs=40, learning_rate=0.003)
#
# model_file_path = "neural_network_model.pkl"
# nn.save_model(model_file_path)