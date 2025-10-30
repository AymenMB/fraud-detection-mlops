import pandas as pd
import numpy as np

# Load dataset from main data source
df = pd.read_csv('main_data.csv')

# Display information
print("=== MAIN BRANCH VERSION ===")
print(f"Dataset shape: {df.shape}")
print(df.head())

# Statistics
print(df.describe())
