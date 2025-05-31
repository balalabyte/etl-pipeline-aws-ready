# scripts/load.py

import os

def load_data(df, output_path="data/processed/cleaned_data.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data successfully loaded to {output_path}")

# Test load step (optional)
if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    raw_data = extract_data()
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data)
