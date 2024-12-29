import pandas as pd

# Load the CSV files
tracks_df = pd.read_csv('tracks_with_coordinates.csv')
audio_features_df = pd.read_csv('audio_features.csv')

# Ensure the columns are of the same type for merging
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
audio_features_df['File Number'] = audio_features_df['File Number'].astype(int)

# Merge the DataFrames on 'track_id' and 'File Number'
combined_df = pd.merge(tracks_df, audio_features_df, left_on='track_id', right_on='File Number', how='inner')

# Drop the redundant 'File Number' column
combined_df = combined_df.drop(columns=['File Number'])

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('all_data.csv', index=False)

print("Combined data saved to all_data.csv")