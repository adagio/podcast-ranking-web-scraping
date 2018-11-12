from pprint import pprint

from modules.utils import *
from modules.scraping import *


filepaths = [
    'sandbox/content/podcast_internet_tecnologia_1.html',
    'sandbox/content/podcast_internet_tecnologia_2.html'
]

urls = [
    'https://www.ivoox.com/podcast-internet-tecnologia_sc_f445_1.html',
    'https://www.ivoox.com/podcast-internet-tecnologia_sc_f445_2.html'
]


podcasts = []

"""for filepath in filepaths:
    soup = getSoup(read_file(filepath))
    get_podcasts(soup, podcasts)"""

for url in urls:
    soup = getSoup(get_url_content(url))
    get_podcasts(soup, podcasts)

pprint(podcasts)
