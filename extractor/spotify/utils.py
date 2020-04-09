import urllib.parse as url_parser

def build_query(title, artist):
   return url_parser.quote(f'{title} artist:{artist}')
