import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load wine quality dataset from CSV file
wine_df = pd.read_csv('winequality-white.csv', delimiter=';')

# Calculate correlation coefficients
correlation_matrix = wine_df.corr()

# Plot correlation matrix as heatmap
sns.set(font_scale=1.2)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Coefficient Heatmap for Wine Quality Dataset')
plt.show()
