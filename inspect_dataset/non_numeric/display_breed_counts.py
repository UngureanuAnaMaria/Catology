import pandas as pd
from colorama import Fore, Style, init

init(autoreset=True)


def display_breed_counts(file_path):
    """
    Display the number of instances for each cat breed in the dataset.

    Parameters:
    - file_path (str): Path to the Excel file containing the dataset.
    """
    try:
        data = pd.read_excel(file_path)
        print(f"\nDataset loaded successfully from {file_path}.")

        if 'Breed' not in data.columns:
            print("Error: The dataset does not contain a 'Breed' column.")
            return

        breed_counts = data['Breed'].value_counts()
        total_instances = data['Breed'].count()

        print("\nNumber of instances for each breed:")
        for breed_name, count in breed_counts.items():
            percentage = (count / total_instances) * 100
            print(
                f"Breed: {Fore.GREEN}{breed_name}{Style.RESET_ALL}, "
                f"Count: {Fore.LIGHTRED_EX}{count}{Style.RESET_ALL}, "
                f"Percentage: {Fore.LIGHTRED_EX}{percentage:.2f}%{Style.RESET_ALL}"
            )

        print(f"\nTotal number of instances: {Fore.LIGHTRED_EX}{total_instances}{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
