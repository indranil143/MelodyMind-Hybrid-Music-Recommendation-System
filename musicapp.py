import os
import streamlit as st
import requests
import pandas as pd
from rapidfuzz import process  # For fuzzy matching

# ✅ Move this to the top before any other Streamlit command
st.set_page_config(page_title="🎶 MelodyMind - AI Music Recommender", layout="wide")

# Fetch API Key securely
API_KEY = os.getenv("LASTFM_API_KEY")  # Fetch from system environment

if not API_KEY:
    st.error("⚠️ API Key is missing! Make sure it's set correctly.")

BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def correct_spelling(query, choices):
    """Use fuzzy matching to correct user input."""
    match, score = process.extractOne(query, choices)
    return match if score > 80 else query  # Only correct if confidence is high

def get_top_tracks():
    """Fetch a list of popular songs to use for fuzzy matching."""
    params = {
        "method": "chart.getTopTracks",
        "api_key": API_KEY,
        "format": "json",
        "limit": 100
    }
    response = requests.get(BASE_URL, params=params).json()
    return [track['name'] for track in response.get("tracks", {}).get("track", [])]

def get_recommendations(track, artist):
    params = {
        "method": "track.getSimilar",
        "api_key": API_KEY,
        "artist": artist,
        "track": track,
        "limit": 10,
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

st.title("🎵 MelodyMind - AI-Powered Music Recommendation System")
st.markdown("#### *Discover personalized music recommendations based on your unique taste!* 🎧✨")

# Load popular songs for fuzzy matching
popular_tracks = get_top_tracks()

# Input fields
song = st.text_input("🎧 *Enter a Song Name:*", "Shape of You")
artist = st.text_input("🎤 *Enter the Artist Name:*", "Ed Sheeran")

# Auto-correct spelling mistakes
if popular_tracks:
    song = correct_spelling(song, popular_tracks)

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
