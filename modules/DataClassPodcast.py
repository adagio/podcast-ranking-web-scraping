from dataclasses import dataclass

@dataclass(frozen=True)
class DataClassPodcast:
    __slots__ = ['title', 'desc', 'episode', 'url']
    title: str
    desc: str
    episode: str
    url: str
    def __str__(self):
        return f'{self.title}'