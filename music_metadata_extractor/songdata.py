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
            logging.warning(ve, stack_info=True)
            raise ve
        except IndexError as ie:
            if str(ie) == "No data found in Spotify":
                logging.warning(ie, stack_info=True)
                raise ValueError("No data found on Spotify") from ie
        except AttributeError as ae:
            if str(ae) == "Error while parsing YouTube page":
                logging.warning(ae, stack_info=True)
                raise ValueError("Error while parsing YouTube page") from ie
        except Exception as e:
            logging.error(e, stack_info=True)
            raise ValueError("Unable to fetch metadata for input link") from e

    def __repr__(self):
        return "<SongData(\n\ttrack=%s,\n\tartists=%s,\n\textraAttrs=%s\n)>" % (
            self.track,
            self.artists,
            str(self.extraAttrs),
        )
