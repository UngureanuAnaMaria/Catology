from nlp.generate_new_text import generate_replaced_text
from nlp.read_text import read_text
from nlp.stylometric_analysis import stylometric_analysis
from nlp.generate_alternative_text import generate_alternative_text
from colorama import Fore, Style
import pycountry
from langdetect import detect


def apply_nlp():

    text = ""

    while True:
        print(f"""
        {Fore.BLUE}1.{Style.RESET_ALL} Read Text
        {Fore.BLUE}2.{Style.RESET_ALL} Detect Language
        {Fore.BLUE}3.{Style.RESET_ALL} Display Stylometry Information
        {Fore.BLUE}4.{Style.RESET_ALL} Generate Alternative Text
        {Fore.BLUE}5.{Style.RESET_ALL} Extract keywords and generate a sentence for each
        {Fore.RED}6.{Style.RESET_ALL} Exit
        """)

        choice = input("Please choose the desired option: ")

        if choice == '1':
            text = read_text()
        elif choice == '2':
            if text:
                """
                try:
                    result = detect_language(text)
                    print(result)
                except Exception as e:
                    print(f"Language detection failed: {e}")
                """

                lang = detect(text)
                lang_name = pycountry.languages.get(alpha_2=lang)

                print(lang, lang_name)
            else:
                print("Please provide a text first!")
        elif choice == '3':
            if text:
                try:
                    stylometric_analysis(text)
                except Exception as e:
                    print(f"Stylometric analysis failed: {e}")
            else:
                print("Please provide a text first!")
        elif choice == '4':
            if text:
                try:
                    modified_text = generate_alternative_text(text)
                    print(f"\n{Fore.GREEN}Original Text:{Style.RESET_ALL} {text}")
                    if modified_text == "None":
                        print("Please provide another text. The text you provided doesn't have enough words "
                              "with synonyms, antonyms, hypernyms to fulfill the 20% restriction.")
                    else:
                        print(f"\n{Fore.GREEN}Modified text:{Style.RESET_ALL} {modified_text}")
                except Exception as e:
                    print(f"\nGenerate alternative text failed: {e}")
                generate_replaced_text(text)
            else:
                print("\nPlease provide a text first!")
        elif choice == '5':
            print(f"{Fore.RED}Not enough RAM for this, go to Google Colab!{Style.RESET_ALL}")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please choose again.")


apply_nlp()
