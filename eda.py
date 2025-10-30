import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data.csv')

# Display first rows
print(df.head())

# Basic statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Visualization
plt.figure(figsize=(12, 8))
df.hist(bins=20, figsize=(12, 8))
plt.tight_layout()
plt.savefig('eda_histogram.png')
print("EDA visualization saved!")

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
print("Correlation heatmap saved!")
