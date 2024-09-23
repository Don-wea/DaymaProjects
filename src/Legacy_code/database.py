import pandas as pd

# General function for reading data
def read_data(file_path):
    return pd.read_excel(file_path)

# Function for writing data
def write_data(file_path, data_frame):
    data_frame.to_excel(file_path, index=False)
