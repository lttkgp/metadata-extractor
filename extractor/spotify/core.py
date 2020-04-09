from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import urllib.parse as parser

load_dotenv(find_dotenv())
# env variables: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials()
sp = Spotify(client_credentials_manager=client_credentials_manager)

def search(query):
    return sp.search(q=parser.quote(query['q']), limit=query['limit'])

