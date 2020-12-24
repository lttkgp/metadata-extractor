"""Convert YouTube Music URLs to YouTube URLs."""
import logging
from urllib import parse

from music_metadata_extractor.config import *


def convert_yt_music(input_url: str) -> str:
    """
    Convert a YouTube Music link to a YouTube link.

    YouTube Music videos share the same `v` URL parameter as their YouTube counterparts
    and hence can be processed like YouTube URLs after making changes to the URL
    This function replaces the `music.youtube.com` part of the URL with `youtube.com`

    As an example:
    `input_url`: https://music.youtube.com/watch?v=J7p4bzqLvCw&list=RDAMVMJ7p4bzqLvCw
    Returns: https://youtube.com/watch?v=J7p4bzqLvCw&list=RDAMVMJ7p4bzqLvCw
    """
    url_parts = list(parse.urlparse(input_url))
    url_parts[1] = YOUTUBE_HOST
    return parse.urlunparse(url_parts)
