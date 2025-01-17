import os
import pandas as pd
import json
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
dataset_path = os.path.join(project_root, 'Catology.xlsx')
dataset = pd.read_excel(dataset_path)

exclude_columns = ['Breed', 'Sex', 'Age']

most_common_values = {}

for column in dataset.columns:
    if column not in exclude_columns:
        most_common_value = dataset[column].mode()[0]
        most_common_values[column] = most_common_value

output_path = "most_common_values.json"
with open(output_path, 'w') as json_file:
    json.dump(most_common_values, json_file, indent=4)

print(f"Most common values saved to {output_path}")
