import re

_traffic_signs = {
    0:  'speed_limit_20',
    1:  'speed_limit_30',
    2:  'speed_limit_50',
    3:  'speed_limit_60',
    4:  'speed_limit_70',
    5:  'speed_limit_80',
    6:  'end_of_speed_limit_80',
    7:  'speed_Limit_100',
    8:  'speed_limit_120',
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
    32: 'end_of_all_previously_signed_restrictions',
    33: 'keep_right_ahead',
    34: 'keep_left_ahead',
    35: 'go_straight',
    36: 'go_straight_or_turn_right',
    37: 'go_straight_or_turn_Left', # -----
    38: 'keep_right',
    39: 'keep_left',
    40: 'roundabout',
    41: 'end_of_no_overtaking',
    42: 'end_of_no_overtaking_by_heavy_goods_vehicles'
}

def get_traffic_sign_name(predicted_class: int) -> str:
    if predicted_class not in _traffic_signs:
        return 'Unknown'
    
    return _traffic_signs[predicted_class]


def get_image_path(image_name: str) -> str:
    """ With a image name, return the path to the image in the assets folder
    """
    return f'assets/signs/{image_name[:-4]}.png'


def parse_Sparql_name(name: str) -> str:
    """ Parse the name to get the sign name: NoOvertakingSign -> No Overtaking
    """
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)[:-4]


def parse_Sparql_name_to_link(name: str) -> str:
    """ Parse the name to get the sign name in the ontology: NoOvertakingSign -> no_overtaking
    """
    result = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)[:-4].lower().replace(' ', '_')
    return result[:-1]