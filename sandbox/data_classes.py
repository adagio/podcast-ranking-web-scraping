from dataclasses import dataclass

@dataclass
class DataClassPodcast:
    title: str
    desc: str
    episode: str
    url: str

#podcast = DataClassPodcast('tt', 'dd', 777, 'uu')
podcast = DataClassPodcast()

podcast.title = 'hola'

print(podcast)