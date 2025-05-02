import os
import streamlit as st
import requests
import pandas as pd
from rapidfuzz import process  # For fuzzy matching

#  Move this to the top before any other Streamlit command
st.set_page_config(page_title="🎶 MelodyMind - AI Music Recommender", layout="wide")

# Fetch API Key securely
API_KEY = os.getenv("LASTFM_API_KEY")  # Fetch from system environment

if not API_KEY:
    st.error("⚠️ API Key is missing! Make sure it's set correctly.")

BASE_URL = "http://ws.audioscrobbler.com/2.0/"

#  Function to correct spelling mistakes
def correct_spelling(query, choices):
    """Use fuzzy matching to correct user input."""
    result = process.extractOne(query, choices)
    
    # Ensure the result is a tuple and contains at least two elements (match and score)
    if result and isinstance(result, tuple) and len(result) == 2:
        match, score = result
        return match if score > 80 else query  # Only correct if confidence is high
    
    # If no match found or confidence is too low, return the original query
    return query

# Fetch top tracks for better recommendations
@st.cache_data
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

# Fetch song recommendations
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

# 🎶 App UI
st.title("🎵 MelodyMind - AI-Powered Music Recommendation System")
st.markdown("#### *Discover personalized music recommendations based on your unique taste!* 🎧✨")

# Load popular songs for fuzzy matching
popular_tracks = get_top_tracks()

# 🎧 User Inputs
song = st.text_input("🎧 *Enter a Song Name:*", "Shape of You")
artist = st.text_input("🎤 *Enter the Artist Name:*", "Ed Sheeran")

#  Auto-correct spelling mistakes
if popular_tracks:
    corrected_song = correct_spelling(song, popular_tracks)
    if corrected_song != song:
        st.info(f"🔍 Did you mean **{corrected_song}**? Using corrected name for better recommendations!")
        song = corrected_song

# 🔍 Fetch recommendations
if st.button("🔍 Get Recommendations"):
    with st.spinner("*Finding the best songs for you...* 🎼"):
        results = get_recommendations(song, artist)
        
        if results:
            df = pd.DataFrame(results)
            st.dataframe(df, use_container_width=True)  # Responsive table
            
            # 👍 Like Button for User Interaction
            if st.button("👍 Love These Picks! 💚"):
                st.success("*Glad you liked it! Keep vibing!* 🎶")
        else:
            st.warning("❌ *Oops! No recommendations found. Try a different song or artist.* 😢")

st.markdown("✨MelodyMind – Your ears will thank you later!🎧")
