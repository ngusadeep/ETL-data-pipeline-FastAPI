import pandas as pd

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """Apply transformations to clean and enrich data."""

    # Validate numeric columns exist
    required_cols = ['Sales_Amount', 'Unit_Price', 'Unit_Cost']
    for col in required_cols:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")

    # Round values
    data['Sales_Amount'] = data['Sales_Amount'].round(0)
    data['Unit_Price'] = data['Unit_Price'].round(0)
    data['Unit_Cost'] = data['Unit_Cost'].round(0)


    # Example: categorize by sales amount
    data['Sales_Category'] = pd.cut(
        data['Sales_Amount'],
        bins=[0, 100, 200, float('inf')],
        labels=['Low', 'Medium', 'High']
    )

    print("Transformations applied.")
    return data
