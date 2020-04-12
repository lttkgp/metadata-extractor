import re

def yt_validate(yt_link) :
        if(bool(re.match("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?",yt_link))):
                return True
        return False

def is_short_link(yt_link):
        if(bool(re.match("^https://youtu.be/", yt_link))):
                return True
        return False


