import os
import pandas as pd

# Define the paths to the data and data_references folders
data_folder = os.path.join(os.path.dirname(__file__), 'data')
data_references_folder = os.path.join(os.path.dirname(__file__), 'data_references')

# Load the CSV files
tracks_df = pd.read_csv(os.path.join(data_folder, 'world_music.csv'))
coords_df = pd.read_csv(os.path.join(data_references_folder, 'country_coordinates.csv'))

# Ensure both dataframes have a clean 'Country' column
coords_df['Country'] = coords_df['Country'].str.strip()  # Remove extra spaces

# Merge the DataFrames on the location and Country columns
merged_df = pd.merge(tracks_df, coords_df, left_on='location', right_on='Country', how='left')

# Fill missing coordinates with a default value (e.g., 0.0 for both latitude and longitude)
merged_df['Latitude'] = merged_df['Latitude'].fillna(0.0)
merged_df['Longitude'] = merged_df['Longitude'].fillna(0.0)

# Display the resulting DataFrame to ensure everything is correct
print(merged_df.head())

# Save the merged DataFrame to a new CSV file in the data folder
output_csv_path = os.path.join(data_folder, 'tracks_with_coordinates.csv')
merged_df.to_csv(output_csv_path, index=False)

print(f"Metadata with coordinates saved to {output_csv_path}")