import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

#  Page Configuration 
st.set_page_config(
    page_title="MelodyMind: Hybrid Music Recommender",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

#  Load Saved Components 
@st.cache_resource
def load_components(filepath='music_recommender_components.pkl'):
    """Loads the saved model components."""
    try:
        with open(filepath, 'rb') as f:
            components = pickle.load(f)
        st.success("Model components loaded successfully!", icon="✅")
        return components
    except FileNotFoundError:
        st.error(f"Error: '{filepath}' not found. Please ensure the file is in the same directory as app.py.", icon="❌")
        st.stop()
    except Exception as e:
        st.error(f"Error loading components: {e}", icon="❌")
        st.stop()

components = load_components()

# Extract components
lightfm_model = components['lightfm_model']
# scaler = components['scaler']
scaled_features = components['scaled_features']
data_lookup = components['data']
user_encoder = components['user_encoder']
# lightfm_user_id_map = components['lightfm_user_id_map']
original_item_id_map = components['original_item_id_map']
item_id_to_details = components['item_id_to_details']
idx_to_track_name = components['idx_to_track_name']
idx_to_artist_name = components['idx_to_artist_name']

num_items = len(original_item_id_map)

#  Helper Functions (Adapted from Notebook) 


def get_content_recommendations(track_name, all_features, data_df, idx_to_track, idx_to_artist, num_recommendations=10):
# Generates song recommendations based on content similarity, calculating similarity on-demand using scaled features. Returns a larger list (num_recommendations * 2) for hybrid combining.
    
    matching_indices = data_df[data_df['track_name'] == track_name].index
    if not matching_indices.any(): return []

    idx = matching_indices[0]

    target_features = all_features[idx].reshape(1, -1)
    sim_scores_vector = cosine_similarity(target_features, all_features)[0]

    sim_scores = list(enumerate(sim_scores_vector))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top N similar songs (exclude the track itself)
    try:
        input_track_sim_index = [i[0] for i in sim_scores].index(idx)
        
        top_indices = [i[0] for i in sim_scores if i[0] != idx][:num_recommendations * 2]
    except ValueError:
         # Fallback slicing
         top_indices = [i[0] for i in sim_scores[1:num_recommendations * 2 + 1]]


    return [(idx_to_track.get(i, 'Unknown'), idx_to_artist.get(i, 'Unknown')) for i in top_indices]



def get_lightfm_recommendations(user_id, model, num_recommendations=10):
# Generates recommendations for a given user_id using a trained LightFM model. Returns a larger list (num_recommendations * 2) for hybrid combining.

    lightfm_user_id_map = components['lightfm_user_id_map']

    if user_id not in lightfm_user_id_map:
        st.warning(f"User ID for selected artist not found in LightFM mapping.", icon="⚠️")
        return []

    internal_user_id = lightfm_user_id_map[user_id]
    all_item_indices = np.arange(num_items)

    scores = model.predict(internal_user_id, all_item_indices)

    # Get top N item indices based on scores
    
    top_internal_item_indices = np.argsort(-scores)[:num_recommendations * 2]

    # Map internal item indices back to original item IDs
    recommended_item_ids = [original_item_id_map.get(i) for i in top_internal_item_indices]

    # Get track details for the recommended item IDs
    recommendations = [item_id_to_details.get(item_id) for item_id in recommended_item_ids if item_id is not None and item_id in item_id_to_details]
    return recommendations


# This function's logic was already correct for combining and slicing the final output
def hybrid_recommendation(user_id, reference_track_name, num_recommendations=10):
# Generates hybrid recommendations combining content-based and collaborative filtering. Combines results from larger lists and returns the top N unique recommendations.

    st.info(f"Generating recommendations for User: **{user_encoder.classes_[user_id]}**, based on track: **'{reference_track_name}'**...", icon="🎧")

    # Generate recommendations from both methods (requesting more candidates)
    content_recs = get_content_recommendations(
        reference_track_name,
        scaled_features,
        data_lookup,
        idx_to_track_name,
        idx_to_artist_name,
        num_recommendations=num_recommendations # Pass the requested number here, slicing happens inside helper functions
    )

    collab_recs = get_lightfm_recommendations(user_id, lightfm_model, num_recommendations) # Pass the requested number here

    # Combine and deduplicate
    combined_recs = {}

    for track, artist in collab_recs:
        if (track, artist) not in combined_recs:
            combined_recs[(track, artist)] = "collab"

    for track, artist in content_recs:
        if (track, artist) not in combined_recs:
            combined_recs[(track, artist)] = "content"

    # Convert back to a list of tuples and take the top N unique recommendations
    final_recommendations = list(combined_recs.keys())

    # This slice ensures we return exactly the requested number (or fewer if not enough unique)
    return final_recommendations[:num_recommendations]


#  Streamlit UI 

st.title("🎧 MelodyMind: Hybrid Music Recommender")

st.markdown("""
Welcome to MelodyMind! This application provides personalized music recommendations
by combining insights from both the audio features of songs (Content-Based Filtering)
and patterns learned from user interactions (Collaborative Filtering).

**Simply select an artist (as a simulated user) and a reference track, and let MelodyMind find new music for you!**
""")

st.divider()

#  Sidebar for Input 
with st.sidebar:
    st.header("Configure Your Recommendations")

    available_artists = sorted(list(user_encoder.classes_))
    selected_artist = st.selectbox(
        "1. Choose an Artist (Simulated User):",
        available_artists,
        index=available_artists.index('Unknown') if 'Unknown' in available_artists else 0,
        help="Select an artist whose listening preferences we'll simulate."
    )

    tracks_by_selected_artist = data_lookup[data_lookup['primary_artist'] == selected_artist]['track_name'].unique()
    if len(tracks_by_selected_artist) > 0:
         available_tracks = sorted(list(tracks_by_selected_artist))
         selected_track = st.selectbox(
            "2. Choose a Reference Track:",
            available_tracks,
            index=0,
            help="Select a track that the system will use as a starting point for content-based similarity."
         )
    else:
         st.warning(f"No tracks found for '{selected_artist}'. Select a different artist or track.", icon="⚠️")
         available_tracks = sorted(data_lookup['track_name'].unique())
         selected_track = st.selectbox(
            "2. Choose a Reference Track:",
            available_tracks,
            index=min(100, len(available_tracks)-1),
            help="Select a track that the system will use as a starting point for content-based similarity."
         )


    num_recs = st.slider(
        "3. Number of Recommendations:",
        min_value=5,
        max_value=25,
        value=10,
        step=1,
        help="How many song recommendations would you like? (Max 25)" 
    )

    st.markdown("---")

    if st.button("Get Recommendations", use_container_width=True, type="primary"):
        st.session_state['get_recs'] = True
    else:
         if 'get_recs' not in st.session_state:
              st.session_state['get_recs'] = False


#  Display Recommendations 
if st.session_state['get_recs']:
    st.subheader("🔮 Your Personalized Recommendations:")

    try:
        user_id = user_encoder.transform([selected_artist])[0]

        recommendations = hybrid_recommendation(user_id=user_id,
                                                reference_track_name=selected_track,
                                                num_recommendations=num_recs) # Pass the requested number from slider

        if recommendations:
            recs_df = pd.DataFrame(recommendations, columns=['Track Title', 'Artist'])
            recs_df.index = np.arange(1, len(recs_df) + 1)

            st.dataframe(recs_df, use_container_width=True)

            st.markdown("---")
            st.markdown("Enjoy your new music discoveries! ✨")

        else:
            st.warning("Could not generate recommendations. Please try selecting a different artist or reference track.", icon="⚠️")

    except ValueError as ve:
        st.error(f"Error processing input artist: {ve}", icon="❌")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}", icon="❌")
        st.exception(e)

else:
     st.info("Select your preferences in the sidebar and click 'Get Recommendations' to begin!", icon="👆")


st.markdown("---")
st.markdown("Built with using LightFM and Streamlit.")
st.markdown("Find the project notebook [here](https://github.com/indranil143/Hybrid-Music-Recommendation-System)")