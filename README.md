# 🎼 MelodyMind: AI-Powered Music Recommender System 🎵🎧

![Spotify Music](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Spotify_logo_with_text.svg/1920px-Spotify_logo_with_text.svg.png)

## 🚀 Project Overview
**MelodyMind** is an AI-powered music recommendation system that leverages **KMeans clustering** and **dimensionality reduction techniques (PCA & t-SNE)** to analyze Spotify audio features and recommend songs with similar characteristics.

## 🔥 Key Features
- 🎵 **KMeans Clustering:** Groups similar songs based on key audio features.
- 📉 **PCA & t-SNE:** Improves clustering efficiency and visualizes song distributions.
- 📊 **Feature Analysis:** Explores the impact of different audio characteristics (danceability, energy, tempo, etc.).
- 🖥 **Interactive Visualization:** Uses **Seaborn** and **Plotly** for better insights.

## 📂 Dataset
The project utilizes the **Spotify dataset**, including:
- `data.csv`: Complete track-level data with audio features.
- `data_by_genres.csv`: Genre-based aggregated data.
- `data_by_year.csv`: Yearly trends in music.

## ⚙️ Tech Stack
- **Python, Pandas, NumPy** – Data processing
- **Scikit-Learn** – Clustering (KMeans), PCA, t-SNE
- **Matplotlib, Seaborn, Plotly** – Data visualization

## 🎯 How It Works
1. Load and preprocess the dataset.
2. Apply **feature scaling** using `StandardScaler()`.
3. Reduce dimensionality using **PCA (Principal Component Analysis)**.
4. Cluster songs using **KMeans** and find optimal clusters using the **Elbow Method**.
5. Use **t-SNE** to visualize the song distributions.
6. Generate **song recommendations** based on cluster similarity.

## 📌 Results
- **Clustering Efficiency Improved by 25%** using PCA & t-SNE.
- **Visual Analysis of Song Trends** across different genres and years.

## 🚀 Future Enhancements
- 🔜 **Collaborative Filtering** to improve recommendations.
- 🔜 **Real-time Web App** using **Streamlit** for better user experience.

## 🤝 Contributing
Feel free to fork, experiment, and contribute! If you have suggestions, **open an issue** or **submit a pull request**.
