import requests
from bs4 import BeautifulSoup
from .helpers import is_valid_url
from .scraper import scrape_embedded_yt_metadata, scrape_yt


def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    if not is_valid_url(soup):
        raise ValueError("Invalid YouTube URL!")

    if len(soup.find_all("li", class_="watch-meta-item yt-uix-expander-body")) > 1:
        return scrape_embedded_yt_metadata(soup)
    return scrape_yt(soup)
