from extractor.youtube.core import get_yt_info

## TODO: Add spotify data to SongData

class SongData:
    def __init__(self, yt_url):
        yt_data = get_yt_info(yt_url)
        self.title = yt_data.title
        self.artist = yt_data.artist
        self.album = yt_data.album
        self.yt_url = yt_url

