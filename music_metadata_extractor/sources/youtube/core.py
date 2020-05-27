import requests
from typing import Tuple
from bs4 import BeautifulSoup
from .helpers import is_valid_url
from .scraper import scrape_embedded_yt_metadata, scrape_yt
from music_metadata_extractor.models import BaseProviderInput


def get_info(url: str) -> Tuple[BaseProviderInput, dict]:
    """Generate provider input object for YouTube URL"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    if not is_valid_url(soup):
        raise ValueError("Video unavailable!")

    try:
        return scrape_yt(soup)
    except AttributeError as ae:
        if str(ae) == "'NoneType' object has no attribute 'text'":
            raise Exception("Error while parsing YouTube page") from ae
        else:
            raise ae
    except Exception as e:
        raise e
