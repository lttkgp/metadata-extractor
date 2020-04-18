from music_metadata_extractor import SongData


def test_songData():
    song_data = SongData("https://www.youtube.com/watch?v=XoYu7K6Ywkg")
    assert song_data is not None

    track = song_data.track
    artists = song_data.artists
    assert track.name == "Last Hope"
    assert artists[0].name == "Paramore"
