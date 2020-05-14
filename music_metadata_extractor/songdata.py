from typing import List
from .resolver import get_source_data
from .spotify import SpotifyProvider
from .models import Track, Artist, BaseProviderInput, BaseProvider
import logging

class SongData:
    """Contains all metadata to be consumed by users of this package"""

    def __init__(self, input_url: str):
        """Constructor for the SongData class."""
        provider_input,extraAttrs = get_source_data(input_url)
        try:
            provider_data: BaseProvider = SpotifyProvider(provider_input).data
            self.track: Track = provider_data.track
            self.artists: List[Artist] = provider_data.artists
        except IndexError as e:
            logging.warning(e, stack_info=True)
            self.track: Track = Track(provider_id=None, name=provider_input.song_name, is_cover=None, original_id=None, popularity=None, year=None, explicit=None, image_id=None, genre=[])
            self.artists: List[Artist] = []

        self.extraAttrs : dict = extraAttrs



    def __repr__(self):
        return "<SongData(\n\ttrack=%s,\n\tartists=%s,\n\textraAttrs=%s\n)>" % (self.track, self.artists , str(self.extraAttrs))
