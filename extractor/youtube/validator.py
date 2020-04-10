import re

def validate_yt(link): 
    if(bool(re.match("https://\w{0,3}.?youtube+\.\w{2,3}/watch\?v=[\w-]{11}", link) or bool(re.match("https://youtu.be/[\w-]{11}", link))):
            return True
    return False

