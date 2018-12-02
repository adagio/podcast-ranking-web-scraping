import logging

import pandas as pd

from modules.storage import Storage
from modules.driver import Driver
from modules.setup import setup

def retrieve():

    driver = Driver('storage/subcategories.csv')

    setup()
    logger = logging.getLogger('infoLogger')

    #podcasts = driver.drive_sync()
    podcasts = driver.drive_async()

    df = pd.DataFrame(podcasts)
    Storage.save_csv('storage/programs.csv', dataframe = df)

    log_msg = f'Podcats: {len(podcasts)}'
    logger.info(log_msg)

    logger.info('Finalize app')

    #stored_podcasts = Storage.load(f'storage/ranking-{category_id}.pkl')

    #for podcast in stored_podcasts:
    #    print(podcast)
