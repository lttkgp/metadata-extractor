"""Fetch YouTube URL information using the public API."""
from typing import Tuple

import requests
from bs4 import BeautifulSoup

from music_metadata_extractor.models import BaseProviderInput

from .scraper import YouTubeScraped


def get_info(url: str) -> Tuple[BaseProviderInput, dict]:
    """Generate provider input object for YouTube URL."""
    session = requests.Session()

    # In case of shortened links, get the original link
    response = session.head(url, allow_redirects=True)
    main_url = response.url

    main_response = requests.get(main_url)
    soup = BeautifulSoup(main_response.content, "lxml")

    try:
        scraped_data = YouTubeScraped(main_url, soup)
        return scraped_data.scrape_yt()
    except AttributeError as ae:
        if str(ae) == "'NoneType' object has no attribute 'text'":
            raise Exception("Error while parsing YouTube page") from ae
        else:
            raise ae
    except Exception as e:
        raise e
