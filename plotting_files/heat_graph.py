import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your football dataset into a DataFrame
df = pd.read_excel('~/TeamJhense/player_expected_stats.xlsx')

# Select relevant columns for correlation analysis
cols = ['total_points', 'form', 'performance_ratio', 'xfpl', 'xfpl&f', 'xG', 'xA', 'xGC', 'xBP', 'CS%', 'xS', 'xYC', 'xPS', 'xPM', 'xRC']

# Calculate correlation matrix
corr_matrix = df[cols].corr()

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Generate a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# Add title
plt.title('Correlation Matrix Heatmap of Performance Metrics')
plt.savefig('correlation_matrix_heatmap.png')
# Show plot
plt.show()
