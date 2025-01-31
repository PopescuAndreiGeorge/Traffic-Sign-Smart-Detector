from flask import url_for
import re

_traffic_signs = {
    0:  'speed_limit20',
    1:  'speed_limit30',
    2:  'speed_limit50',
    3:  'speed_limit60',
    4:  'speed_limit70',
    5:  'speed_limit80',
    6:  'end_of_speed_limit80',
    7:  'speed_Limit100',
    8:  'speed_limit120',
    9:  'no_overtaking',
    10: 'no_overtaking_by_heavy_goods_vehicles',
    11: 'crossroads_with_a_minor_road',
    12: 'priority_road',
    13: 'yield',
    14: 'stop',
    15: 'no_vehicles',
    16: 'no_heavy_goods_vehicles',
    17: 'no_entry',
    18: 'other_danger',
    19: 'curve',
    20: 'curve',
    21: 'series_of_curves',
    22: 'uneven_surface',
    23: 'slippery_surface',
    24: 'road_narrows',
    25: 'roadworks',
    26: 'traffic_signals',
    27: 'pedestrians', # -----
    28: 'children',
    29: 'cyclists',
    30: 'ice_or_snow',
    31: 'wild_animals',
    32: 'end_all_previously_signed_restrictions',
    33: 'keep_right_ahead',
    34: 'keep_left_ahead',
    35: 'go_straight',
    36: 'go_straight_or_turn_right',
    37: 'go_straight_or_turn_Left', # -----
    38: 'keep_right',
    39: 'keep_left',
    40: 'roundabout',
    41: 'end_no_overtaking',
    42: 'end_no_overtaking_by_heavy_goods_vehicles'
}

def get_traffic_sign_name(predicted_class: int) -> str:
    if predicted_class not in _traffic_signs:
        return 'Unknown'
    
    return _traffic_signs[predicted_class]


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
    print(name)
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
