import pandas as pd

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Apply transformations to clean and enrich sales data.

    - Validates required numeric columns.
    - Rounds numeric values.
    - Categorizes sales into Low, Medium, High.
    """
    # Required numeric columns
    required_cols = ['Sales_Amount', 'Unit_Price', 'Unit_Cost']
    missing_cols = [col for col in required_cols if col not in data.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Round numeric values
    data[required_cols] = data[required_cols].round(0)

    # Categorize sales
    data['Sales_Category'] = pd.cut(
        data['Sales_Amount'],
        bins=[0, 100, 200, float('inf')],
        labels=['Low', 'Medium', 'High']
    )

    return data
