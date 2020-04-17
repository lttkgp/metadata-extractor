import requests
from bs4 import BeautifulSoup
from extractor.youtube.scrapers import scrape_embedded_yt_metadata, scrape_yt
from extractor.youtube.validator import yt_validate, available_video

def get_yt_info(url):
    if(not yt_validate(url)):
        raise ValueError("Enter YouTube URL!")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    if(not available_video(soup)):
        raise ValueError("Invalid YouTube URL!")

    if(len(soup.find_all('li',class_="watch-meta-item yt-uix-expander-body")) > 1 ):
        return scrape_embedded_yt_metadata(soup)
    return scrape_yt(soup)
