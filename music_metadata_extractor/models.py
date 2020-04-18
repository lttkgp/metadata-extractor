from abc import ABC, abstractmethod
from .resolver import get_provider_input
from .spotify import SpotifyProvider


class SongData:
    def __init__(self, input_url):
        self._get_metadata(input_url)

    def _get_metadata(self, input_url):
        provider_input = get_provider_input(input_url)
        provider_data = SpotifyProvider(provider_input)


class BaseProviderInput:
    def __init__(self):
        super().__init__()


class StringInput(BaseProviderInput):
    def __init__(self, title_string):
        self.title_string = title_string


class DictInput(BaseProviderInput):
    def __init__(self, song_name, artist_name):
        self.song_name = song_name
        self.artist_name = artist_name


class ProviderInput(BaseProviderInput):
    def __init__(self, provider_url):
        self.provider_url = provider_url


class BaseProvider(ABC):
    def __init__(self, input):
        if isinstance(input, StringInput):
            self.provider_data = self.handle_string_input(input.title_string)
        elif isinstance(input, DictInput):
            self.provider_data = self.handle_dict_input(
                input.song_name, input.artist_name
            )
        elif isinstance(input, ProviderInput):
            self.provider_data = self.handle_provider_input(input.provider_url)
        else:
            raise TypeError("Invalid input type")

    @abstractmethod
    def handle_string_input(self, title_string):
        raise NotImplementedError(
            "Provider implementation must override handle_input_string(input)"
        )

    @abstractmethod
    def handle_dict_input(self, song_name, artist_name):
        raise NotImplementedError(
            "Provider implementation must override handle_dict_input(input)"
        )

    @abstractmethod
    def handle_provider_input(self, provider_url):
        raise NotImplementedError(
            "Provider implementation must override handle_provider_input(input)"
        )


class Track:
    def __init__(
        self,
        provider_id,
        name,
        is_cover,
        original_id,
        popularity,
        year,
        explicit,
        image_id,
        genre,
    ):
        self.provider_id = provider_id
        self.name = name
        self.is_cover = is_cover
        self.original_id = original_id
        self.popularity = popularity
        self.year = year
        self.explicit = explicit
        self.image_id = image_id
        self.genre = genre


class Artist:
    def __init__(self, provider_id, name, image_id, genres):
        self.provider_id = provider_id
        self.name = name
        self.image_id = image_id
        self.genres = genres


class ProviderData:
    def __init__(self, track, artist, genre):
        self.track = track
        self.artist = artist
        self.genre = genre
