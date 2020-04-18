import requests
from bs4 import BeautifulSoup
from .helpers import is_valid_url
from .scraper import scrape_embedded_yt_metadata, scrape_yt
from music_metadata_extractor.models import BaseProviderInput


def get_info(url: str) -> BaseProviderInput:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    if not is_valid_url(soup):
        raise ValueError("Invalid YouTube URL!")

    return scrape_yt(soup)
