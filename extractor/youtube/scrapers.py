from youtube_title_parse import get_artist_title
from extractor.youtube.helpers import clean_channel, check_key_get_value
from extractor.youtube.ytinfo import YouTubeInfo

# Scrapper function for videos without "Music in this video" section
def scrape_yt(soup):
    raw_title = soup.find('meta', {'property': 'og:title'}).get('content').strip()
    artist,title = None,None

    #In case the YouTube Title is in the commonly used format <Artist> - <Song name>
    if '-' in raw_title:
        raw_title =  get_artist_title(raw_title)
        artist, title = raw_title.split(' - ')

    # In case the  YouTube Title only contains song name    
    else :
        title = get_artist_title(raw_title)
        try:
            artist = soup.find('a',class_= "yt-uix-sessionlink spf-link").text  #Scrapes "Artist" from the YouTube Channel name 
            artist = clean_channel(artist)
        except AttributeError:
            artist = None

    return YouTubeInfo(title, artist)

# Scrapper function for videos with "Music in this video" section
def scrape_embedded_yt_metadata(soup):
    tags = soup.find_all('li', class_= "watch-meta-item yt-uix-expander-body")

    info = {}
    for tag in tags:
        key = tag.find('h4').text.strip()
        value = tag.find('ul').text.strip()
        info[key] =value 

    return YouTubeInfo(
        title=check_key_get_value(info, 'Song'),
        artist=check_key_get_value(info, 'Artist'),
        album=check_key_get_value(info, 'Album')
    )
