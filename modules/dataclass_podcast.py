from dataclasses import dataclass

@dataclass
class DataClassPodcast:
    __slots__ = ['title', 'episodes', 'stair', 'url']
    title: str
    episodes: int
    stair: int
    url: str
    def __str__(self):
        return f'[{self.stair}] [{self.episodes}] {self.title}'