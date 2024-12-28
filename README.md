# Music Location Prediction and AI-Generated Music

This project focuses on predicting geographical locations for music based on extracted audio features. The aim is to build a deep learning model that predicts the geographical coordinates (latitude and longitude) of a track based on its audio features. Subsequently, AI will be used to generate music that aligns with specific coordinates, creating a unique and contextually relevant music experience.

## Features

- **Audio Feature Extraction**: Extracts various audio features from music tracks, including Mel-Frequency Cepstral Coefficients (MFCCs), Chroma, Spectral Contrast, and Tonnetz.
- **Location Prediction**: Uses the audio features to predict the geographical coordinates (latitude and longitude) for a given track.
- **AI Music Generation**: Leverages AI models to generate music tailored to specific geographical coordinates.
- **Data Collection**: Gathers metadata from Last.fm and MusicBrainz, including artist location and genre information.
- **Country-Specific Filtering**: Limits the number of tracks per country to ensure diversity in the dataset.

## Project Workflow

1. **Audio Feature Extraction**: Extract audio features (MFCCs, Chroma, Spectral Contrast, and Tonnetz) from a set of music tracks.
2. **Metadata Collection**: Fetch metadata from Last.fm and MusicBrainz, including artist name, location, and genre.
3. **Location Prediction**: Train a deep learning model using the extracted audio features to predict the geographical coordinates (latitude and longitude).
4. **Music Generation**: Use AI models (e.g., generative models or style transfer) to generate new music based on the predicted coordinates.
5. **Output**: The output is a generated track that corresponds to specific geographical coordinates.

## Project Structure

- `genre_mapping.json`: Contains a mapping of music genres to tags.
- `tag_to_country.json`: Maps Last.fm tags to countries.
- `music_data.py`: Main script to fetch and process music metadata.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `README.md`: This file.

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

The project requires Python and a few dependencies. To install them, run:

```bash
pip install -r requirements.txt
```

### 3. API Keys

You need a Last.fm API key to fetch data. To obtain your key, follow these steps:

- Go to Last.fm API and sign up.
- Create an application to generate your API key.
- Once you have the API key, create a `.env` file in the project directory with the following content:

```bash
LASTFM_API_KEY=your_lastfm_api_key_here
```

### 4. Data Preparation

You need to prepare your audio files for feature extraction. Convert them to the required format (e.g., WAV format with a consistent sample rate) before running the feature extraction process.

### 5. Running the Script

Once you've set up the environment and the required files, run the script to start extracting features and collecting metadata:

```bash
python fetch_music_metadata.py
```

This will:

- Extract audio features (MFCCs, Chroma, Spectral Contrast, Tonnetz) from your audio files.
- Fetch metadata for tracks from Last.fm and MusicBrainz, including artist name, location, and listeners.
- Filter the tracks based on location and genre.
- Save the extracted data to a CSV file for later use in training the deep learning model.

### 6. Training the Deep Learning Model

After gathering sufficient data, use the extracted features to train a deep learning model to predict the geographical coordinates (latitude and longitude). You can use the following steps:

- Load the CSV data.
- Preprocess the data (e.g., normalize the features).
- Train the model on the features and coordinates.
- Evaluate the model's performance.

### 7. AI Music Generation

Once the model is trained and you have predicted coordinates, you can use AI techniques to generate music based on those coordinates. This might involve:

- **Style Transfer**: Using pre-trained models to apply a musical style to the generated music.
- **Generative Models**: Using models like OpenAI's MuseNet or Google's Magenta to generate new music based on input features (e.g., predicted coordinates).

### 8. CSV Output

The script will generate a CSV file `music_metadata.csv` with the following columns:

- `track_id`: The unique ID of the track.
- `track_name`: The name of the track.
- `artist_name`: The name of the artist.
- `location`: The location of the artist (from MusicBrainz or country mapping).
- `listeners`: The number of listeners for the artist.
- `genre`: The genre based on the tag mapping.
- `mfcc`: The extracted MFCC features.
- `chroma`: The extracted Chroma features.
- `spectral_contrast`: The extracted Spectral Contrast features.
- `tonnetz`: The extracted Tonnetz features.
- `predicted_latitude`: The predicted latitude coordinate.
- `predicted_longitude`: The predicted longitude coordinate.

### Example Output

```csv
track_id,track_name,artist_name,location,listeners,genre,mfcc,chroma,spectral_contrast,tonnetz,predicted_latitude,predicted_longitude
123456,Song Title,Artist Name,United States,120000,Rock,-87.775566,0.28905708,16.46927748,0.01035144,37.7749,-122.4194
789101,Another Song,Artist 2,Canada,80000,Pop,110.30225,0.27479342,16.20537921,0.03168212,45.4215,-75.6992
...
```

### Notes

- **API Rate Limiting**: The script sleeps for 0.5 seconds between requests to avoid hitting the Last.fm API too quickly.
- **Max Tracks per Country**: The script is configured to include a maximum of 50 tracks per country.
- **Missing Data**: If the location is not available from Last.fm, the script will attempt to derive the location from the associated tag.