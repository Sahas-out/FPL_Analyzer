import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
df = pd.read_excel('~/TeamJhense/player_expected_stats.xlsx')
# Make sure 'xG' and 'xfpl' columns exist in your DataFrame and are numeric
# Assuming 'xG' is the column for expected goals and 'xfpl' for expected FPL points

# Check for any missing values and handle them
# For simplicity, we'll drop rows with missing values in these columns
df.dropna(subset=['xG', 'xfpl'], inplace=True)
plt.figure(figsize=(10, 6))

# Setting the background color
plt.gca().set_facecolor('#001824')
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='#444444')  # Adjust grid color for visibility

# Scatter plot
plt.scatter(df['xG'], df['xfpl'], s=50, c='#ff5252', alpha=0.75, edgecolors='none')

plt.title('Scatter Plot of xG vs. xfpl', color='white')
plt.xlabel('Expected Goals (xG)', color='white')
plt.ylabel('Expected FPL Points (xfpl)', color='white')

# Setting the color of the tick labels
plt.xticks(color='white')
plt.yticks(color='white')

# Adjust the step size on the axes to improve readability
plt.xlim(0, max(df['xG']) + 0.05)  # Adjust the limit to just beyond the max value for better fit
plt.ylim(0, max(df['xfpl']) + 0.05)

# Adjust the ticks to better accommodate your data range
tick_step_x = 0.05  # Adjust the step size as needed
tick_step_y = 0.05  # Adjust the step size as needed

plt.xticks(np.arange(0, max(df['xG']) + tick_step_x, tick_step_x))
plt.yticks(np.arange(0, max(df['xfpl']) + tick_step_y, tick_step_y))

plt.show()