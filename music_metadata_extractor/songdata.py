from typing import List
from .resolver import get_source_data
from .spotify import SpotifyProvider
from .models import Track, Artist, BaseProviderInput, BaseProvider
import logging


class SongData:
    """Contains all metadata to be consumed by users of this package"""

    def __init__(self, input_url: str):
        """Constructor for the SongData class."""
        provider_input, extraAttrs = get_source_data(input_url)
        try:
            provider_data: BaseProvider = SpotifyProvider(provider_input).data
            self.track: Track = provider_data.track
            self.artists: List[Artist] = provider_data.artists
            self.extraAttrs: dict = extraAttrs
        except ValueError as ve:
            logging.warning(ve)
            raise ve
        except IndexError as ie:
            if str(ie) == "No data found in Spotify":
                self.track = None
                self.artists = []
                self.extraAttrs: dict = extraAttrs
                logging.warning(ie)
        except AttributeError as ae:
            if str(ae) == "Error while parsing YouTube page":
                logging.warning(ae)
                raise ValueError("Error while parsing YouTube page") from ae
        except Exception as e:
            logging.error(e)
            raise ValueError("Unable to fetch metadata for input link") from e

    def __repr__(self):
        return "<SongData(\n\ttrack=%s,\n\tartists=%s,\n\textraAttrs=%s\n)>" % (
            self.track,
            self.artists,
            str(self.extraAttrs),
        )
