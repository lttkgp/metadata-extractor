"""Import functions from the corresponding modules and export to users of the package."""

from .youtube import get_info as get_yt_info
from .youtube_music.converter import convert_yt_music
from .spotify import get_info as get_spotify_info