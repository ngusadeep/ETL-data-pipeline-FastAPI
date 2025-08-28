import pandas as pd
import uuid

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    # Standardize column names to lowercase snake_case
    data.columns = [col.lower().replace(" ", "_") for col in data.columns]

    # Remove duplicated columns from merges (keep only "_x" versions)
    for col in data.columns:
        if col.endswith('_y'):
            data.drop(columns=[col], inplace=True)
    data.columns = [col.replace('_x', '') for col in data.columns]

    # Generate unique sale_id if not exists
    if 'sale_id' not in data.columns:
        data['sale_id'] = [str(uuid.uuid4()) for _ in range(len(data))]

    # Validate numeric columns exist
    required_cols = ['sales_amount', 'unit_price', 'unit_cost']
    for col in required_cols:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")

    # Round numeric values
    data['sales_amount'] = data['sales_amount'].round(0)
    data['unit_price'] = data['unit_price'].round(0)
    data['unit_cost'] = data['unit_cost'].round(0)

    # Categorize sales amount
    data['sales_category'] = pd.cut(
        data['sales_amount'],
        bins=[0, 100, 200, float('inf')],
        labels=['Low', 'Medium', 'High']
    )

    return data
