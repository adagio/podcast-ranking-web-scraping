from dataclasses import dataclass

@dataclass
class DataClassPodcast:
    __slots__ = ['title', 'desc', 'episodes', 'stair','url']
    title: str
    desc: str
    episodes: str
    stair: str
    url: str
    def __str__(self):
        return f'[{self.stair}] [{self.episodes}] {self.title}'