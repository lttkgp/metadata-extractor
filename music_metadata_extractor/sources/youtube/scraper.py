from typing import Tuple

from youtube_title_parse import get_artist_title
from .helpers import clean_channel, check_key_get_value
from music_metadata_extractor.models import BaseProviderInput, StringInput, DictInput

import requests
import googleapiclient.discovery

from os import getenv
from urllib import parse
from dotenv import load_dotenv, find_dotenv
from dateutil.parser import isoparse as isoparser
load_dotenv(find_dotenv())

class YouTubeScraped:
    def __init__(self, url, soup):
        self.url = url
        self.soup = soup
        try:
            self.api_key = getenv('GOOGLE_APPLICATION_CREDENTIALS')
        except:
            raise Exception('GOOGLE_APPLICATION_CREDENTIALS not found! Please add a valid API key in the .env file')
        self.api_client = googleapiclient.discovery.build(
            'youtube', 'v3', developerKey=self.api_key, cache_discovery=False
        )
        self.request_parts = ['snippet', 'statistics']
        self.api_data = self.get_yt_api_response()
    
    def get_youtube_id(self):
        parsed = parse.parse_qs(parse.urlsplit(self.url).query)
        return parsed['v'][0]

    def get_yt_api_response(self):
        id = self.get_youtube_id()
        request = self.api_client.videos().list(part=self.request_parts, id=id)
        response = request.execute()
        return response['items'][0]

    def get_extra_attrs(self) -> dict:
        return {
            'youtube': {
                'title': self.api_data['snippet']['title'],
                'views': self.api_data['statistics']['viewCount'],
                'posted_date': isoparser(self.api_data['snippet']['publishedAt'])
            }
        }

    def scrape_yt(self) -> Tuple[BaseProviderInput, dict]:
        """Scraper function for YouTube videos"""
        
        # Check if video page has a "Music in this video" section
        # This section is not provided by the YouTube API directly and needs to be scraped
        if len(self.soup.find_all("li", class_="watch-meta-item yt-uix-expander-body")) > 1:
            output, extras = self.scrape_embedded_yt_metadata()
            if output.song_name is not None and output.artist_name is not None:
                return output, extras

        raw_title = self.api_data['snippet']['title']

        artist, title = get_artist_title(raw_title) or (None, None)
        # If artist/title is found to be None, use video title as title and channel name as artist
        if artist is None or title is None:
            title = raw_title
            try:
                artist = self.api_data['snippet']['channelTitle']  # Scrapes "Artist" from the YouTube Channel name
                artist = clean_channel(artist)
            except AttributeError:
                artist = None

        extra = self.get_extra_attrs()

        return DictInput(title, artist), extra

    def scrape_embedded_yt_metadata(self) -> Tuple[BaseProviderInput, dict]:
        """Scrapper function for videos with "Music in this video" section"""
        tags = self.soup.find_all("li", class_="watch-meta-item yt-uix-expander-body")

        info = {}
        for tag in tags:
            key = tag.find("h4").text.strip()
            value = tag.find("ul").text.strip()
            info[key] = value

        extras = self.get_extra_attrs()
        return (
            DictInput(
                song_name=check_key_get_value(info, "Song"),
                artist_name=check_key_get_value(info, "Artist"),
            ),
            extras,
        )