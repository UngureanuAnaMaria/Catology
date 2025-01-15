from inspect_dataset.non_numeric.display_breed_counts import display_breed_counts
from inspect_dataset.non_numeric.display_values_and_frequencies import display_values_and_frequencies
from inspect_dataset.non_numeric.check_duplicates import check_duplicates
from inspect_dataset.non_numeric.check_missing_values import check_missing_values
from inspect_dataset.non_numeric.plot_attribute_distributions import plot_behavioral_traits, plot_other_traits

from colorama import Fore, Style


def inspect_non_numeric_dataset():
    file_path = r"C:\Users\User\Desktop\Catology.xlsx"

    while True:
        print(f"""
        {Fore.BLUE}1.{Style.RESET_ALL} Check Dataset for Duplicates and Missing Values
        {Fore.BLUE}2.{Style.RESET_ALL} Display Number of Instances for Each Breed
        {Fore.BLUE}3.{Style.RESET_ALL} Display distinct values and their frequencies for each attribute
        {Fore.BLUE}4.{Style.RESET_ALL} Display Graphical Visualization of Attributes (Histograms)
        {Fore.RED}5.{Style.RESET_ALL} Exit
        """)

        choice = input("Please choose the desired option: ")

        if choice == '1':
            check_duplicates(file_path)
            check_missing_values(file_path)
        elif choice == '2':
            display_breed_counts(file_path)
        elif choice == '3':
            output_file_path = "values_and_frequencies.txt"
            display_values_and_frequencies(file_path, output_file_path)
        elif choice == '4':
            plot_behavioral_traits(file_path)
            plot_other_traits(file_path)
        elif choice == '5':
            break
        else:
            print(f"{Fore.RED}Invalid option. Please choose again.{Style.RESET_ALL}")


inspect_non_numeric_dataset()
