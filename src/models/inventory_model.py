import pandas as pd

def load_inventory():
    # Load inventory data from an Excel file
    df = pd.read_excel("data/inventory_data.xlsx")
    
    # Convert to list of dictionaries
    return df.to_dict(orient="records")
