from bs4 import BeautifulSoup
import enum
from dataclasses import dataclass
from ruamel.yaml import YAML


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


def load_formulas():
    stream = open("./sandbox/content/formulas.yaml", 'r')
    yaml = YAML()
    yaml_formulas = yaml.load(stream)
    return yaml_formulas

#TODO use the enum, not the literal
def get_value(tag, content_mode):
    if (content_mode == "content_attribute"):
        return tag.attrs['content']
    elif (content_mode == "text"):
        return tag.getText().strip()
    else:
        return None


yaml_formulas = load_formulas()


def get_values(html_block):

    values = {}

    for i, (key, ordered_formula) in enumerate(yaml_formulas.items()):
        formula = dict(ordered_formula)
        html_tag = get_html_tag(html_block, formula['html_pattern'])
        value = get_value(html_tag, formula['content_mode'])
        values[key] = value

    #for formula in formulas:
    #    html_tag = get_html_tag(html_block, formula['html_pattern'])
    #    value = get_value(html_tag, formula['content_mode'])
    #    values[formula['key']] = value

    return values


def build_podcast_object(program):
    values = get_values(program)
    podcast = DataClassPodcast(**values)
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

