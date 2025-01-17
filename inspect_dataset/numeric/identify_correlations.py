import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def analyze_correlations(file_path):
    """
    Analyzes the correlations between the attributes and the target `Breed` in the dataset.

    The Pearson correlation coefficient measures the linear relationship between two variables.
    Its values range from -1 to 1:
        - 1: Perfect positive correlation (as one variable increases, the other also increases proportionally).
        - 0: No linear correlation.
        - -1: Perfect negative correlation (as one variable increases, the other decreases proportionally).

    This function computes the correlation matrix of the dataset, extracts the correlations with the `Breed` column,
    and visualizes the top 10 correlations in a bar chart.
    """

    data = pd.read_excel(file_path)

    correlation_matrix = data.corr()

    breed_correlations = correlation_matrix["Breed"].drop("Breed")

    breed_correlations_sorted = breed_correlations.abs().sort_values(ascending=False)

    print("Top 10 correlations with the `Breed` class:\n")
    print(breed_correlations_sorted.head(10))

    plt.figure(figsize=(10, 6))
    breed_correlations_sorted.head(10).plot(kind="bar", color="skyblue")
    plt.title("\nTop Correlations Between Attributes and `Breed` Class")
    plt.xlabel("Attributes")
    plt.ylabel("Pearson Correlation Coefficient")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
file_path = os.path.join(project_root, 'Catology.xlsx')

analyze_correlations(file_path)
