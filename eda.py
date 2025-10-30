import pandas as pd

# Load dataset
df = pd.read_csv('data.csv')

# Display first rows
print(df.head())

# Basic statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
