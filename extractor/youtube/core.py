import requests
from bs4 import BeautifulSoup
from youtube_title_parse import get_artist_title

def scrape_yt(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    raw_title = soup.find('meta', {'property': 'og:title'}).get('content').strip()
    artist, title = raw_title.split(' - ')
    return artist, title
