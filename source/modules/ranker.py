import logging
from concurrent.futures import ProcessPoolExecutor, as_completed

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


    def get_podcasts_by_page(self, page_index):
        url_path = self.get_url_path(
            self.category_name,
            self.category_id,
            page_index
        )

        logger = logging.getLogger('infoLogger')
        log_msg = url_path
        logger.info(log_msg)
        
        url = self.base_path + url_path
        soup = get_soup(get_url_content(url))
        podcasts = scrap_podcasts(
            resource = soup,
            category_id = self.category_id,
            page_index = page_index
        )
        return podcasts
    

    def get_podcasts(self):       

        with ProcessPoolExecutor(max_workers=3) as executor:
            podcasts = []
            futures = [ executor.submit(self.get_podcasts_by_page, page) for page in
                       range(1, self.max_pages + 1) ]
            for completed_futures in as_completed(futures):
                podcasts.extend(completed_futures.result())
            return podcasts