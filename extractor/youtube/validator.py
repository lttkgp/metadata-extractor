import re

def yt_validate(yt_link) :
        if(bool(re.match("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?", yt_link))):
                return True
        return False

def available_video(soup):
        if(soup.find('meta', {'property': 'og:title'})):
                return True
        return False