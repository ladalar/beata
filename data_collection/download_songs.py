import pandas as pd
import os
from yt_dlp import YoutubeDL

# Define the path to the data folder
data_folder = os.path.join(os.path.dirname(__file__), 'data')

# Load the CSV file from the data folder
csv_file = os.path.join(data_folder, 'world_music.csv')
df = pd.read_csv(csv_file)

# Create a directory to store downloaded songs
output_dir = 'downloaded_songs'
os.makedirs(output_dir, exist_ok=True)

# Function to search and download a song in WAV format
def download_song(track_id, track_name, artist_name):
    search_query = f"{track_name} {artist_name}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, f'{track_id}.wav'),
        'quiet': False,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',  # Save in WAV format
                'preferredquality': '192',  # Best quality for source
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Searching and downloading: {search_query}")
            ydl.download([f"ytsearch1:{search_query}"])  # Search and download the first result
            print(f"Downloaded {track_name} by {artist_name} as {track_id}.wav")
        except Exception as e:
            print(f"Failed to download {track_name} by {artist_name}: {e}")

# Iterate through the CSV and download each song
for _, row in df.iterrows():
    track_id = row['track_id']
    track_name = row['track_name']
    artist_name = row['artist_name']
    download_song(track_id, track_name, artist_name)