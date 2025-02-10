## **Overview**  
This project aims to predict the popularity category of a song—low, medium, or high listener counts—based on various extracted audio features. By leveraging machine learning techniques, the model classifies songs using key acoustic and metadata attributes.

## **Music Data Collection and Preprocessing - `music_data.ipynb`**

### **Overview**  
This Jupyter Notebook automates the process of collecting and preprocessing music-related data. It integrates multiple data sources and techniques to gather track metadata, download audio files, extract audio features, and enrich the dataset with geographical information.  

### **Workflow**  
The notebook follows these key steps:

1. **Data Collection** 📊  
   - Fetches metadata from **Last.fm**, **MusicBrainz**, and **OpenCage API** to gather track information, artist details, and geographic locations.  

2. **Audio Processing** 🎧  
   - Downloads audio tracks using `yt-dlp`.  
   - Extracts key audio features such as MFCCs, Chroma, Tonnetz, Spectral Contrast, RMS, and more using `librosa`.  
   - Detects the dominant language of the track using OpenAI's **Whisper** model.  

3. **Data Integration & Storage** 🔄  
   - Combines track metadata with the extracted audio features.  
   - Ensures missing geographic coordinates are retrieved and stored for future use.  
   - Saves the final dataset for further analysis or machine learning applications.

### **Expected Output** ✅  
- A CSV file (`all_data.csv`) containing enriched track metadata, audio features, and geographic information.  
- Processed and cleaned datasets ready for visualization, analysis, or machine learning applications.

## **Music Popularity Analysis - `music_popularity.ipynb`**

### **Overview**  
In this Jupyter Notebook, the dataset collected from `music_data.ipynb` is analyzed to predict the popularity of the tracks based on their audio features and metadata. The notebook uses various machine learning algorithms to classify the songs into different popularity categories.

### **Workflow**  
The analysis process follows these steps:
1. **Data Preprocessing**  
   - Data cleaning, feature engineering, and splitting the dataset into training and testing sets.
   
2. **Model Training**  
   - Training a hybrid neural network model with LSTM and Dense branches to predict the popularity category.

3. **Evaluation**  
   - Evaluating the model's performance using various metrics, including accuracy, confusion matrix, and classification report.

4. **Visualization**  
   - Visualizing the model's performance and feature importance to better understand the influence of different features on popularity prediction.

---

## **How to Open and Run the Notebooks**

To open and run the Jupyter Notebooks, follow these steps:

1. **Install Jupyter Notebook** (if not installed):
   - First, make sure you have Python installed. You can install Jupyter by running the following command in your terminal or command prompt:
   ```bash
   pip install notebook
   ```
2. **Navigate to Your Project Directory**

Open a terminal or command prompt and navigate to the directory where your project files are stored.

3. **Launch Jupyter Notebook:**

In the terminal, type:
```bash
jupyter notebook
```

This will open the Jupyter Notebook interface in your web browser.
4. ***Open the Notebooks:**

In the Jupyter interface, locate and click on the following files to open them:
`music_data.ipynb` for data collection and preprocessing.
`music_popularity`.ipynb for analyzing the dataset and training the model.
Run the Notebooks:

Once the notebook is open, you can run each cell sequentially by selecting each one and pressing Shift + Enter.

## Future Plans
# Music Location Prediction and AI-Generated Music
This project will focus on predicting geographical locations for music based on extracted audio features. The aim is to build a deep learning model that predicts the geographical coordinates (latitude and longitude) of a track based on its audio features.

Subsequently, AI will be used to generate music that aligns with specific geographical coordinates, creating a unique and contextually relevant music experience. This will open the door for more personalized and location-aware music generation, enhancing the way music is experienced across different regions.