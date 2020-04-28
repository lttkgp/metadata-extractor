from typing import List
from .resolver import get_provider_input
from .spotify import SpotifyProvider
from .models import Track, Artist, BaseProviderInput, BaseProvider


class SongData:
    """Contains all metadata to be consumed by users of this package"""

    def __init__(self, input_url: str):
        """Constructor for the SongData class."""
        provider_input: BaseProviderInput = get_provider_input(input_url)
        try:
            provider_data: BaseProvider = SpotifyProvider(provider_input).data
            self.track: Track = provider_data.track
            self.artists: List[Artist] = provider_data.artists
        except:
            self.track: Track = Track(provider_id=None, name=provider_input.song_name, is_cover=None, original_id=None, popularity=None, year=None, explicit=None, image_id=None, genre=[])
            self.artists: List[Artist] = []


    def __repr__(self):
        return "<SongData(\n\ttrack=%s,\n\tartists=%s\n)>" % (self.track, self.artists)
