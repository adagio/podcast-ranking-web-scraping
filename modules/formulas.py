from ruamel.yaml import YAML
from modules.structs import ContentMode


def update_enums(yaml_formulas):

    for i, (key, ordered_formula) in enumerate(yaml_formulas.items()):
        if ( yaml_formulas[key]['content_mode'] == 'content_attribute' ):
            yaml_formulas[key]['content_mode'] = ContentMode.content_attribute
        elif ( yaml_formulas[key]['content_mode'] == "text" ):
            yaml_formulas[key]['content_mode'] = ContentMode.text
    
    return yaml_formulas


def load_formulas():
    stream = open("./sandbox/content/formulas.yaml", 'r')
    yaml = YAML()
    yaml_formulas = yaml.load(stream)

    yaml_formulas = update_enums(yaml_formulas)

    return yaml_formulas
