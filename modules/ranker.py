from modules.utils import *
from modules.scraping import *

class Ranker:

    def __init__(self, realpart, imagpart):

        self.path = 'sandbox/content/'

        self.filenames = [
            'podcast_internet_tecnologia_1.html',
            'podcast_internet_tecnologia_2.html'
        ]

        protocol = 'https'
        domain = 'www.ivoox.com'
        self.base_path = protocol + '://' +  domain + '/'

        self.url_paths = [
            'podcast-internet-tecnologia_sc_f445_1.html',
            'podcast-internet-tecnologia_sc_f445_2.html'
        ]

        self.podcasts = []

        self.r = realpart
        self.i = imagpart

    def get_podcasts(self):
        for filename in self.filenames:
            filepath = self.path + filename
            soup = get_soup(read_file(filepath))
            these_podcasts = get_podcasts(soup)
            self.podcasts.extend(these_podcasts)

        """ for url_path in url_paths:
            url = base_path + url_path
            soup = get_soup(get_url_content(url))
            these_podcasts = get_podcasts(soup)
            podcasts.extend(these_podcasts) """

        return self.podcasts
