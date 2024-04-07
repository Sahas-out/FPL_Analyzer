import requests
import pandas as pd

api_key = '4f95451102a87b6d92664aa43aaef94e'
image_path = 'box_plot.png'

# Prepare the data for the POST request
with open(image_path, 'rb') as image:
    files = {
        'image': (image_path, image),
    }
    data = {
        'key': api_key,
    }

    # Make the request to upload the image
    response = requests.post('https://api.imgbb.com/1/upload', data=data, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the image URL
        image_url = response.json()['data']['url']
        
        # Save the URL to a CSV file
        df = pd.DataFrame({'Image URL': [image_url]})
        df.to_csv('final_graphs.csv', index=False)
    else:
        print("Failed...")
