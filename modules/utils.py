import requests


def read_file(filepath):
    """
        Extrae el contenido de ficheros locales y comprueba si existen
    """
    try:
        file = open(filepath)
    except FileNotFoundError:
        print("El fichero no existe") 
    
    text = file.read()

    return text


def get_url_content(url):
    """
        Extrae el contenido de unas URL específicas
    """
    res = requests.get(url)
    # Levanta el error solo si algo fue mal (errores 400)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Problem! %s' % (exc))
    
    text = res.text

    return text
