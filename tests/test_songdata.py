from music_metadata_extractor import SongData
from datetime import datetime


def test_songData():
    song_data = SongData("https://www.youtube.com/watch?v=XoYu7K6Ywkg")
    assert song_data is not None

    track = song_data.track
    artists = song_data.artists
    extraAttrs = song_data.extraAttrs
    assert track.name == "Last Hope"
    assert artists[0].name == "Paramore"
    assert extraAttrs["youtube"]["posted_date"] == datetime(2014, 9, 1, 0, 0)
