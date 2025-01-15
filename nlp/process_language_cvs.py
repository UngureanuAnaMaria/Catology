import pandas as pd


def process_language_csv(file_path):
    try:
        df = pd.read_csv(file_path)

        if 'Language' in df.columns:
            df['Language'] = df['Language'].str.lower().str.strip()

            output_path = r"C:\Users\User\Desktop\CatologyProject\nlp\modified_languages.csv"
            df.to_csv(output_path, index=False)
            print(f"File has been successfully saved to {output_path}")
        else:
            print("The 'Language' column does not exist in the CSV file.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
    except Exception as e:
        print(f"Error: {str(e)}")
