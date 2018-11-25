import pandas as pd

from modules.storage import Storage
from modules.driver import Driver

def retrieve():

    driver = Driver('storage/subcategories.csv')

    #podcasts = driver.drive_sync()
    podcasts = driver.drive_async()

    df = pd.DataFrame(podcasts)
    Storage.save_csv(f'storage/ranking.csv', dataframe = df)

    #stored_podcasts = Storage.load(f'storage/ranking-{category_id}.pkl')

    #for podcast in stored_podcasts:
    #    print(podcast)
