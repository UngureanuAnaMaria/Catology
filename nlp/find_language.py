import pandas as pd


def find_language(abbreviation):
    file_path = r"C:\Users\User\Desktop\CatologyProject\nlp\modified_languages.csv"
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():
        if row.iloc[2] == abbreviation:
            language = row.iloc[3].split(";")
            print(language[0])
            return language[0]
    return None
