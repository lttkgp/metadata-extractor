from music_metadata_extractor.spotify.core import Track
from music_metadata_extractor.spotify.client import spotify_client

def get_track(**kwargs):
    if('artist' in kwargs.keys()):
        response = spotify_client.search(q=f"{kwargs['title']} artist:{kwargs['artist']}", type='track', limit=1)
    else:
        response = spotify_client.search(q=f"{kwargs['title']}", type='track', limit=1)
    try:
        return Track(response['tracks']['items'][0]['id'])
    except:
        return None
