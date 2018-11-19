from modules.ranker import Ranker

ranker = Ranker(1, 2)
podcasts = ranker.get_podcasts()

for podcast in podcasts:
    print(podcast) # is using DataClassPodcast __str__ representation
