import logging
from urllib import parse
from config import *


def convert_yt_music(input_url: str) -> str:
    url_parts = list(parse.urlparse(input_url))
    url_parts[1] = YOUTUBE_HOST
    return parse.urlunparse(url_parts)
