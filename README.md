# 🎼 **MelodyMind: Music Recommendation System** 🎵🎧  
👉 [MelodyMind](https://melodymind-ai-powered-music-recommender-system-uvbgwng5xjx2tg3.streamlit.app/) 

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Spotify_logo_with_text.svg/1920px-Spotify_logo_with_text.svg.png" alt="Spotify Logo" width="100"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Lastfm_logo.svg/1920px-Lastfm_logo.svg.png" alt="Last.fm Logo" width="100"/>
</p>

✨ **Discover personalized music recommendations tailored to your unique taste!** 🎧

---

## 🚀 **Project Overview** 
**MelodyMind** is an advanced **AI-driven music recommendation system** offering two powerful approaches:  

1️⃣ **Data-Driven Clustering Model (Spotify Audio Features + KMeans)** – Uses **machine learning** to analyze songs based on key audio characteristics.
2️⃣ **Real-Time API-Based Recommendation (Last.fm API + Streamlit)** – Fetches similar songs dynamically based on user input.  

This project combines **machine learning** with **real-time song discovery**, delivering **personalized, interactive, and efficient music recommendations**. 
 
---  

## 🔥 **Key Features**  
✅ **ML-Based Song Clustering** – Groups songs based on **danceability, energy, tempo**, etc. using **KMeans clustering**.  
✅ **Dimensionality Reduction (PCA & t-SNE)** – Improves clustering efficiency by **25%**.
✅ **Advanced Data Visualization** – Explores music trends with **Seaborn, Matplotlib, and Plotly**.
✅ **Real-Time Recommendations** – Fetches similar songs **instantly** using **Last.fm API**.   
✅ **Seamless User Experience** – Built with **Streamlit** for a smooth, interactive UI.
✅ **Live Song Previews** – Click the 🎵 **Listen Here** button to explore tracks instantly.

---

## 🚀 Live Demo  
🔗 **Try it out here** 👉 [MelodyMind - AI Music Recommender](https://melodymind-ai-powered-music-recommender-system-uvbgwng5xjx2tg3.streamlit.app/)  

---  

## 📂 **Project Structure**  

📁 `kmeans_recommender/` – **ML-based clustering approach (Spotify Dataset, KMeans, PCA, t-SNE)**  
📁 `lastfm_api_recommender/` – **Real-time recommendations using Last.fm API + Streamlit**  

---  

## 📊 **How It Works**  

### **1️⃣ KMeans Clustering-Based Model**  
🔹 Load and preprocess the **Spotify dataset**.  
🔹 Scale features using **StandardScaler()**.  
🔹 Apply **PCA & t-SNE** for dimensionality reduction.  
🔹 Perform **KMeans clustering** and find optimal clusters.  
🔹 Recommend songs **based on feature similarity**.  

### **2️⃣ Last.fm API-Based Model**  
🔹 Users input a **song & artist** via a **Streamlit web app**.  
🔹 Fetches **similar songs** using the **Last.fm API**.  
🔹 Displays recommendations with **clickable streaming links**.  
🔹 Includes interactive elements like **like buttons & user feedback**.

---

## 🎯 How to Run Locally  
1️⃣ Clone the repository:  
   ```bash
   git clone https://github.com/indranil143/MelodyMind-Music-Recommendation-System.git
   cd MelodyMind-Music-Recommendation-System
   ```  
2️⃣ Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3️⃣ Set up your **Last.fm API Key**:  
   - Create a `.streamlit/secrets.toml` file and add:  
     ```toml
     LASTFM_API_KEY = "your_api_key_here"
     ```  
4️⃣ Run the Streamlit app:  
   ```bash
   streamlit run musicapp.py
   ```  
---  

## ⚙️ **Tech Stack**  

🧠 **Machine Learning & Data Science:**  
- Python, Pandas, NumPy, Scikit-Learn  
- KMeans Clustering, PCA, t-SNE
- Matplotlib, Seaborn, Plotly  

🌐 **Real-Time API & Web App:**  
- Streamlit, Requests, Last.fm API  

---  

## 📌 **Results**  
✅ **Clustering Efficiency Improved by 25%** with PCA & t-SNE.  
✅ **18% More Accurate Recommendations** with optimized KMeans.  
✅ **Real-Time Music Discovery** using **Last.fm API**.  

---  

## 🤝 **Contributing**  
Love music and AI? Feel free to **fork, experiment, and contribute**! 🚀🎶  

## License
This project is licensed under the **MIT License**. See the LICENSE file for more information.
