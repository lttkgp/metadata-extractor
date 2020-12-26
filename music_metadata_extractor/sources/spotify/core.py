from music_metadata_extractor.models import ProviderInput, BaseProviderInput
from typing import Tuple
from music_metadata_extractor.utils import get_spotify_client
import googleapiclient.discovery
from dateutil.parser import isoparse as isoparser
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def search_yt_title_artist(track_name: str, artist_name: str) -> dict:
    search_query = track_name + " " + artist_name
    
    api_key = getenv("GOOGLE_APPLICATION_CREDENTIALS")
    api_client = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key, cache_discovery=False)
    
    request = api_client.search().list(part=["id"], q=search_query)
    response = request.execute()
    # first 5 items
    items = response['items']
    for item in items:
        kind_id = item['id']['kind']
        if kind_id == 'youtube#video':
            video_id = item['id']['videoId']
            video_request = api_client.videos().list(part=["snippet", "statistics"], id=video_id)
            video_response = video_request.execute()
            video = video_response['items'][0]
            return {
                "youtube": {
                    "title": video["snippet"]["title"],
                    "views": video["statistics"]["viewCount"],
                    "posted_date": isoparser(video["snippet"]["publishedAt"]),
                    "converted_url": f"https://www.youtube.com/watch?v={video_id}"
                }
            }

def get_extra_attrs(input_url: str) -> dict:
    spotify_client = get_spotify_client()
    track_data = spotify_client.track(input_url)
    
    track_name = track_data["name"]
    track_artists = " ".join([artist["name"] for artist in track_data["artists"]])
    
    return search_yt_title_artist(track_name, track_artists)

def get_info(input_url: str) -> Tuple[BaseProviderInput, dict]:
    extra = get_extra_attrs(input_url)
    return ProviderInput(provider_url=input_url), extra