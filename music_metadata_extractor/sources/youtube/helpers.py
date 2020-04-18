def is_valid_url(soup):
    if soup.find("meta", {"property": "og:title"}):
        return True
    return False


def clean_channel(raw_channel):
    clean_channel = raw_channel
    dirt = ["-", "topic", "Topic"]
    for substr in dirt:
        clean_channel = clean_channel.replace(substr, "")
    return clean_channel.strip()


# To escape KeyError
def check_key_get_value(data, key):
    if key in data.keys():
        return data[key]
    return None