import tkinter as tk
from tkinter import filedialog


def select_file():
    """
        Opens a file dialog and returns the path of the selected file.

        Returns:
            str: The selected file path, or an empty string if no file is selected.
    """
    root = tk.Tk()
    root.title("Select file")
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select file",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    return file_path


def read_text():
    """
    Reads text from command line input or a file.
    """
    while True:
        print("Choose input method:\n(1) Command line\n(2) File")
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            text = input("Enter your text: ")
            return text
        elif choice == '2':
            file_path = select_file()

            if not file_path:
                print("No file selected.")
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    print("\n")
                    print(text)
                    return text
            except FileNotFoundError:
                print(f"File {file_path} not found.")
            except PermissionError:
                print(f"Permission denied to read the file {file_path}.")
            except Exception as e:
                print(f"Error reading the file: {str(e)}")
        else:
            print("Invalid choice.")
