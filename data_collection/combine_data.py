import pandas as pd
import os

# Define the path to the data folder
data_folder = os.path.join(os.path.dirname(__file__), 'data')

# Load the CSV files from the data folder
tracks_df = pd.read_csv(os.path.join(data_folder, 'tracks_with_coordinates.csv'))
audio_features_df = pd.read_csv(os.path.join(data_folder, 'audio_features.csv'))

# Ensure the columns are of the same type for merging
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
audio_features_df['File Number'] = audio_features_df['File Number'].astype(int)

# Merge the DataFrames on 'track_id' and 'File Number'
combined_df = pd.merge(tracks_df, audio_features_df, left_on='track_id', right_on='File Number', how='inner')

# Drop the redundant 'File Number' column
combined_df = combined_df.drop(columns=['File Number'])

# Save the combined DataFrame to a new CSV file in the data folder
combined_csv_path = os.path.join(data_folder, 'all_data.csv')
combined_df.to_csv(combined_csv_path, index=False)

print(f"Combined data saved to {combined_csv_path}")