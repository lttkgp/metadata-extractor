from typing import List
from spotipy import Spotify
from .utils import get_spotify_client
from .models import BaseProvider, ProviderData, BaseProviderInput
from .models import Track, Artist

SPOTIFY_CLIENT = get_spotify_client()


class SpotifyProvider(BaseProvider):
    def __init__(self, input: BaseProviderInput):
        super().__init__(input)

    def handle_string_input(self, title_string: str) -> ProviderData:
        return search(title=title_string)

    def handle_dict_input(self, song_name: str, artist_name: str) -> ProviderData:
        return search(title=song_name, artist=artist_name)

    def handle_provider_input(self, provider_url: str) -> ProviderData:
        return search(id=provider_url)


def get_artist(id: str) -> Artist:
    """
    Method to call Spotify's `artist` endpoint.
    Documentation: https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/

    Arguments:
        id {str} -- Spotify artist ID

    Returns:
        Artist -- contains required artist metadata
    """
    response = SPOTIFY_CLIENT.artist(id)
    artist_id = response["id"]
    artist_name = response["name"]
    artist_image = response["images"][0]["url"]
    genres = [genre for genre in response["genres"]]
    artist = Artist(artist_id, artist_name, artist_image, genres)
    return artist


def get_artists(ids: List[str]) -> List[Artist]:
    """
    Method to call Spotify's `artists` endpoint.
    Documentation: https://developer.spotify.com/documentation/web-api/reference/artists/get-several-artists/

    Arguments:
        ids {List[str]} -- List of Spotify artist IDs

    Returns:
        List[Artist] -- contains required artist metadata for all input IDs
    """
    artists = []
    response = SPOTIFY_CLIENT.artists(ids)
    for artist in response["artists"]:
        artist_id = artist["id"]
        artist_name = artist["name"]
        artist_image = artist["images"][0]["url"]
        genres = [genre for genre in artist["genres"]]
        artist = Artist(artist_id, artist_name, artist_image, genres)
        artists.append(artist)
    return artists


def parse_track_response(track_data: dict) -> ProviderData:
    """Generate ProviderData from search response (made with type="track")"""
    track_id = track_data["id"]
    song_name = track_data["name"]
    is_cover = False
    original_id = None
    popularity = track_data["popularity"]
    explicit = track_data["explicit"]

    year = track_data["album"]["release_date"]
    image_id = track_data["album"]["images"][0]["url"]
    genres = []

    track = Track(
        track_id,
        song_name,
        is_cover,
        original_id,
        popularity,
        year,
        explicit,
        image_id,
        genres,
    )

    artist_ids = [artist["id"] for artist in track_data["artists"]]
    artists = get_artists(artist_ids)

    provider_data = ProviderData(track, artists)
    return provider_data


def search(**kwargs) -> ProviderData:
    """
    Method to call Spotify's `search` endpoint.
    Documentation: https://developer.spotify.com/documentation/web-api/reference/search/search/

    Raises:
        IndexError: if metadata is not found on Spotify

    Returns:
        ProviderData -- contains track and artists information
    """
    if "id" in kwargs.keys():
        response = SPOTIFY_CLIENT.track(id)
    elif "artist" in kwargs.keys():
        response = SPOTIFY_CLIENT.search(
            q=f"{kwargs['title']} artist:{kwargs['artist']}", type="track", limit=1
        )
    else:
        response = SPOTIFY_CLIENT.search(q=f"{kwargs['title']}", type="track", limit=1)
    track_data = response["tracks"]["items"][0]
    if not track_data:
        raise IndexError("No data found in Spotify")
    response = parse_track_response(track_data)
    return response
