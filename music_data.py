import requests
import pandas as pd
import time
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('LASTFM_API_KEY')
BASE_URL = 'http://ws.audioscrobbler.com/2.0/'

# Load the genre mapping JSON
with open('genre_mapping.json') as f:
    genre_mapping = json.load(f)['genre_mapping']

# Load the JSON file for tags and countries
with open('tag_to_country.json') as f:
    tag_to_country = json.load(f)

# Get tags with countries and tags without countries
tags_with_country = tag_to_country.get('with_country', {})
tags_without_country = tag_to_country.get('without_country', [])
tags_country = tag_to_country.get('countries', {})

# Combine both lists of tags
tags = list(tags_with_country.keys()) + tags_without_country + list(tags_country.keys())

all_metadata = []
country_count = {}
max_per_country = 50

def fetch_artist_location_from_musicbrainz(mbid, retries=3, delay=3):
    """Fetch location from MusicBrainz using the artist's MBID."""
    url = f"https://musicbrainz.org/ws/2/artist/{mbid}?fmt=json"
    
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            data = response.json()
            if data and isinstance(data, dict):
                area = data.get('area')
                if area and isinstance(area, dict):
                    location = area.get('name')
                    if location:
                        return location
                    else:
                        print(f"Warning: No location found for MBID {mbid}.")
            else:
                print(f"Warning: Invalid or empty data for MBID {mbid}.")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise
    return None

def fetch_artist_info(artist_name, mbid=None):
    """Fetch artist info from Last.fm and fallback to MusicBrainz if needed."""
    params = {
        'method': 'artist.getInfo',
        'artist': artist_name,
        'api_key': API_KEY,
        'format': 'json'
    }
    url = "http://ws.audioscrobbler.com/2.0/"
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data and 'artist' in data:
            artist_info = data['artist']
            if 'mbid' in artist_info and not mbid:
                mbid = artist_info['mbid']
            if mbid:
                location = fetch_artist_location_from_musicbrainz(mbid)
                return location, artist_info
            else:
                print(f"Warning: No MBID found for artist {artist_name}.")
        else:
            print(f"Warning: Invalid or empty data for artist {artist_name}.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch artist info from Last.fm: {e}")
    except ValueError as e:
        print(f"JSON decoding failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None, None

def fetch_top_tracks_by_tag(tag, limit=20):
    """Fetch top tracks by tag from Last.fm."""
    params = {
        'method': 'tag.getTopTracks',
        'tag': tag,
        'api_key': API_KEY,
        'format': 'json',
        'limit': limit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get('tracks', {}).get('track', [])
    else:
        print(f"Error fetching tracks for tag {tag}: {response.status_code}")
    return []

def should_add_track(location):
    """Determine if a track's location should be included based on max per country."""
    if location:
        country = location.split(',')[-1].strip() if ',' in location else location.strip()
        country_count[country] = country_count.get(country, 0)
        if country_count[country] < max_per_country:
            country_count[country] += 1
            return True
    return False

def get_country_from_tag(tag):
    """Return a country associated with a tag, if available."""
    return tags_country.get(tag) or tags_with_country.get(tag)

def categorize_genre(tag):
    """Categorize genre based on the tag."""
    tag_lower = tag.lower()
    
    for genre, tags in genre_mapping.items():
        if tag_lower in tags:
            return genre
    return 'Other'

# Initialize track ID counter
track_id_counter = 1

# Fetch tracks based on tags and filter by location
for tag in tags:
    tracks = fetch_top_tracks_by_tag(tag)
    for track in tracks:
        artist_name = track.get('artist', {}).get('name')
        mbid = track.get('artist', {}).get('mbid')  # Artist MBID if available
        
        # Fetch location and artist info (e.g., listeners)
        location, artist_info = fetch_artist_info(artist_name, mbid)
        
        # If no location, try mapping tag to country if the tag has an associated country
        if not location:
            location = get_country_from_tag(tag)
        
        # Get number of listeners
        listeners = artist_info.get('stats', {}).get('listeners', 0) if artist_info else 0
        
        # Categorize genre based on the tag
        genre = categorize_genre(tag)
        
        # Get the track URL to generate track ID
        track_url = track.get('url')
        track_id = track.get('url').split('/')[-1] if track_url else None
        
        # Add incremental track ID
        track_data = {
            'track_id_number': track_id_counter,  # Add the incremental ID
            'track_id': track_id,
            'track_name': track.get('name'),
            'artist_name': artist_name,
            'location': location,
            'listeners': listeners,
            'genre': genre
        }
        
        # Check if the track should be included
        if should_add_track(location):
            all_metadata.append(track_data)
            track_id_counter += 1  # Increment the track ID for the next track
        
        time.sleep(0.5)  # Avoid hitting the API too quickly

# Convert the metadata to a DataFrame
df = pd.DataFrame(all_metadata)

# Save to a CSV file
df.to_csv('world_music.csv', index=False)
print("Metadata saved to world_music.csv")
