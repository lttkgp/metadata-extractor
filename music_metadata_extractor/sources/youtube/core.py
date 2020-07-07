import requests
from typing import Tuple
from bs4 import BeautifulSoup
from .helpers import is_valid_url
from .scraper import YouTubeScraped
from music_metadata_extractor.models import BaseProviderInput


def get_info(url: str) -> Tuple[BaseProviderInput, dict]:
    """Generate provider input object for YouTube URL"""
    session = requests.Session()
    
    # In case of shortened links, get the original link
    response = session.head(url, allow_redirects=True)
    main_url = response.url
    
    main_response = requests.get(main_url)
    soup = BeautifulSoup(main_response.content, "lxml")

    if not is_valid_url(soup):
        raise ValueError("Video unavailable!")

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
