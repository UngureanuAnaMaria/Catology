import pandas as pd


def find_abbreviation(abbreviation):
    file_path = r"C:\Users\User\Desktop\CatologyProject\nlp\modified_languages.csv"
    df = pd.read_csv(file_path)

    language = []
    for index, row in df.iterrows():
        if row.iloc[2] == abbreviation:
            language.append(row.iloc[0])
            language.append(row.iloc[1])
            return language
    return None
