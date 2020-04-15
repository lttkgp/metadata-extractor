from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# env variables: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials()
spotify_client = Spotify(client_credentials_manager=client_credentials_manager)

def search(query):
    return spotify_client.search(q=query['q'], type=query['type'], limit=1)

if __name__ == "__main__":
    import json
    with open('sample.json', 'w') as f:
        json.dump(search({
            'q': 'Bohemian Rhapsody',
            'type': 'track'
        }), f)