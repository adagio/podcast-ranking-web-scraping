from bs4 import BeautifulSoup


def getSoup(text):
    soup = BeautifulSoup(text, features="lxml")
    return soup


def build_program_object(program):

    patterns = {
        'name': 'meta[itemprop="name"]',
        'desc': 'meta[itemprop="description"]',
        'url': 'meta[itemprop="url"]',
        'episode': '.microphone'
    }

    # TODO Refactor the block below

    program_object = {
        'title': ["%s" % name.attrs['content'] for name in program.select(patterns['name'])][0],
        'description': ["%s" % desc.attrs['content'] for desc in program.select(patterns['desc'])][0],
        'url': ["%s" % url.attrs['content'] for url in program.select(patterns['url'])][0],
        'episode': ["%s" % micro.getText().strip() for micro in program.select(patterns['episode'])][0]
    }

    return program_object


def get_podcasts(resource: BeautifulSoup, podcasts):
    """
        Extrae el listado de podcasts 
        Devuelve una lista con el diccionario de elementos encontrados
    """
    for program in resource.findAll("div", {"class": ["modulo-type-programa"]}):
        try:
            podcasts.append(
                build_program_object(program)    
            )
        except IndexError:
            print("No se puede capturar el contenido") 

    return podcasts

