# scripts/extract.py

import os
import pandas as pd

def extract_data(raw_folder_path="data/raw"):
    dataframes = []
    for file in os.listdir(raw_folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(raw_folder_path, file)
            df = pd.read_csv(file_path)
            print(f"Extracted: {file} with shape {df.shape}")
            dataframes.append(df)
    return dataframes

# Test extract step (optional)
if __name__ == "__main__":
    dfs = extract_data()
    print(f"Total files extracted: {len(dfs)}")
