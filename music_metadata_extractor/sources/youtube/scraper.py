from typing import Tuple
from youtube_title_parse import get_artist_title
from .helpers import clean_channel, check_key_get_value
from music_metadata_extractor.models import BaseProviderInput, StringInput, DictInput
from datetime import datetime as dt


def __extraAttrs(soup) -> dict:

    yt_views = int(
        soup.find("div", class_="watch-view-count").text[:-6].replace(",", "")
    )
    raw_yt_date = soup.find("strong", class_="watch-time-text").text[-11:].strip()
    for fmt in ("%d-%b-%Y", "%d %b %Y"):
        try:
            yt_date = dt.strptime(raw_yt_date, fmt)
            if yt_date: break
        except ValueError as err:
            pass

    return {"youtube": {"views": yt_views, "posted_date": yt_date}}


def scrape_yt(soup) -> Tuple[BaseProviderInput, dict]:
    """Scraper function for YouTube videos"""
    # Check if video page has a "Music in this video" section
    if len(soup.find_all("li", class_="watch-meta-item yt-uix-expander-body")) > 1:
        output, extras = scrape_embedded_yt_metadata(soup)
        if output.song_name is not None and output.artist_name is not None:
            return output, extras

    raw_title = soup.find("meta", {"property": "og:title"}).get("content").strip()
    artist, title = None, None

    # In case the YouTube Title is in the commonly used format <Artist> - <Song name>
    if "-" in raw_title:
        raw_title = get_artist_title(raw_title)
        artist, title = raw_title.split(" - ")

    # In case the  YouTube Title only contains song name
    else:
        title = get_artist_title(raw_title)
        try:
            artist = soup.find(
                "a", class_="yt-uix-sessionlink spf-link"
            ).text  # Scrapes "Artist" from the YouTube Channel name
            artist = clean_channel(artist)
        except AttributeError:
            artist = None

    extra = __extraAttrs(soup)

    return DictInput(title, artist), extra


def scrape_embedded_yt_metadata(soup) -> Tuple[BaseProviderInput, dict]:
    """Scrapper function for videos with "Music in this video" section"""
    tags = soup.find_all("li", class_="watch-meta-item yt-uix-expander-body")

    info = {}
    for tag in tags:
        key = tag.find("h4").text.strip()
        value = tag.find("ul").text.strip()
        info[key] = value

    extras = __extraAttrs(soup)
    return (
        DictInput(
            song_name=check_key_get_value(info, "Song"),
            artist_name=check_key_get_value(info, "Artist"),
        ),
        extras,
    )
