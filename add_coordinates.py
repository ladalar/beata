import pandas as pd

# Load the track metadata CSV file
tracks_df = pd.read_csv('world_music_data.csv')

# Load the country coordinates CSV file
coords_df = pd.read_csv('country_coordinates.csv')

# Ensure both dataframes have a clean 'Country' column
coords_df['Country'] = coords_df['Country'].str.strip()  # Remove extra spaces

# Merge the track metadata with the country coordinates based on the 'location' column
# Assumes 'location' contains the country name, and 'Country' contains country names in the coordinates file
merged_df = pd.merge(tracks_df, coords_df, left_on='location', right_on='Country', how='left')

# Fill missing coordinates with a default value (e.g., 0.0 for both latitude and longitude)
merged_df['Latitude'] = merged_df['Latitude'].fillna(0.0)
merged_df['Longitude'] = merged_df['Longitude'].fillna(0.0)

# Display the resulting DataFrame to ensure everything is correct
print(merged_df.head())

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('tracks_with_coordinates.csv', index=False)

print("Metadata with coordinates saved to tracks_with_coordinates.csv")