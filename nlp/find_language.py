import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def find_language(abbreviation):
    current_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(current_dir, '..'))
    file_path = os.path.join(project_root, 'nlp', 'modified_languages.csv')
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():
        if row.iloc[2] == abbreviation:
            language = row.iloc[3].split(";")
            print(language[0])
            return language[0]
    return None
