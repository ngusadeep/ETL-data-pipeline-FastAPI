import pandas as pd
from pathlib import Path
from typing import Union

def extract_data(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Extracts data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str | Path): Path to the CSV file.

    Returns:
        pd.DataFrame: The extracted data.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    file = Path(file_path)

    if not file.exists():
        raise FileNotFoundError(f"CSV file not found at {file.resolve()}")

    data = pd.read_csv(file)
    print(f"Extracted {len(data)} rows from {file.resolve()}")
    return data
