import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your football dataset into a DataFrame
df = pd.read_excel('~/TeamJhense/player_expected_stats.xlsx')
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='position', y='xfpl', palette='colorblind')

# Add title and labels
plt.title('Box Plot of Expected Points (xfpl) by Position', fontsize=16)
plt.xlabel('Position', fontsize=14)
plt.ylabel('Expected Points (xfpl)', fontsize=14)

# Show plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.savefig('box_plot.png')
plt.show()
