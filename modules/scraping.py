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
        text_value = tag.getText().strip()
        if text_value != '':
            return int(tag.getText().strip())
        else:
            return None
    else:
        return None


yaml_formulas = load_formulas()


def get_values(html_block):

    values = {}

    for i, (key, ordered_formula) in enumerate(yaml_formulas.items()):
        formula = dict(ordered_formula)
        if formula['enabled']:
            html_tag = get_html_tag(html_block, formula['html_pattern'])
            value = get_value(html_tag, formula['content_mode'])
            values[key] = value

    return values


def build_podcast_object(html_block):
    values = get_values(html_block)
    return values


def build_podcast_dataclass(program):
    values = get_values(program)
    podcast = DataClassPodcast(**values)
    return podcast


def scrap_podcasts(resource: BeautifulSoup, category_id, page_index):
    """
        Extrae el listado de podcasts 
        Devuelve una lista con el diccionario de elementos encontrados
    """
    podcasts = []
    for key,podcast_html_block in enumerate( resource.findAll("div", {"class": ["modulo-type-programa"]}) ):
        try:
            podcast = build_podcast_object(podcast_html_block)
            podcast['page_pos'] = key
            podcast['category_id'] = category_id
            podcast['page_ix'] = page_index
            podcasts.append(podcast)
        except IndexError:
            print("No se puede capturar el contenido") 

    return podcasts
