from flask import url_for
import re

def get_image_path(image_name: str) -> str:
    """ With a image name, return the path to the image in the assets folder
    """
    return f'assets/signs/{image_name[:-4]}.png'


def sparql_name_to_label(name: str) -> str:
    """ Parse the name to get the sign name: EndSpeedLimit50 -> End Speed Limit 50
    """
    # result = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)[:-4]

    idx = 0
    result = ''

    while idx < len(name):
        if (name[idx].isupper() and idx != 0) or (name[idx - 1].isalpha() and name[idx].isdigit()):
            result += ' '
        result += name[idx]
        idx += 1 

    return result[:-5]


def url_name_to_label(name: str) -> str:
    """ Parse the name to get the sign name in the url: end_speed_limit50 -> End Speed Limit 50
    """
    
    idx = 0
    result = ''

    name = ' '.join(word.capitalize() for word in name.split('_'))

    while idx < len(name):
        if name[idx - 1].isalpha() and name[idx].isdigit():
            result += ' ' + name[idx]
        else:
            result += name[idx]
       
        idx += 1 

    return result


def sparql_name_to_link(name: str) -> str:
    """ Parse the name to get the sign name in the ontology: NoOvertakingSign -> no_overtaking
    """
    result = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)[:-4].lower().replace(' ', '_')
    result = result[:-1] if result[-1] == '_' else result

    return result


def link_name_to_sparql(name: str) -> str:
    """ Parse the name to get the sign name in the ontology: no_overtaking -> NoOvertakingSign
    """
    result = ''.join(word.capitalize() for word in name.split('_'))
    result += 'Sign'

    return result

def get_signs_list(signs: list) -> list:
    """ Parse the list of sign names from ontology to a list of dictionaries with the sign name, about url and image url
    """

    signs_list = []

    for sign in signs:
        signs_list.append ( { 
            'name': sparql_name_to_label(sign), 
            'about_url': url_for('about', sign = sparql_name_to_link(sign)), 
            'image_url': url_for('static', filename = get_image_path(sign))
        } )

    return signs_list
