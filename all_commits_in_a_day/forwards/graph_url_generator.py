import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Wedge
import requests

# Load and prepare your DataFrame here if not already done
# Example DataFrame loading (replace with your actual data loading)
df = pd.read_excel('~/TeamJhense/forwards/Top-Forwds.xlsx')
# df['prc'] = df['prc'].str[1:-1].astype('float64')
# df['T'] = df['T'].str.replace(',','').astype('int64')

# Assuming 'name' is the column with player names
# Selecting stats columns, replace these with your actual stat columns
stats_columns = df.columns.drop(['name', 'position', 'team', 'role','VS','xS','chance_playing','xPS','xPM','xYC','xRC'])

# Ensure stats columns are numeric
df[stats_columns] = df[stats_columns].apply(pd.to_numeric, errors='coerce')

# Calculate max values for normalization
max_values = df[stats_columns].max()

# Define colors for the slices
colors = plt.cm.viridis(np.linspace(0, 1, len(stats_columns)))

# Create a DataFrame to store image URLs
image_urls = []

# Iterate over each player in the DataFrame
for index, row in df.iterrows():
    player_name = row['name']
    player_stats = row[stats_columns]
    radii = player_stats / max_values

    # Plot setup
    fig, ax = plt.subplots()
    ax.set_aspect('equal')  # Keep the aspect ratio square
    start_angle = 90  # Starting from the top

    num_stats = len(player_stats)
    angle_per_slice = 360 / num_stats

    for i, (stat, radius) in enumerate(zip(stats_columns, radii)):
        # Calculate start and end angles
        theta1 = start_angle + i * angle_per_slice
        theta2 = start_angle + (i + 1) * angle_per_slice
        
        # Create a wedge
        wedge = Wedge(center=(0, 0), r=radius, theta1=theta1, theta2=theta2,
                      facecolor=colors[i], edgecolor='w')
        ax.add_patch(wedge)

        # Add text label for the stat
        middle_angle_rad = np.radians((theta1 + theta2) / 2)
        distance = radius * 0.5  # Position the text at half the radius
        value_str = f'{row[stat]:.1f}'  # Format the value to one decimal place
        ax.text(distance * np.cos(middle_angle_rad), distance * np.sin(middle_angle_rad), f'{stat}\n{value_str}',
                horizontalalignment='center', verticalalignment='center', fontsize=8)

    # Set limits and hide axes
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    # Save the plot as an image
    image_path = f'{player_name}_pizza_chart.png'
    plt.savefig(image_path, bbox_inches='tight')
    plt.close()

    # Upload the image to imgbb.com using their API
    upload_url = 'https://api.imgbb.com/1/upload'
    with open(image_path, 'rb') as file:
        response = requests.post(upload_url, files={'image': file}, data={'key': '4f95451102a87b6d92664aa43aaef94e'})
        if response.status_code == 200:
            image_url = response.json()['data']['url']
            image_urls.append({'name': player_name, 'url': image_url})

# Convert the list of dictionaries to a DataFrame
image_urls_df = pd.DataFrame(image_urls)

# Save the DataFrame to a CSV file
image_urls_df.to_csv('player_urls.csv', index=False)
