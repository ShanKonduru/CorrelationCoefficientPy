import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load wine quality dataset from CSV file
wine_df = pd.read_csv('winequality-white.csv', delimiter=';')

# Calculate correlation coefficients
correlation_matrix = wine_df.corr()

# Mask upper triangle of correlation matrix
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Plot correlation matrix as heatmap
sns.set(font_scale=1.2)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, mask=mask, square=True, cmap='bwr', annot=True, fmt=".2f", vmin=-1, vmax=1, linewidth=0.5)

plt.title('Correlation Coefficient Heatmap for Wine Quality Dataset (Lower Triangle)')
plt.show()
