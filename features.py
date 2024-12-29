import librosa
import numpy as np
import os
import csv

def extract_features(audio_file):
    try:
        # Check if the file exists
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Audio file {audio_file} not found.")
        
        # Load the audio file
        y, sr = librosa.load(audio_file)
        
        # Extract features
        mfccs = librosa.feature.mfcc(y=y, sr=sr)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        
        # Concatenate the features into a single vector
        features = np.concatenate([np.mean(mfccs, axis=1), 
                                   np.mean(chroma, axis=1),
                                   np.mean(spectral_contrast, axis=1),
                                   np.mean(tonnetz, axis=1)])
        
        return features
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except librosa.util.exceptions.ParameterError as e:
        print(f"Librosa parameter error: {e}")
    except Exception as e:
        print(f"Error extracting features from {audio_file}: {e}")
    return None

def save_features_to_csv(audio_folder, output_csv):
    # Open the CSV file for writing
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['File Number', 'MFCC1', 'MFCC2', 'MFCC3', 'MFCC4', 'MFCC5', 'MFCC6', 'MFCC7', 'MFCC8', 'MFCC9', 
                         'MFCC10', 'MFCC11', 'MFCC12', 'MFCC13', 'MFCC14', 'MFCC15', 'MFCC16', 'MFCC17', 'MFCC18', 'MFCC19', 'MFCC20',
                         'Chroma1', 'Chroma2', 'Chroma3', 'Chroma4', 'Chroma5', 'Chroma6', 'Chroma7', 'Chroma8', 'Chroma9',
                         'Chroma10', 'Chroma11', 'Chroma12', 'Spectral Contrast1', 'Spectral Contrast2', 'Spectral Contrast3',
                         'Spectral Contrast4', 'Spectral Contrast5', 'Spectral Contrast6', 'Spectral Contrast7',
                         'Tonnetz1', 'Tonnetz2', 'Tonnetz3', 'Tonnetz4', 'Tonnetz5', 'Tonnetz6'])
        
        # Iterate through all the audio files in the folder
        for audio_file in os.listdir(audio_folder):
            if audio_file.endswith('.wav'):  # Only process .wav files
                audio_path = os.path.join(audio_folder, audio_file)
                
                # Extract features from the audio file
                features = extract_features(audio_path)
                
                if features is not None:
                    # Get the file number from the filename (assuming filenames are like '1.wav', '2.wav', etc.)
                    file_number = os.path.splitext(audio_file)[0]
                    
                    # Write the features to the CSV file, along with the file number
                    writer.writerow([file_number] + features.tolist())
                    print(f"Features for {audio_file} saved.")
                else:
                    print(f"Failed to extract features for {audio_file}.")

# Example usage
audio_folder = 'songs'
output_csv = 'audio_features.csv'
save_features_to_csv(audio_folder, output_csv)