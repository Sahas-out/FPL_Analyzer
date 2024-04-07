import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_excel('~/TeamJhense/player_expected_stats.xlsx')
# Make sure 'xG' and 'xfpl' columns exist in your DataFrame and are numeric
# Assuming 'xG' is the column for expected goals and 'xfpl' for expected FPL points

# Check for any missing values and handle them
# For simplicity, we'll drop rows with missing values in these columns
df.dropna(subset=['xG', 'xfpl'], inplace=True)
# Increase figure size for better visibility
plt.figure(figsize=(12, 8))

# Adjust marker size (s), edgecolor for clarity, and use a bit of transparency (alpha)
plt.scatter(df['xG'], df['xfpl'], alpha=0.6, edgecolor='w', s=50, linewidth=0.6)

# Setting the background style using seaborn
sns.set_style("whitegrid")

# Enhancing the grid to make it more visible, but not too distracting
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='gray')

# Optional: Zooming in on a specific region if your points are clustered in a known area
# plt.xlim([min_x_value, max_x_value])
# plt.ylim([min_y_value, max_y_value])

# Add titles and labels with a clear font size
plt.title('Cleaner Scatter Plot of xG vs. xfpl', fontsize=16)
plt.xlabel('Expected Goals (xG)', fontsize=14)
plt.ylabel('Expected FPL Points (xfpl)', fontsize=14)

# Adjusting the tick frequency and font size for clarity
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('scatter_plot_xg_vs_xfpl.png')
plt.show()

