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
        raise ValueError("Invalid YouTube URL!")

    return scrape_yt(soup)
