from modules.ranker import Ranker

#TODO other categories
ranker = Ranker(
    category_name='internet-tecnologia',
    category_id='445',
    max_pages=3
)
podcasts = ranker.get_podcasts()

for podcast in podcasts:
    print(podcast) # is using DataClassPodcast __str__ representation
