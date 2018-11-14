from bs4 import BeautifulSoup
import enum
from dataclasses import dataclass
import json
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class DataClassPodcast:
    __slots__ = ['title', 'desc', 'episode', 'url']
    title: str
    desc: str
    episode: str
    url: str
    def __str__(self):
        return f'{self.title}'


class ContentMode(enum.Enum):
    content_attribute = 0
    text = 1


def get_soup(text):
    soup = BeautifulSoup(text, features="lxml")
    return soup


def get_html_tag(html_block, pattern):
    return html_block.select(pattern)[0]


formulas = [
    {
        'key': 'title',
        'html_pattern': 'meta[itemprop="name"]',
        'content_mode': ContentMode.content_attribute
    },
    {
        'key': 'desc',
        'html_pattern': 'meta[itemprop="description"]',
        'content_mode': ContentMode.content_attribute
    },
    {
        'key': 'url',
        'html_pattern': 'meta[itemprop="url"]',
        'content_mode': ContentMode.content_attribute
    },
    {
        'key': 'episode',
        'html_pattern': '.microphone',
        'content_mode': ContentMode.text
    },
]


def get_value(tag, content_mode):
    if (content_mode == ContentMode.content_attribute):
        return tag.attrs['content']
    elif (content_mode == ContentMode.text):
        return tag.getText().strip()
    else:
        return None


def get_values(html_block):

    values = {}

    for formula in formulas:
        html_tag = get_html_tag(html_block, formula['html_pattern'])
        value = get_value(html_tag, formula['content_mode'])
        values[formula['key']] = value

    return values


def build_podcast_object(program):
    values = get_values(program)
    values_in_json = json.dumps(values)
    podcast = DataClassPodcast.from_json(values_in_json)
    return podcast


def get_podcasts(resource: BeautifulSoup):
    """
        Extrae el listado de podcasts 
        Devuelve una lista con el diccionario de elementos encontrados
    """
    podcasts = []
    for podcast_html_block in resource.findAll("div", {"class": ["modulo-type-programa"]}):
        try:
            podcast = build_podcast_object(podcast_html_block)
            podcasts.append(podcast)
        except IndexError:
            print("No se puede capturar el contenido") 

    return podcasts

