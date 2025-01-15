import pandas as pd


def delete_columns(file_path):
    """
    Delete specific columns from the dataset:
    'Row.names', 'Horodateur', 'Nombre', 'Logement', 'Zone',
    'Ext', 'Obs', 'Abondance', 'PredOiseau', 'PredMamm' and 'Plus'.

    Args:
        file_path (str): Path to the input Excel file.
    """

    dataset = pd.read_excel(file_path)

    columns_to_delete = [
        'Row.names', 'Horodateur', 'Nombre', 'Logement', 'Zone',
        'Ext', 'Obs', 'Abondance', 'PredOiseau', 'PredMamm', 'Plus'
    ]

    dataset = dataset.drop(columns=[col for col in columns_to_delete if col in dataset.columns])

    dataset.to_excel(file_path, index=False)

    print(f"Columns {', '.join(columns_to_delete)} deleted (if they existed) from the dataset")
