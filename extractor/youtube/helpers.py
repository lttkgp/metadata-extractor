from extractor.youtube.validator import is_short_link

# Get long youtube link from shortened link
def get_yt_link(link):
    if is_short_link(link) :
        return "https://www.youtube.com/watch?v={}".format(get_yt_code(link))
    return link

def get_yt_code(link):
    return link[-11:]

def clean_channel(raw_channel):
    clean_channel = raw_channel
    dirt = ["-","topic", 'Topic']
    for substr in dirt:
        clean_channel = clean_channel.replace(substr, "")
    return clean_channel.strip()
\
# To escape KeyError
def check_key_get_value(data, key):
    if(key in data.keys()):
        return data[key]
    return None