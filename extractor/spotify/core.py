from extractor.spotify.client import spotify_client

class Track:
    def __init__(self, id):
        response = spotify_client.track(id)
        self.title = response['name']
        self.artists = [Artist(artist['id']) for artist in response['artists']]
        self.album = Album(response['album']['id'])

class Artist:
    def __init__(self, id):
        response = spotify_client.artist(id)
        self.name = response['name']
        self.id = response['id']
        self.genres = [Genre(genre) for genre in response['genres']]

class Album:
    def __init__(self, id):
        response = spotify_client.album(id)
        self.name = response['name']
        self.id = response['id']
    
    def get_artwork_link(self, dimension):
        for image_dict in response['images']:
            if(image_dict['width'] == dimension):
                return image_dict['url']

class Genre:
    def __init__(self, name):
        self.name = name;
        