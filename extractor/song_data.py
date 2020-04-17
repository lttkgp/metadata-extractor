from extractor.youtube import get_yt_info
from extractor.spotify import get_track

class SongData:
    def __init__(self, yt_url):
        yt_data = get_yt_info(yt_url)
        self.title = yt_data.title
        if(yt_data.artist):
            sp_data = get_track(title=yt_data.title, artist=yt_data.artist)
        else:
            sp_data = get_track(title=yt_data)
        if(sp_data):
            self.artists = sp_data.artists
            self.album = sp_data.album
        else:
            self.artists = yt_data.artist
            self.album = yt_data.album
