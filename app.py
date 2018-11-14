from pprint import pprint

from modules.utils import *
from modules.scraping import *

path = 'sandbox/content/'

filenames = [
    'podcast_internet_tecnologia_1.html',
    'podcast_internet_tecnologia_2.html'
]

protocol = 'https'
domain = 'www.ivoox.com'
base_path = protocol + '://' +  domain + '/'

url_paths = [
    'podcast-internet-tecnologia_sc_f445_1.html',
    'podcast-internet-tecnologia_sc_f445_2.html'
]


podcasts = []

"""for filename in filenames:
    filepath = path + filename
    soup = getSoup(read_file(filepath))
    get_podcasts(soup, podcasts)"""

for url_path in url_paths:
    url = base_path + url_path
    soup = getSoup(get_url_content(url))
    get_podcasts(soup, podcasts)

pprint(podcasts)
