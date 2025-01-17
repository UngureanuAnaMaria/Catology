from colorama import Fore, Style
from compare_breeds_openai import compare_breeds_openai
from compare_breeds_by_traits import compare_breeds_by_traits

def compare_breeds():
    while True:
        print(f"""
        {Fore.BLUE}1. {Style.RESET_ALL} Compare breeds using AI
        {Fore.BLUE}2. {Style.RESET_ALL} Compare breeds using the data from database
        {Fore.RED}3. {Style.RESET_ALL} Exit
        """)

        choice = input("Please choose the desired option: ")

        if choice == '1':
            breed1 = input("Please provide the first breed: ")
            breed2 = input("Please provide the second breed: ")

            comparison = compare_breeds_openai(breed1, breed2)
            print(comparison)
        if choice == '2':
            breed1 = input("Please provide the first breed: ")
            breed2 = input("Please provide the second breed: ")

            comparison = compare_breeds_by_traits(breed1, breed2)
            print(comparison)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

compare_breeds()
