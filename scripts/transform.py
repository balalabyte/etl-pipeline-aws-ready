# scripts/transform.py

import pandas as pd

def transform_data(dataframes):
    cleaned_dfs = []

    for df in dataframes:
        # Basic cleaning: drop rows with null values
        df = df.dropna()
        cleaned_dfs.append(df)

    combined_df = pd.concat(cleaned_dfs, ignore_index=True)
    print(f"Transformed data shape: {combined_df.shape}")
    return combined_df

# Test transform step (optional)
if __name__ == "__main__":
    from extract import extract_data
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    print(transformed_data.head())
