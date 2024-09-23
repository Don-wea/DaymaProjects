import pandas as pd

def load_sales():
    # Load sales data from an Excel file
    df = pd.read_excel("data/sales_data.xlsx")
    
    # Convert to list of dictionaries
    return df.to_dict(orient="records")
