import os
import requests
import streamlit as st

# Use a session object for connection pooling, which is more efficient.
session = requests.Session()

@st.cache_data(ttl=3600)
def _make_lastfm_api_request(params):

    API_KEY = os.getenv("LASTFM_API_KEY")
    if not API_KEY:
        # This error is critical and should stop the app.
        st.error("FATAL: Last.fm API Key is missing. Please set the 'LASTFM_API_KEY' environment variable.", icon="❌")
        st.stop()

    BASE_URL = "http://ws.audioscrobbler.com/2.0/"
    params["api_key"] = API_KEY
    params["format"] = "json"
    params["autocorrect"] = 1

    try:
        response = session.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        st.toast(f"API Request Failed: {e}", icon="🚫")
        return None

def _get_image_from_response(data, size='extralarge'):
# Safely extracts an image URL from an API response item.
    if not isinstance(data, dict) or 'image' not in data:
        return ""
    for image in data.get('image', []):
        if image.get('size') == size and image.get('#text'):
            return image['#text']
    return ""

@st.cache_data(ttl=3600)
def get_track_info(track_name, artist_name):
# Fetches detailed information for a single track.
    params = {"method": "track.getInfo", "track": track_name, "artist": artist_name}
    response_json = _make_lastfm_api_request(params)
    if not response_json or "track" not in response_json:
        return None
    track_data = response_json["track"]
    return {
        "name": track_data.get("name"),
        "artist": track_data.get("artist", {}).get("name"),
        "art": _get_image_from_response(track_data.get("album", {})),
        "tags": [tag["name"] for tag in track_data.get("toptags", {}).get("tag", [])],
        "summary": track_data.get("wiki", {}).get("summary", "No summary available.")
    }

@st.cache_data(ttl=3600)
def get_artist_info(artist_name):
# Fetches detailed information for a single artist.
    params = {"method": "artist.getInfo", "artist": artist_name}
    response_json = _make_lastfm_api_request(params)
    if not response_json or "artist" not in response_json:
        return None
    artist_data = response_json["artist"]
    return {
        "name": artist_data.get("name"),
        "art": _get_image_from_response(artist_data),
        "tags": [tag["name"] for tag in artist_data.get("tags", {}).get("tag", [])],
        "summary": artist_data.get("bio", {}).get("summary", "No biography available.")
    }

@st.cache_data(ttl=3600)
def get_recommendations(method, params, limit):
# Generic function to fetch a list of recommended tracks,
    params.update({"method": method, "limit": limit * 2})
    response_json = _make_lastfm_api_request(params)
    if not response_json: return []
    
    recommendations = []
    # Map API methods to the correct keys in the response
    item_key_map = {
        "track.getSimilar": ("similartracks", "track"),
        "artist.getTopTracks": ("toptracks", "track"),
        "tag.getTopTracks": ("tracks", "track")
    }
    if method not in item_key_map: return []
    
    item_key, item_list_key = item_key_map[method]
    items = response_json.get(item_key, {}).get(item_list_key, [])

    for item in items:
        if len(recommendations) >= limit: break
        track_name = item.get("name")
        artist_name = item.get("artist", {}).get("name")
        listen_url = item.get("url")

        # Ensure essential data is present before adding to the list
        if not all([track_name, artist_name, listen_url]): continue
        
        recommendations.append({
            "track": track_name,
            "artist": artist_name,
            "url": listen_url,
            "art": _get_image_from_response(item)
        })
    return recommendations

@st.cache_data(ttl=3600)
def get_similar_artists(artist_name, limit=5):
# Fetches similar artists for a given artist.
    params = {"method": "artist.getSimilar", "artist": artist_name, "limit": limit}
    response_json = _make_lastfm_api_request(params)
    if not response_json: return []
    artists_data = response_json.get("similarartists", {}).get("artist", [])
    return [artist["name"] for artist in artists_data if "name" in artist]

@st.cache_data(ttl=3600)
def get_top_tags_for_entity(entity_type, name, artist_name=None):
# Fetches top tags for either a track or an artist.
    if entity_type == "track":
        params = {"method": "track.getTopTags", "track": name, "artist": artist_name}
    elif entity_type == "artist":
        params = {"method": "artist.getTopTags", "artist": name}
    else:
        return []
        
    response_json = _make_lastfm_api_request(params)
    if not response_json: return []
    
    tags_data = response_json.get("toptags", {}).get("tag", [])
    return [tag.get("name") for tag in tags_data if tag.get("name")]

@st.cache_data(ttl=3600)
def search_track(track_name):
# Finds the top track match for a given query.
    params = {"method": "track.search", "track": track_name, "limit": 1}
    response = _make_lastfm_api_request(params)
    if not response: return None
    top_track = response.get("results", {}).get("trackmatches", {}).get("track", [None])[0]
    return top_track
