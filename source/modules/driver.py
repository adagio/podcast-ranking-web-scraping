import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed

from modules.ranker import Ranker


class Driver:

    def __init__(self, filename):
        df = pd.read_csv(filename)
        self.categories = df.to_dict('records')

    def print_categories(self):
        for category in self.categories:
            print(category)

    def get_podcasts_by_category(self, category):
        category_id = category['id']
        category_name = category['slug']
        #TODO just print in dev .env
        print(f'{category_id} {category_name}')
        category_podcasts = []
        ranker = Ranker(
            category_name=category_name,
            category_id=category_id,
            max_pages=3
        )
        category_podcasts = ranker.get_podcasts()
        return category_podcasts

    def drive_sync(self):
        podcasts = []
        for category in self.categories:
            category_podcasts = self.get_podcasts_by_category(category)
            podcasts.extend(category_podcasts)
        return podcasts
    
    # TODO show progress in prod .env
    def drive_async(self):
        podcasts = []
        with ProcessPoolExecutor(max_workers=4) as executor:
            category_podcasts = []
            futures = [ executor.submit(self.get_podcasts_by_category, category) for category in self.categories ]
            for completed_futures in as_completed(futures):
                category_podcasts.extend(completed_futures.result())
            podcasts.extend(category_podcasts)
        return podcasts