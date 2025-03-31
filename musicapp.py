import os
import streamlit as st 
import requests
import pandas as pd

# Fetch API Key securely
API_KEY = os.getenv("LASTFM_API_KEY")  # Fetch from system environment

if not API_KEY:
    st.error("⚠️ API Key is missing! Make sure it's set correctly.")

BASE_URL = "http://ws.audioscrobbler.com/2.0/"

# Function to get song recommendations
def get_recommendations(track, artist):
    params = {
        "method": "track.getSimilar",
        "api_key": API_KEY,
        "artist": artist,
        "track": track,
        "limit": 10,  # Fetch 10 recommendations
        "format": "json"
    }
    
    response = requests.get(BASE_URL, params=params).json()
    
    if "similartracks" in response and "track" in response["similartracks"]:
        return [
            {
                "Song": song["name"],
                "Artist": song["artist"]["name"],
                "Listen": f"[🎵 Listen Here]({song['url']})"
            }
            for song in response["similartracks"]["track"]
        ]
    return []

# Streamlit App UI
st.set_page_config(page_title="🎶 MelodyMind - AI Music Recommender", layout="wide")

st.title("🎵 MelodyMind - AI-Powered Music Recommendation System")
st.markdown("#### *Discover personalized music recommendations based on your unique taste!* 🎧✨")

# Input fields
song = st.text_input("🎧 *Enter a Song Name:*", "Shape of You")
artist = st.text_input("🎤 *Enter the Artist Name:*", "Ed Sheeran")

# Fetch recommendations
if st.button("🔍 Get Recommendations"):
    with st.spinner("*Finding the best songs for you...* 🎼"):
        results = get_recommendations(song, artist)
        
        if results:
            df = pd.DataFrame(results)
            st.dataframe(df, use_container_width=True)  # Responsive table
            
            # Interactive like button
            if st.button("👍 Love These Picks! 💚"):
                st.success("*Glad you liked it! Keep vibing!* 🎶")
        else:
            st.warning("❌ *Oops! No recommendations found. Try a different song or artist.* 😢")

st.markdown("✨MelodyMind – Your ears will thank you later!🎧")

