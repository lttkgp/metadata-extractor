import requests
from bs4 import BeautifulSoup
from youtube_title_parse import get_artist_title
from helpers import get_yt_link, clean_channel

# Scrapper function for videos without "Music in this video" section
def scrape_yt(soup):
    raw_title = soup.find('meta', {'property': 'og:title'}).get('content').strip()
    artist,title = None,None

    #In case the YouTube Title is in good format,i.e, Artist-Song("foo")
    if '-' in raw_title:
        raw_title =  get_artist_title(raw_title)
        artist, title = raw_title.split(' - ')

    # In case the  YouTube Title only contains song name    
    else :
        title = get_artist_title(raw_title)
        artist = soup.find('a',class_= "yt-uix-sessionlink spf-link").text
        artist = clean_channel(artist)

    info = {'Category': None , 'Song' :title, 'Artist':artist, 'Album':None, 'Licensed to YouTube by' : None}
    return info

# Scrapper function for videos with "Music in this video" section
def scrape_yt_new(soup):
    tags = soup.find_all('li', class_= "watch-meta-item yt-uix-expander-body")

    info = {'Category': None, 'Song':None, 'Artist': None, 'Album':None, 'Licensed to YouTube by':None}

    for tag in tags:
        key = tag.find('h4').text.strip()
        value = tag.find('ul').text.strip()

        if key in info :
            info[key] =value 

    return info

def scrape(url):
    link = get_yt_link(url)
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'lxml')

    if(len(soup.find_all('li',class_="watch-meta-item yt-uix-expander-body")) > 1 ):
        return scrape_yt_new(soup)
    return scrape_yt(soup)

