import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pydotplus
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import StratifiedKFold
from io import StringIO


def decision_tree_classifier(data, n_splits=5):
    """
    This function trains and evaluates a decision tree classifier with regularization and pruning.
    The model is evaluated using k-fold cross-validation.

    Parameters:
    data (DataFrame): A pandas DataFrame containing the dataset. The target column must be 'Breed'.
    n_splits (int): The number of splits for cross-validation.

    Process:
    1. Limits the tree depth to prevent overfitting.
    2. Uses k-fold cross-validation to evaluate the model.
    3. Evaluates using accuracy, precision, recall, and f1-score.
    4. Performs pruning by adjusting parameters like min_samples_split and min_samples_leaf.
    """

    X = data.drop(columns=['Breed'])
    y = data['Breed']

    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    accuracy_train_scores = []
    accuracy_test_scores = []
    precision_scores = []
    recall_scores = []
    f1_scores = []

    for fold, (train_index, test_index) in enumerate(skf.split(X, y), start=1):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        clf = DecisionTreeClassifier(
            criterion='entropy',
            max_depth=4,
            min_samples_split=20,
            min_samples_leaf=10,
            random_state=42
        )
        clf.fit(X_train, y_train)

        y_train_pred = clf.predict(X_train)
        y_test_pred = clf.predict(X_test)

        accuracy_train = accuracy_score(y_train, y_train_pred)
        accuracy_test = accuracy_score(y_test, y_test_pred)

        accuracy_train_scores.append(accuracy_train)
        accuracy_test_scores.append(accuracy_test)
        precision_scores.append(precision_score(y_test, y_test_pred, average='weighted', zero_division=1))
        recall_scores.append(recall_score(y_test, y_test_pred, average='weighted', zero_division=1))
        f1_scores.append(f1_score(y_test, y_test_pred, average='weighted', zero_division=1))

        print(f"Fold {fold}: Training Accuracy: {accuracy_train:.4f}, Testing Accuracy: {accuracy_test:.4f}")

    print(f"\nAverage Training Accuracy across {n_splits}-fold CV: {np.mean(accuracy_train_scores):.4f}")
    print(f"Average Testing Accuracy across {n_splits}-fold CV: {np.mean(accuracy_test_scores):.4f}")
    print(f"Average Precision across {n_splits}-fold CV: {np.mean(precision_scores):.4f}")
    print(f"Average Recall across {n_splits}-fold CV: {np.mean(recall_scores):.4f}")
    print(f"Average F1-score across {n_splits}-fold CV: {np.mean(f1_scores):.4f}")

    clf = DecisionTreeClassifier(
        criterion='entropy',
        max_depth=5,
        min_samples_split=20,
        min_samples_leaf=10,
        random_state=42
    )
    clf.fit(X, y)

    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True,
                    feature_names=X.columns.tolist(), class_names=[str(cls) for cls in clf.classes_])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('decision_tree_regularized.png')

    plt.figure(figsize=(20, 20))
    plt.imshow(plt.imread('decision_tree_regularized.png'))
    plt.axis("off")
    plt.show()


file_path = r"C:\Users\User\Desktop\Catology.xlsx"
dataset = pd.read_excel(file_path)
decision_tree_classifier(dataset)
