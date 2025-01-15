import pandas as pd


def display_values_and_frequencies(file_path, output_file_path):
    data = pd.read_excel(file_path)

    with open(output_file_path, 'w') as output_file:

        unique_breeds = data["Breed"].unique()

        for column in data.columns:

            if column == "Breed":
                continue

            distinct_values = data[column].unique()
            value_counts = data[column].value_counts()

            output_file.write(f"Attribute: {column}\n")
            output_file.write(f"Total distinct values: {len(distinct_values)}\n")
            output_file.write(f"Overall counts and frequencies:\n")
            for value, count in value_counts.items():
                output_file.write(f"  Value: {value}, Count: {count}\n")

            output_file.write(f"\nCounts and frequencies by breed:\n")

            for breed in unique_breeds:
                breed_data = data[data["Breed"] == breed]
                breed_value_counts = breed_data[column].value_counts()
                output_file.write(f"  Breed: {breed}\n")
                for value, count in breed_value_counts.items():
                    output_file.write(f"    Value: {value}, Count: {count}\n")

            output_file.write("\n" + "=" * 100 + "\n")

    print(f"\nResults have been saved to {output_file_path}")
