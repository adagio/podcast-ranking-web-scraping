from modules.ranker import Ranker
from modules.storage import Storage

category_name = 'internet-tecnologia'
category_id = '445'

ranker = Ranker(
    category_name=category_name,
    category_id=category_id,
    max_pages=3
)
podcasts = ranker.get_podcasts()

Storage.save_csv(f'storage/ranking-{category_id}', podcasts)

#stored_podcasts = Storage.load(f'storage/ranking-{category_id}.pkl')

#for podcast in stored_podcasts:
#    print(podcast)
