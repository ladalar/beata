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

- `add_coordinates.py`: Combines `country_coordinates.csv` and `world_music_data.csv` to generate `tracks_with_coordinates.csv`.
- `all_data.csv`: Contains all data collected.
- `combine_data.py`: Combines all data collected into `all_data.csv`.
- `convert_songs.py`: Ensures that `.wav` files can be processed by `features.py`.
- `country_coordinates.csv`: Contains countries and regions with corresponding capital city coordinates.
- `download_songs.py`: Downloads songs present in `world_music_data.csv`.
- `features.py`: Extracts MFCCs, Chroma features, Spectral contrast measures, and Tonnetz features from downloaded audio files to `audio_features.csv`.
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

### 4. Collect Data

Once you've set up the environment, collect data:

```bash
python music_data.py
```

This creates `world_music.csv` containing: `track_id`, `track_name`, `artist_name`, `location`, `listeners`, `genre`.

### 5. Add Coordinates

Add coordinates to the tracks:

```bash
python add_coordinates.py
```

This creates `tracks_with_coordinates.csv`.

### 6. Download Songs

Download the songs:

```bash
python download_songs.py
```

This saves songs present in `world_music.csv` to a folder `downloaded_songs`.

### 7. Extract Features

Extract features from the songs:

```bash
python features.py
```

This extracts features from the songs in the `downloaded_songs` folder and saves them in `audio_features.csv`.

### 8. Combine Data

Combine all data:

```bash
python combine_data.py
```

This combines data from `audio_features.csv` and `tracks_with_coordinates.csv` and saves it in `all_data.csv`.

### 9. Training the Deep Learning Model

After gathering sufficient data, use the extracted features to train a deep learning model to predict the geographical coordinates (latitude and longitude). You can use the following steps:

- Load the CSV data.
- Preprocess the data (e.g., normalize the features).
- Train the model on the features and coordinates.
- Evaluate the model's performance.

### 10. AI Music Generation

Once the model is trained and you have predicted coordinates, you can use AI techniques to generate music based on those coordinates. This might involve:

- **Style Transfer**: Using pre-trained models to apply a musical style to the generated music.
- **Generative Models**: Using models like OpenAI's MuseNet or Google's Magenta to generate new music based on input features (e.g., predicted coordinates).

### 11. CSV Output

The scripts will generate a CSV file `all_data.csv` with the following columns:

- **Track Information**:
    - `track_id`: Unique identifier for each track.
    - `track_name`: Title of the track.
    - `artist_name`: Name of the artist who performed the track.
    - `location`: Location associated with the artist (potentially where they are from or based).
    - `listeners`: Number of listeners for the track on Last.fm (if available).
    - `genre`: Genre of the track (potentially obtained from Last.fm tags).
- **Geographical Information**:
    - `Country`: Country of the artist's origin (potentially inferred from location or artist information).
    - `Capital`: Capital city of the artist's country (if applicable).
    - `Latitude`: Latitude coordinate of the capital city (if available).
    - `Longitude`: Longitude coordinate of the capital city (if available).
- **Audio Features**:
    - `MFCC1 - MFCC20`: Mel-Frequency Cepstral Coefficients (MFCCs) represent the short-term power spectrum of a sound, commonly used in audio feature extraction and music information retrieval.
    - `Chroma1 - Chroma12`: Chroma features represent the strength of the 12 pitch classes (C, C#, D, ..., B) in the music.
    - `Spectral Contrast1 - Spectral Contrast7`: Spectral contrast measures the difference in energy between bands of frequencies.
    - `Tonnetz1 - Tonnetz6`: Tonnetz features represent the position of the sound in a psychoacoustically-inspired 6-dimensional space.

### Example Output

```csv
track_id,track_name,artist_name,location,listeners,genre,Country,Capital,Latitude,Longitude,MFCC1,MFCC2,MFCC3,MFCC4,MFCC5,MFCC6,MFCC7,MFCC8,MFCC9,MFCC10,MFCC11,MFCC12,MFCC13,MFCC14,MFCC15,MFCC16,MFCC17,MFCC18,MFCC19,MFCC20,Chroma1,Chroma2,Chroma3,Chroma4,Chroma5,Chroma6,Chroma7,Chroma8,Chroma9,Chroma10,Chroma11,Chroma12,Spectral Contrast1,Spectral Contrast2,Spectral Contrast3,Spectral Contrast4,Spectral Contrast5,Spectral Contrast6,Spectral Contrast7,Tonnetz1,Tonnetz2,Tonnetz3,Tonnetz4,Tonnetz5,Tonnetz6
1,Saoko,Rosalía,Spain,1357002,Traditional,Spain,Madrid,40.42,-3.75,-77.41459656,52.02815246582031,-3.623052359,26.31342887878418,-6.456990242,4.815507411956787,-0.890465736,1.266771436,-4.186604977,8.584629059,-4.188908577,-1.132911921,-4.31681633,-3.103135586,-6.049440384,-2.329935551,-9.885704994,0.4364224076271057,-5.408226967,-3.179271221,0.423987865,0.4096793234348297,0.3129310607910156,0.3942963778972626,0.3675473928451538,0.2445663064718246,0.2352212965488433,0.3119161128997803,0.5756404995918274,0.451972634,0.3388523757457733,0.3229532837867737,18.671025343659387,16.510451585655943,19.57577634269491,20.28098252185062,20.19127154826591,19.324665797656024,48.27960009715634,-0.027142259,-0.020731049,-0.021391769,0.044810451,-0.007973986,-0.004324663
```

### Notes

- **API Rate Limiting**: The script sleeps for 0.5 seconds between requests to avoid hitting the Last.fm API too quickly.
- **Max Tracks per Country**: The script is configured to include a maximum of 50 tracks per country.
- **Missing Data**: If the location is not available from Last.fm, the script will attempt to derive the location from the associated tag.