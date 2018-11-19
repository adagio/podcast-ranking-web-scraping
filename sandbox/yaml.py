from ruamel.yaml import YAML

stream = open("./content/formulas.yaml", 'r')

yaml = YAML()
yaml_formulas = yaml.load(stream)

yaml_formulas['title']['html_pattern'] = 'hey'

#formulas = []

""" for i, (key, value) in enumerate(yaml_formulas.items()):
    print(key)
    for j, (jkey, jvalue) in enumerate(value.items()):
        print(jvalue) """


for i, (key, value) in enumerate(yaml_formulas.items()):
    print(i, key)
    mydict = dict(value)
    print(mydict)

