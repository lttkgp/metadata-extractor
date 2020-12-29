# metadata-extractor

Package to fetch music metadata from common Music APIs from a variety of data sources. 

Currently, YouTube, YouTube Music and Spotify links are supported and data is fetched from Spotify APIs.

## Installation
```
pip install music-metadata-extractor
```
Ensure that the `.env` file for your project has all the environment variables defined in `.env.template`. 

`SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` can be obtained by creating a new app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

Similarly, you can get `GOOGLE_APPLICATION_CREDENTIALS` by creating a new project on the [Google Developer Console](https://console.developers.google.com/). Enable the `YouTube Data API` and create credentials. Use the API key you get in the `GOOGLE_APPLICATION_CREDENTIALS`.

## Usage

Example
```python
from music_metadata_extractor import SongData
data = SongData("https://www.youtube.com/watch?v=xwtdhWltSIg")
print(data)
```
The output is in the format
```
<SongData(
	track=<Track(provider_id=31AOj9sFz2gM0O3hMARRBx, name=Losing My Religion, is_cover=False, original_id=None,popularity=82, year=1991-03-12, explicit=False, image_id=https://i.scdn.co/image/ab67616d0000b273e2dd4e821bcc3f70dc0c8ffd, genres=[])>,
	artists=[<Artist(provider_id=4KWTAlx2RvbpseOGMEmROg, name=R.E.M., image_id=https://i.scdn.co/image/d24ff8fbfd6688b345a5d53acff032d2ac1ff387, genres=['alternative rock', 'classic rock', 'permanent wave', 'pop rock', 'rock'])>],
	extraAttrs={'youtube': {'title': 'R.E.M. - Losing My Religion (Official Music Video)', 'views': '770535535', 'posted_date': datetime.datetime(2011, 7, 2, 0, 30, 31, tzinfo=tzutc()), 'converted_link': 'https://www.youtube.com/watch?v=xwtdhWltSIg'}}
)>

```
`music.youtube.com/watch` links and `open.spotify.com/track/` are also supported as inputs to `SongData`. 

YouTube Music and Spotify links are converted to their equivalent YouTube links and returned in the `converted_link` field of the `extraAttrs` attribute.

