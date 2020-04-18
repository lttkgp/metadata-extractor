from abc import ABC, abstractmethod


class BaseProviderInput:
    def __init__(self):
        super().__init__()


class StringInput(BaseProviderInput):
    def __init__(self, title_string):
        self.title_string = title_string

    def __repr__(self):
        return "<StringInput(title_string=%s)>" % (self.title_string)


class DictInput(BaseProviderInput):
    def __init__(self, song_name, artist_name):
        self.song_name = song_name
        self.artist_name = artist_name

    def __repr__(self):
        return "<DictInput(song_name=%s, artist_name=%s)>" % (
            self.song_name,
            self.artist_name,
        )


class ProviderInput(BaseProviderInput):
    def __init__(self, provider_url):
        self.provider_url = provider_url

    def __repr__(self):
        return "<ProviderInput(provider_url=%s)>" % (self.provider_url)


class BaseProvider(ABC):
    def __init__(self, input):
        if isinstance(input, StringInput):
            self.data = self.handle_string_input(input.title_string)
        elif isinstance(input, DictInput):
            self.data = self.handle_dict_input(input.song_name, input.artist_name)
        elif isinstance(input, ProviderInput):
            self.data = self.handle_provider_input(input.provider_url)
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
    def __init__(self, provider_id, name, image_id, genres):
        self.provider_id = provider_id
        self.name = name
        self.image_id = image_id
        self.genres = genres

    def __repr__(self):
        return "<Artist(provider_id=%s, name=%s, image_id=%s, genres=%s)>" % (
            self.provider_id,
            self.name,
            self.image_id,
            self.genres,
        )


class ProviderData:
    def __init__(self, track, artists):
        self.track = track
        self.artists = artists
