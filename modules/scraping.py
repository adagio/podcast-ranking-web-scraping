from bs4 import BeautifulSoup
from modules.formulas import *
from modules.dataclass_podcast import DataClassPodcast


def get_soup(text):
    soup = BeautifulSoup(text, features="lxml")
    return soup


def get_html_tag(html_block, pattern):
    return html_block.select(pattern)[0]


def get_value(tag, content_mode):
    if ( content_mode == ContentMode.content_attribute ):
        return tag.attrs['content']
    elif ( content_mode == ContentMode.text ):
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

