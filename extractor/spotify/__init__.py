from extractor.spotify.core import spotify_client, search

class Track:
    def __init__(self, title):
        data = search({
            'q': title,
            'type': 'track'
        })['tracks']['items'][0]
        self.title = data['name']
        self.artists = [Artist(artist['id']) for artist in data['artists']]
        self.album = Album(data['album']['id'])

class Artist:
    def __init__(self, id):
        response = spotify_client.artist(id)
        self.name = response['name']
        self.id = response['id']
        self.genres = response['genres']

    def get_spotify_link(self):
        return f'https://open.spotify.com/artist/{self.id}'

class Album:
    def __init__(self, id):
        response = spotify_client.album(id)
        self.name = response['name']
        self.id = response['id']
    
    def get_artwork_link(self, dimension):
        for image_dict in response['images']:
            if(image_dict['width'] == dimension):
                return image_dict['url']