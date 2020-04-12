import re

def yt_validate(yt_link) :
        if(bool(re.match("^https://\w{0,3}.?youtube+\.\w{2,3}/watch\?v=[\w-]{11}$", yt_link)) or bool(re.match("^https://youtu.be/", yt_link))):
                return True
        return False

def is_short_link(yt_link):
        if(bool(re.match("^https://youtu.be/", yt_link))):
                return True
        return False