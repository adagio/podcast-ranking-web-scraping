from dataclasses import dataclass
from dataclasses_json import dataclass_json
import json

value = {
    'title': 'tu',
    'desc': 'yes'
}
value_json = json.dumps(value)

@dataclass_json
@dataclass(frozen=True)
class DataClassPodcast:
    title: str
    desc: str
    episode: str
    url: str
    
"""     def __init__(self, value):
        self.title = value['title']
        self.desc = value['desc']
        self.episode = '777'
        self.url = 'uu' """

#podcast = DataClassPodcast('tt', 'dd', 777, 'uu')
podcast = DataClassPodcast.from_json(value_json)

print(podcast)