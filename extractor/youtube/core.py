import requests
from bs4 import BeautifulSoup
from extractor.youtube.helpers import get_yt_link
from extractor.youtube.scrapers import scrape_embedded_yt_metadata, scrape_yt

def get_yt_info(url):
    link = get_yt_link(url)
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'lxml')

    if(len(soup.find_all('li',class_="watch-meta-item yt-uix-expander-body")) > 1 ):
        return scrape_embedded_yt_metadata(soup)
    return scrape_yt(soup)