from abc import ABC, abstractmethod
from typing import List


class Track:
    def __init__(
        self,
        provider_id: str,
        name: str,
        is_cover: bool,
        original_id: str,
        popularity: int,
        year: str,
        explicit: bool,
        image_id: str,
        genre: List[str],
    ):
        self.provider_id: str = provider_id
        self.name: str = name
        self.is_cover: bool = is_cover
        self.original_id: str = original_id
        self.popularity: int = popularity
        self.year: str = year
        self.explicit: bool = explicit
        self.image_id: str = image_id
        self.genre: List[str] = genre

    def __repr__(self):
        return (
            "<Track(provider_id=%s, name=%s, is_cover=%s, original_id=%s, popularity=%d, year=%s, explicit=%s, image_id=%s, genres=%s)>"
            % (
                self.provider_id,
                self.name,
                self.is_cover,
                self.original_id,
                self.popularity,
                self.year,
                self.explicit,
                self.image_id,
                self.genre,
            )
        )


class Artist:
    def __init__(self, provider_id: str, name: str, image_id: str, genres: List[str]):
        self.provider_id: str = provider_id
        self.name: str = name
        self.image_id: str = image_id
        self.genres: List[str] = genres

    def __repr__(self):
        return "<Artist(provider_id=%s, name=%s, image_id=%s, genres=%s)>" % (
            self.provider_id,
            self.name,
            self.image_id,
            self.genres,
        )


class ProviderData:
    def __init__(self, track: Track, artists: List[Artist]):
        self.track: Track = track
        self.artists: List[Artist] = artists


class BaseProviderInput:
    def __init__(self):
        super().__init__()


class StringInput(BaseProviderInput):
    def __init__(self, title_string: str):
        self.title_string: str = title_string

    def __repr__(self):
        return "<StringInput(title_string=%s)>" % (self.title_string)


class DictInput(BaseProviderInput):
    def __init__(self, song_name: str, artist_name: str):
        self.song_name: str = song_name
        self.artist_name: str = artist_name

    def __repr__(self):
        return "<DictInput(song_name=%s, artist_name=%s)>" % (
            self.song_name,
            self.artist_name,
        )


class ProviderInput(BaseProviderInput):
    def __init__(self, provider_url: str):
        self.provider_url: str = provider_url

    def __repr__(self):
        return "<ProviderInput(provider_url=%s)>" % (self.provider_url)


class BaseProvider(ABC):
    def __init__(self, input: BaseProviderInput):
        if isinstance(input, StringInput):
            self.data = self.handle_string_input(input.title_string)
        elif isinstance(input, DictInput):
            self.data = self.handle_dict_input(input.song_name, input.artist_name)
        elif isinstance(input, ProviderInput):
            self.data = self.handle_provider_input(input.provider_url)
        else:
            raise TypeError("Invalid input type")

    @abstractmethod
    def handle_string_input(self, title_string: str) -> ProviderData:
        raise NotImplementedError(
            "Provider implementation must override handle_input_string(input)"
        )

    @abstractmethod
    def handle_dict_input(self, song_name: str, artist_name: str) -> ProviderData:
        raise NotImplementedError(
            "Provider implementation must override handle_dict_input(input)"
        )

    @abstractmethod
    def handle_provider_input(self, provider_url: str) -> ProviderData:
        raise NotImplementedError(
            "Provider implementation must override handle_provider_input(input)"
        )
