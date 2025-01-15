import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, accuracy_score


def random_forest_classifier(data):
    X = data.drop(columns='Breed')
    y = data['Breed']

    rf_clf = RandomForestClassifier(
        n_estimators=100,
        max_depth=4,
        min_samples_split=20,
        min_samples_leaf=10,
        random_state=42
    )

    cv_scores = cross_val_score(rf_clf, X, y, cv=5, scoring='accuracy')

    print(f"Average Accuracy across 5-fold CV: {cv_scores.mean():.4f}")

    rf_clf.fit(X, y)

    y_pred = rf_clf.predict(X)

    print(f"Training Accuracy: {accuracy_score(y, y_pred):.4f}")
    print("Classification Report (Train Set):")
    print(classification_report(y, y_pred, zero_division=1))

    return rf_clf


def predict_breed_rf(model, instance):
    predicted_breed = model.predict([instance])
    return predicted_breed[0]


