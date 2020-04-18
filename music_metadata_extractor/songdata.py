from .resolver import get_provider_input
from .spotify import SpotifyProvider


class SongData:
    def __init__(self, input_url):
        provider_input = get_provider_input(input_url)
        provider_data = SpotifyProvider(provider_input).data
        self.track = provider_data.track
        self.artists = provider_data.artists

    def __repr__(self):
        return "<SongData(\n\ttrack=%s,\n\tartists=%s\n)>" % (self.track, self.artists)
