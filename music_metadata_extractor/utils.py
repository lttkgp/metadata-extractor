"""Helper functions used package-wide."""

from dotenv import find_dotenv, load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# env variables: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
load_dotenv(find_dotenv())

_client_credentials_manager = SpotifyClientCredentials()
_spotify_client = Spotify(
    client_credentials_manager=_client_credentials_manager)


def get_spotify_client():
    """Return a Spotify client, an object of class `spotipy.Spotify`."""
    return _spotify_client
