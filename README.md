# **MelodyMind: Hybrid Music Recommendation System** 🎧  

Welcome to the MelodyMind project repository! 

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![LightFM](https://img.shields.io/badge/Library-LightFM-orange?style=flat-square)](https://makingunconferenc.es/lightfm/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

This project implements a **Hybrid Music Recommendation System** combining **Content-Based Filtering** and **Collaborative Filtering** using the **LightFM** library. It provides personalized song recommendations by analyzing audio features and simulating user interactions (artist-track associations).


## ✨ Features

* **Hybrid Approach:** Combines Content-Based and Collaborative Filtering.
* **Content-Based Filtering:** Recommends songs based on audio features (danceability, tempo, energy, etc.) using cosine similarity.
* **Collaborative Filtering:** Utilizes the LightFM library to learn user (artist) and item (track) embeddings from interaction data.
* **Simulated User Interactions:** Demonstrates collaborative filtering using artist-track associations as implicit feedback.
* **Streamlit Web App:** Provides an interactive web interface to get recommendations.
* **Modular Design:** Separated data processing and deployment ('music_app.py').

## 💡 Concepts Explained

- **Content-Based Filtering:** Imagine recommending songs that *sound* similar to what you already like. This method analyzes the characteristics (features) of items (songs) and suggests others with similar characteristics.
- **Collaborative Filtering:** This method looks at the behavior of many users. If User A and User B like similar songs, and User A likes a song that User B hasn't heard, Collaborative Filtering might recommend that song to User B. It finds patterns in user-item interactions.
- **Hybrid System:** Combines both methods to recommend new, niche songs (Content-Based) while leveraging user patterns (Collaborative Filtering) for enhanced accuracy.

## 🚀 Getting Started
Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.9+
* Git

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/indranil143/MelodyMind-Hybrid-Music-Recommendation-System.git
    cd MelodyMind-Hybrid-Music-Recommendation-System
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # Windows: .\venv\Scripts\activate
    # macOS/Linux: source venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Data

Uses the Spotify Dataset 1921-2020, 160k+ Tracks (`data.csv`).
**Source:** [https://www.kaggle.com/datasets/fcpercival/160k-spotify-songs-sorted](https://www.kaggle.com/datasets/fcpercival/160k-spotify-songs-sorted)
Ensure `data.csv` or renamed as `music_data.csv` is accessible by the notebook.

### Running the Notebook

Execute the cells in `MelodyMind_Hybrid_Music_Recommendation_System.ipynb` using Kaggle or Google Colab. This trains the model and saves `music_recommender_components.pkl`.

### Running the Streamlit App

1.  Ensure `music_recommender_components.pkl` is in the root directory.
2.  Activate your virtual environment.
3.  Run the app:
    ```bash
    streamlit run music_app.py
    ```
    The app will open in your browser.

---

## 📚 Previous Project: Last.fm API-Based Recommender

This project builds upon my earlier work that focused purely on **real-time music recommendations** using the **Last.fm API**:

👉 [Live Demo](https://melodymind-ai-powered-music-recommender-system-uvbgwng5xjx2tg3.streamlit.app/)  
🔗 GitHub: [MelodyMind-Music-Recommendation-System](https://github.com/indranil143/MelodyMind-Music-Recommendation-System)

That version offered:
-  **Dynamic song suggestions** based on user input (song & artist)  
-  **Real-time music discovery** via Last.fm API  
-  **Streamlit web app** for an interactive user experience  


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute to this project by opening issues or submitting pull requests!


























