from enum import Enum
from datetime import datetime
import pytest
from music_metadata_extractor import SongData


class Expected(Enum):
    PASS = 1
    NO_METADATA_FOUND = 2  # See if we can convert these to PASS
    UNSUPPORTED_LINK = 3  # Support these links if possible
    VIDEO_UNAVAILABLE = 4
    VIDEO_UNABAILABLE_TO_PARSER = 5  # Add support to verify cause (deleted vs region)


tests = [
    {
        "link": "https://www.youtube.com/watch?v=XoYu7K6Ywkg",
        "expectation": Expected.PASS,
        "result": {"name": "Last Hope", "artists": ["Paramore"],},
    },
    {"link": "https://youtu.be/q604eed4ad0", "expectation": Expected.NO_METADATA_FOUND},
    {"link": "https://youtu.be/nXTtA5bKHrM", "expectation": Expected.NO_METADATA_FOUND},
    {
        "link": "https://www.youtube.com/watch?v=VaGDSHBV1dQ",
        "expectation": Expected.PASS,
        "result": {"name": "Deadmen", "artists": ["SAINT PHNX"],},
    },
    {
        "link": "https://youtu.be/Il7Nv270zNk",
        "expectation": Expected.PASS,
        "result": {"name": "cold/mess", "artists": ["Prateek Kuhad"],},
    },
    {
        "link": "https://www.youtube.com/attribution_link?a=BQnXYx6P5Zw&u=%2Fwatch%3Fv%3DPib8eYDSFEI%26feature%3Dshare",
        "expectation": Expected.UNSUPPORTED_LINK,
    },
    {
        "link": "https://www.youtube.com/watch?v=LE20ORdjaxw",
        "expectation": Expected.PASS,
        "result": {"name": "Another Time", "artists": ["City of the Sun"],},
    },
    {
        "link": "https://youtu.be/sh55BDdjxu4",
        "expectation": Expected.NO_METADATA_FOUND,
    },
    {
        "link": "https://www.youtube.com/watch?v=CYDM-8jAG6U&list=RDCYDM-8jAG6U&start_radio=1",
        "expectation": Expected.NO_METADATA_FOUND,
    },
    # Unavailable video
    {"link": "https://youtu.be/VrBKxr309i4", "expectation": Expected.VIDEO_UNAVAILABLE},
    {
        "link": "https://www.youtube.com/watch?v=VLnWf1sQkjY",
        "expectation": Expected.PASS,
        "result": {
            "name": "Jizz In My Pants",
            "artists": ["The Lonely Island"]
        }
    },
    {
        "link": "https://youtu.be/DoqNQGakX7g",
        "expectation": Expected.PASS,
        "result": {"name": "Vision", "artists": ["Simmy"],},
    },
    {"link": "https://youtu.be/cSExygIJBoE", "expectation": Expected.NO_METADATA_FOUND},
    {
        "link": "https://www.youtube.com/attribution_link?a=wEtuCP2uXaQ&u=%2Fwatch%3Fv%3DJ9AqA2gJ38M%26feature%3Dshare",
        "expectation": Expected.UNSUPPORTED_LINK,
    },
    {
        "link": "https://youtu.be/Y7ix6RITXM0",
        "expectation": Expected.PASS,
        "result": {"name": "Maps", "artists": ["Maroon 5"],},
    },
    {
        "link": "https://www.youtube.com/watch?v=IEF6mw7eK4s",
        "expectation": Expected.NO_METADATA_FOUND,
    },
    {
        "link": "https://www.youtube.com/watch?v=Ozo8LyvS4fE",
        "expectation": Expected.NO_METADATA_FOUND,
        # "result": {"name": "Let Me Live / Let Me Die", "artists": ["Des Rocs"],},
    },
    {
        "link": "https://www.youtube.com/watch?v=4--OKda1qzU",
        "expectation": Expected.PASS,
        "result": {"name": "Moving on", "artists": ["Kodaline"],},
    },
]


@pytest.mark.parametrize("test_params", tests)
def test_songData(test_params):
    input_song_link = test_params["link"]
    expectation = test_params["expectation"]
    print('\n')
    print(input_song_link)
    if expectation is Expected.NO_METADATA_FOUND:
        song_data = SongData(input_song_link)
        print(song_data)
        assert song_data.track is None
        assert len(song_data.artists) == 0
        assert song_data.extraAttrs is not None
        assert song_data.extraAttrs['youtube']['views'] is not None
        assert song_data.extraAttrs['youtube']['posted_date'] is not None
    elif expectation is Expected.VIDEO_UNABAILABLE_TO_PARSER:
        with pytest.raises(ValueError, match="Error while parsing YouTube page"):
            song_data = SongData(input_song_link)
    elif expectation is Expected.UNSUPPORTED_LINK:
        with pytest.raises(ValueError, match="Unsupported URL!"):
            song_data = SongData(input_song_link)
    elif expectation is Expected.VIDEO_UNAVAILABLE:
        with pytest.raises(ValueError, match="Video unavailable!"):
            song_data = SongData(input_song_link)
    else:
        song_data = SongData(input_song_link)
        expected_data = test_params["result"]
        print(song_data)
        assert song_data is not None

        track = song_data.track
        artists = song_data.artists
        assert track.name == expected_data["name"]
        assert artists[0].name == expected_data["artists"][0]
