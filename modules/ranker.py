from modules.utils import *
from modules.scraping import *


class Ranker:


    def __init__(self, category_name, category_id, max_pages):

        self.category_name = category_name
        self.category_id = category_id
        self.max_pages = max_pages

        protocol = 'https'
        domain = 'www.ivoox.com'
        self.base_path = protocol + '://' +  domain

        self.url_path_mask = "/podcast-{0}_sc_f{1}_{2}.html"


    def get_url_path(self, category_name, category_id, page):
        
        url_path = self.url_path_mask.format(
            category_name,
            category_id,
            page
        )
        return url_path


    def get_podcasts(self):

        podcasts = []

        for page_index in range(1, self.max_pages + 1):
            url_path = self.get_url_path(
                self.category_name,
                self.category_id,
                page_index
            )
            url = self.base_path + url_path
            soup = get_soup(get_url_content(url))
            these_podcasts = get_podcasts(soup)
            podcasts.extend(these_podcasts)

        return podcasts

