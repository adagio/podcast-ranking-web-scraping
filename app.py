from modules.ranker import Ranker
from modules.storage import Storage
import pandas as pd

category_name = 'internet-tecnologia'
category_id = '445'

ranker = Ranker(
    category_name=category_name,
    category_id=category_id,
    max_pages=3
)
podcasts = ranker.get_podcasts()

df = pd.DataFrame(podcasts)
Storage.save_csv(f'storage/ranking-{category_id}.csv', dataframe = df)

#stored_podcasts = Storage.load(f'storage/ranking-{category_id}.pkl')

#for podcast in stored_podcasts:
#    print(podcast)
