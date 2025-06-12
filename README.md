# MelodyMind: Hybrid Music Recommendation System 🎧

Welcome to the MelodyMind project repository!  
This repository showcases my work in building **music recommendation systems**, evolving from a real-time API-based recommender to a sophisticated hybrid model.

---

## 🚀 Project 1: Last.fm API-Based Music Recommender (Live Demo)

**👉 [Live Demo](https://hybrid-music-recommendation-system.streamlit.app/)**

[![Powered by Last.fm](https://img.shields.io/badge/Powered%20by-Last.fm-E51B23?style=flat&logo=lastdotfm&logoColor=white)](https://www.last.fm/api/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

This application is your personal guide to discovering new music, powered by the extensive **Last.fm API**. It offers intelligent and diverse recommendations through an intuitive Streamlit interface.

### ✨ Project Overview

MelodyMind isn't just another music recommender; it's a **hybrid system** that intelligently blends various data points from Last.fm to unearth unique music tailored to your taste. Whether you provide an artist, a specific track, or both, MelodyMind digs deep to find your next favorite song. Its hybrid approach ensures you get a broad spectrum of suggestions, moving beyond simple direct similarities to explore connected artists and genres.

### 🌟 Key Features

* **Intelligent Input Handling**: Smartly processes your artist and track inputs, with built-in auto-correction for common typos, ensuring you always find what you're looking for.
* **Diverse Recommendation Strategies**:
    * **Track-Focused**: Discover songs similar to a given track, expanding your playlist effortlessly.
    * **Artist-Centric**: Explore the top hits from your favorite artists or discover new tracks from artists you'll love.
    * **Contextual Hybridization**: When direct matches are scarce, the system intelligently broadens its search to include top tracks from similar artists and songs associated with relevant genres, providing richer recommendations.
* **Comprehensive Insights**: Dive deeper into the music with detailed information about recommended artists and tracks, including their top tags and concise summaries.
* **Sleek User Interface**: Enjoy a smooth and responsive experience thanks to the interactive Streamlit web application.
* **Instant Access**: Direct links to Last.fm enable you to listen to recommended tracks immediately.

### 💻 Technology Stack

* **Python**: The robust foundation for all logic and data processing.
* **Streamlit**: For creating a beautiful, interactive, and easy-to-use web application.
* **Requests**: Handles all HTTP communications with the Last.fm API.
* **Last.fm API**: The rich data source powering the music recommendations.

### ⚙️ Getting Started (Last.fm API App)

To run this version of MelodyMind on your local machine, follow these simple steps!

#### Prerequisites

* Python 3.12 (highly recommended for best compatibility)
* [Git](https://git-scm.com/downloads)
* A [Last.fm API Key](https://www.last.fm/api/account/create) – essential for accessing music data.

#### Local Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/indranil143/Hybrid-Music-Recommendation-System.git](https://github.com/indranil143/Hybrid-Music-Recommendation-System.git)
    cd Hybrid-Music-Recommendation-System
    ```
2.  **Create a Virtual Environment (Highly Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install Dependencies:**
    Ensure your `requirements.txt` file is present in the current directory.
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set Your Last.fm API Key:**
    The application needs your Last.fm API Key to function. Set it as an environment variable:
    * **For Windows (Command Prompt):**
        ```cmd
        set LASTFM_API_KEY="YOUR_ACTUAL_LASTFM_API_KEY"
        ```
    * **For Windows (PowerShell):**
        ```powershell
        $env:LASTFM_API_KEY="YOUR_ACTUAL_LASTFM_API_KEY"
        ```
    * **For macOS/Linux (Bash/Zsh):**
        ```bash
        export LASTFM_API_KEY="YOUR_ACTUAL_LASTFM_API_KEY"
        ```
    * **Remember to replace `YOUR_ACTUAL_LASTFM_API_KEY`** with the key you obtained from Last.fm. For persistent local development, consider using a `.env` file with the `python-dotenv` package.
5.  **Run the Streamlit App:**
    ```bash
    streamlit run music_app_api_only.py
    ```
    Your web browser should automatically open the MelodyMind application.

### ☁️ Deployment to Streamlit Community Cloud

Deploying MelodyMind to [Streamlit Community Cloud](https://share.streamlit.io/) is straightforward:

1.  **GitHub Repository**: Your project must be hosted on a public GitHub repository.
2.  **`requirements.txt`**: Ensure this file is located in the same directory as `music_app_api_only.py`. It should accurately list all project dependencies and avoid platform-specific packages (like `pywin32`) or problematic `+cpu` PyTorch/Torchaudio versions, as these can cause deployment issues.
3.  **API Key as Secret**: Securely store your `LASTFM_API_KEY` in the Streamlit Community Cloud dashboard's secrets. Go to your app settings, then "Advanced settings," and finally "Secrets," adding the following:
    ```toml
    LASTFM_API_KEY="YOUR_ACTUAL_LASTFM_API_KEY_HERE"
    ```

### 🎮 How to Use

* Simply enter an artist name, a track name, or both in the **sidebar** on the left.
* Adjust the "Number of Recommendations" slider to control the quantity of suggestions.
* Then click "Get Recommendations."
* Explore the results under the "🎵 Recommendations" tab, and dive into deeper context with the "📊 Insights" tab.

---

## 🎶 Project 2: Hybrid Music Recommendation System (LightFM)

This project implements a **Hybrid Music Recommendation System** combining **Content-Based Filtering** and **Collaborative Filtering** using the **LightFM** library. It provides personalized song recommendations by analyzing audio features and simulating user interactions (artist-track associations).

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![LightFM](https://img.shields.io/badge/Library-LightFM-orange?style=flat-square)](https://makingunconferenc.es/lightfm/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

### ✨ Features

* **Hybrid Approach:** Combines Content-Based and Collaborative Filtering.
* **Content-Based Filtering:** Recommends songs based on audio features (danceability, tempo, energy, etc.) using cosine similarity.
* **Collaborative Filtering:** Utilizes the LightFM library to learn user (artist) and item (track) embeddings from interaction data.
* **Simulated User Interactions:** Demonstrates collaborative filtering using artist-track associations as implicit feedback.
* **Streamlit Web App:** Provides an interactive web interface to get recommendations.
* **Modular Design:** Separated data processing and deployment (`music_app.py`).

### 💡 Concepts Explained

* **Content-Based Filtering:** Imagine recommending songs that *sound* similar to what you already like. This method analyzes the characteristics (features) of items (songs) and suggests others with similar characteristics.
* **Collaborative Filtering:** This method looks at the behavior of many users. If User A and User B like similar songs, and User A likes a song that User B hasn't heard, Collaborative Filtering might recommend that song to User B. It finds patterns in user-item interactions.
* **Hybrid System:** Combines both methods to recommend new, niche songs (Content-Based) while leveraging user patterns (Collaborative Filtering) for enhanced accuracy.

### Dataset

Uses the Spotify Dataset 1921-2020, 160k+ Tracks.
**Source:** [https://www.kaggle.com/datasets/fcpercival/160k-spotify-songs-sorted](https://www.kaggle.com/datasets/fcpercival/160k-spotify-songs-sorted)

### ⚙️ Getting Started (LightFM Hybrid App)

#### Running the Notebook

Execute the cells in `Hybrid_Music_Recommendation_System.ipynb` using Kaggle or Google Colab. This trains the model and saves `music_recommender_components.pkl`.

#### Running the Streamlit App

1.  Ensure `music_recommender_components.pkl` is in the root directory.
2.  Activate your virtual environment (from the previous setup steps, or create a new one).
3.  Run the app:
    ```bash
    streamlit run music_app.py
    ```
    The app will open in your browser.

---

## 🤝 Contributing

Feel free to contribute to this project by opening issues or submitting pull requests!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
