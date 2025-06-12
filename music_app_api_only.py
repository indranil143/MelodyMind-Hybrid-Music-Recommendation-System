import streamlit as st
from collections import OrderedDict
import time

# Import from our local utility files
from lastfm_api_utils import (
    get_track_info, get_artist_info, get_recommendations,
    get_similar_artists, get_top_tags_for_entity, search_track
)
from genre_assets import get_genre_image_url

# Page Configuration and Styling 
st.set_page_config(
    page_title="MelodyMind: Music Recommender 🎵",
    page_icon="🎶",
    layout="wide"
)

def load_css():

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
        .stApp { background-color: #111111; }
        .card { 
            background: rgba(40, 40, 50, 0.6); 
            border-radius: 12px; 
            padding: 1rem; 
            margin-bottom: 1rem; 
            border: 1px solid rgba(255, 255, 255, 0.1); 
            backdrop-filter: blur(10px); 
            transition: all 0.2s ease-in-out; 
            text-align: center;
            height: 100%;
        }
        .card:hover { 
            transform: translateY(-5px); 
            box-shadow: 0 8px 30px rgba(0, 255, 209, 0.2); 
        }
        .card img { border-radius: 8px; margin-bottom: 1rem; object-fit: cover; width: 100%; aspect-ratio: 1/1;}
        .card .title { font-size: 1.1rem; font-weight: 700; color: #FFFFFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .card .subtitle { font-size: 0.9rem; font-weight: 400; color: #AAAAAA; margin-bottom: 1rem; }
    </style>
    """, unsafe_allow_html=True)

#  Recommendation Engines 
def generate_recommendations(basis, num_recs):

    st.session_state.recommendations = OrderedDict()
    entity_type = basis['type']

    with st.spinner("🎧 Tuning into the right frequency..."):
        time.sleep(1) # Simulate work for better UX
        if entity_type == 'track':
            # Track-based flow: Similar Tracks -> Top Tracks from Similar Artists
            recs = get_recommendations("track.getSimilar", basis, limit=num_recs)
            for r in recs: st.session_state.recommendations[tuple(r.values())] = r
            if len(st.session_state.recommendations) < num_recs:
                st.spinner("Broadening the horizon with similar artists...")
                time.sleep(0.5)
                sim_artists = get_similar_artists(basis['artist'], limit=2)
                for sa in sim_artists:
                    recs = get_recommendations("artist.getTopTracks", {"artist": sa}, limit=2)
                    for r in recs: st.session_state.recommendations.setdefault(tuple(r.values()), r)

        elif entity_type == 'artist':
            # Artist-based flow: Artist's Top Tracks -> Top Tracks from Similar Artists
            recs = get_recommendations("artist.getTopTracks", basis, limit=num_recs)
            for r in recs: st.session_state.recommendations[tuple(r.values())] = r
            if len(st.session_state.recommendations) < num_recs:
                st.spinner("Discovering kindred spirits...")
                time.sleep(0.5)
                sim_artists = get_similar_artists(basis['artist'], limit=3)
                for sa in sim_artists:
                    recs = get_recommendations("artist.getTopTracks", {"artist": sa}, limit=2)
                    for r in recs: st.session_state.recommendations.setdefault(tuple(r.values()), r)

    # Post-process results to add fallback genre art
    with st.spinner("Adding the final artistic touches..."):
        time.sleep(1)
        for key, rec in list(st.session_state.recommendations.items()):
            if not rec.get('art'):
                tags = get_top_tags_for_entity('track', rec['track'], rec['artist'])
                st.session_state.recommendations[key]['art'] = get_genre_image_url(tags)


#  UI Display Functions 
def display_recommendations():

    recs_list = list(st.session_state.recommendations.values())[:st.session_state.num_recs]
    
    st.markdown("### 🔮 Your Personalized Recommendations:")
    
    cols = st.columns(4)
    for i, rec in enumerate(recs_list):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card">
                <img src="{rec['art']}" onerror="this.onerror=null;this.src='https://placehold.co/400x400/708090/FFFFFF?text=Music&font=inter';">
                <div class="title" title="{rec['track']}">{rec['track']}</div>
                <div class="subtitle">{rec['artist']}</div>
            </div>""", unsafe_allow_html=True)
            st.link_button("Listen on Last.fm 🎵", rec['url'], use_container_width=True)

def display_insights(basis):

    st.subheader("📊 Recommendation Insights")
    entity_type = basis['type']
    
    with st.spinner(f"Fetching insights for {basis.get('artist') or basis.get('track')}..."):
        info = get_artist_info(basis['artist']) if entity_type == 'artist' else get_track_info(basis['track'], basis['artist'])

    if not info:
        st.warning("Could not retrieve detailed insights for this selection.")
        return

    col1, col2 = st.columns([1, 2])
    with col1:
        art_url = info.get('art') or get_genre_image_url(info.get('tags', []))
        st.markdown(f'<img src="{art_url}" style="border-radius:12px;" onerror="this.onerror=null;this.src=\'https://placehold.co/400x400/708090/FFFFFF?text=Music&font=inter\';">', unsafe_allow_html=True)

    with col2:
        st.markdown(f"### {info['name']}")
        if entity_type == 'track': st.markdown(f"#### by {info['artist']}")
        st.markdown(f"**Top Tags:** `{'`, `'.join(info.get('tags',[]))}`")
        summary_text = info['summary'].split('. ', 1)[0] + '.' if '. ' in info['summary'] else info['summary']
        if not summary_text or "biography is not available" in summary_text.lower():
            summary_text = f"No detailed summary available for {info['name']}."
        st.markdown(f"<p style='color:#AAAAAA;'>{summary_text}</p>", unsafe_allow_html=True)


#  Main App Logic 
load_css()
st.title("🎧 MelodyMind: Music Recommender")

# Initialize session state for app flow
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'recommendation_basis' not in st.session_state:
    st.session_state.recommendation_basis = None

with st.sidebar:
    st.header("Start Your Discovery", "🎶")
    st.markdown("Enter an artist, a track, or both!")
    
    artist_input = st.text_input("Artist Name (Optional)", value="Linkin Park")
    track_input = st.text_input("Track Name (Optional)", value="Numb")
    st.session_state.num_recs = st.slider("Number of Recommendations", 4, 12, 8, 4)
    
    if st.button("Get Recommendations", use_container_width=True, type="primary"):
        st.session_state.recommendations = None # Clear previous results
        basis = None
        
        # --- HYBRID INPUT LOGIC ---
        if artist_input and track_input:
            basis = {'type': 'track', 'track': track_input, 'artist': artist_input}
        elif artist_input and not track_input:
            basis = {'type': 'artist', 'artist': artist_input}
        elif track_input and not artist_input:
            with st.spinner(f"Finding artist for '{track_input}'..."):
                top_track_match = search_track(track_input)
                if top_track_match:
                    st.info(f"Found **{top_track_match['name']}** by **{top_track_match['artist']}**. Using this for recommendations.", icon="💡")
                    basis = {'type': 'track', 'track': top_track_match['name'], 'artist': top_track_match['artist']}
                else:
                    st.error(f"Could not find a match for '{track_input}'. Please also provide an artist.", icon="❌")
        else:
            st.warning("Please enter an artist or a track name to begin.", icon="⚠️")
        
        st.session_state.recommendation_basis = basis
        st.rerun()

#  Main Panel Display Logic 
if st.session_state.recommendation_basis:
    if st.session_state.recommendations is None:
        st.markdown("##### Generating diverse recommendations...")
        generate_recommendations(st.session_state.recommendation_basis, st.session_state.num_recs)
    
    # Once recommendations are generated, show the tabs.
    tab1, tab2 = st.tabs(["🎵 Recommendations", "📊 Insights"])
    with tab1:
        display_recommendations()
    with tab2:
        display_insights(st.session_state.recommendation_basis)
else:
    # Default view when the app starts.
    st.markdown("""
    Welcome to MelodyMind! This application provides **diverse music recommendations**.  
                
    Our intelligent system attempts to **recognize your intended song/artist** even with typos.
                
    It can work with just an artist, just a track, or both!""")
    st.info("Enter an artist or track in the sidebar and start your journey! ", icon="👈")


st.markdown("---")
st.markdown("Built with ❤️ using Last.fm API and Streamlit.")
st.markdown("Find the Last.fm API documentation [here](https://www.last.fm/api).")
st.markdown("Find the project notebook for this project [here](https://github.com/indranil143/Hybrid-Music-Recommendation-System).")
