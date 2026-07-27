import pandas as pd
from pathlib import Path

# Path to the folder containing all CSV files
DATA_FOLDER = Path("data/raw")

# Get all CSV files from the folder
csv_files = list(DATA_FOLDER.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files.\n")

# Read each CSV file
for file in csv_files:
    print("=" * 60)
    print(f"File Name : {file.name}")

    df = pd.read_csv(file)

    print(f"Shape     : {df.shape}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("=" * 60)
    print()