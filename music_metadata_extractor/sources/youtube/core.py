import requests
from bs4 import BeautifulSoup
from .helpers import is_valid_url
from .scraper import scrape_embedded_yt_metadata, scrape_yt


def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    if not is_valid_url(soup):
        raise ValueError("Invalid YouTube URL!")

    return scrape_yt(soup)
