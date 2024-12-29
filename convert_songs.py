import os
import subprocess

def convert_audio_files(input_folder, output_folder):
    # Make sure the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through all files in the input folder
    for audio_file in os.listdir(input_folder):
        if audio_file.endswith('.wav'):  # Only process .wav files
            input_path = os.path.join(input_folder, audio_file)
            output_file = os.path.splitext(audio_file)[0] + '_converted.wav'  # New file name with '_converted'
            output_path = os.path.join(output_folder, output_file)
            
            # Build the ffmpeg command
            command = [
                'ffmpeg', 
                '-i', input_path,  # Input file
                '-acodec', 'pcm_s16le',  # Set audio codec
                '-ar', '44100',  # Set audio sample rate
                '-ac', '2',  # Set number of audio channels (2 for stereo)
                output_path  # Output file
            ]
            
            # Run the ffmpeg command
            try:
                subprocess.run(command, check=True)
                print(f"Converted {audio_file} to {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {audio_file}: {e}")

# Example usage
input_folder = 'downloaded_songs'  # Folder with your original .wav files
output_folder = 'converted_songs'  # Folder to save the converted .wav files
convert_audio_files(input_folder, output_folder)