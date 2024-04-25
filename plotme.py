import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
test_cases_executed = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
execution_time = np.array([10, 12, 9, 11, 13, 10, 8, 14, 12, 15])
complexity = np.array([2, 3, 1, 2, 3, 2, 1, 3, 2, 3])  # Assigning numerical values to complexity: L=1, M=2, H=3

# Calculate correlation coefficients
correlation_matrix = np.corrcoef([test_cases_executed, execution_time, complexity])

# Plot correlation matrix as heatmap
sns.set(font_scale=1.2)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', xticklabels=['Test Cases Executed', 'Execution Time', 'Complexity'], yticklabels=['Test Cases Executed', 'Execution Time', 'Complexity'])
plt.title('Correlation Coefficient Heatmap')
plt.show()
