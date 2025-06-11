# genre_assets.py

def get_genre_image_url(tags: list) -> str:
# Analyzes a list of genre tags and returns a URL to a suitable genre image. 
# This uses placehold.co to generate clean, labeled images for a modern look.
    # Prioritized mapping of keywords to genre images. The first match wins.
    genre_map = {
        'rock': 'https://placehold.co/400x400/FF6347/FFFFFF?text=Rock&font=inter',
        'metal': 'https://placehold.co/400x400/4F4F4F/FFFFFF?text=Metal&font=inter',
        'punk': 'https://placehold.co/400x400/FF00FF/FFFFFF?text=Punk&font=inter',
        'indie': 'https://placehold.co/400x400/20B2AA/FFFFFF?text=Indie&font=inter',
        'alternative': 'https://placehold.co/400x400/778899/FFFFFF?text=Alternative&font=inter',
        'hip hop': 'https://placehold.co/400x400/8A2BE2/FFFFFF?text=Hip+Hop&font=inter',
        'rap': 'https://placehold.co/400x400/8A2BE2/FFFFFF?text=Rap&font=inter',
        'trap': 'https://placehold.co/400x400/5F4B8B/FFFFFF?text=Trap&font=inter',
        'electronic': 'https://placehold.co/400x400/00FFFF/000000?text=Electronic&font=inter',
        'techno': 'https://placehold.co/400x400/00008B/FFFFFF?text=Techno&font=inter',
        'house': 'https://placehold.co/400x400/DE3163/FFFFFF?text=House&font=inter',
        'edm': 'https://placehold.co/400x400/7B68EE/FFFFFF?text=EDM&font=inter',
        'synthpop': 'https://placehold.co/400x400/FF00FF/FFFFFF?text=Synthpop&font=inter',
        'ambient': 'https://placehold.co/400x400/4682B4/FFFFFF?text=Ambient&font=inter',
        'pop': 'https://placehold.co/400x400/FF69B4/FFFFFF?text=Pop&font=inter',
        'jazz': 'https://placehold.co/400x400/FFD700/000000?text=Jazz&font=inter',
        'blues': 'https://placehold.co/400x400/0000CD/FFFFFF?text=Blues&font=inter',
        'soul': 'https://placehold.co/400x400/8B0000/FFFFFF?text=Soul&font=inter',
        'funk': 'https://placehold.co/400x400/FFA500/000000?text=Funk&font=inter',
        'r&b': 'https://placehold.co/400x400/DA70D6/FFFFFF?text=R%26B&font=inter',
        'classical': 'https://placehold.co/400x400/D2B48C/FFFFFF?text=Classical&font=inter',
        'orchestral': 'https://placehold.co/400x400/BDB76B/FFFFFF?text=Orchestral&font=inter',
        'folk': 'https://placehold.co/400x400/8B4513/FFFFFF?text=Folk&font=inter',
        'acoustic': 'https://placehold.co/400x400/CD853F/FFFFFF?text=Acoustic&font=inter',
        'country': 'https://placehold.co/400x400/B8860B/FFFFFF?text=Country&font=inter',
    }

    # Normalize tags to a single lowercase string for easy searching
    lower_tags = ' '.join(tags).lower()

    # Find the first matching keyword in the tags
    for keyword, url in genre_map.items():
        if keyword in lower_tags:
            return url

    # If no specific genre is found, return a cool, generic music icon.
    return 'https://placehold.co/400x400/708090/FFFFFF?text=Music&font=inter'
