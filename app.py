from modules.ranker import Ranker
from modules.storage import Storage

#TODO other categories
#ranker = Ranker(
#    category_name='internet-tecnologia',
#    category_id='445',
#    max_pages=3
#)
#podcasts = ranker.get_podcasts()

#Storage.save('storage/ranking.pkl', podcasts)
stored_podcasts = Storage.load('storage/ranking.pkl')

for podcast in stored_podcasts:
    print(podcast)
