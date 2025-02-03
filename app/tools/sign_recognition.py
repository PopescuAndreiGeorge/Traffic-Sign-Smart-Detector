import cv2, os
import numpy as np
from tensorflow import keras

_model = keras.models.load_model(os.getenv('TSR_MODEL'))

_traffic_signs = {
    0:  'speed_limit20',
    1:  'speed_limit30',
    2:  'speed_limit50',
    3:  'speed_limit60',
    4:  'speed_limit70',
    5:  'speed_limit80',
    6:  'end_speed_limit80',
    7:  'speed_Limit100',
    8:  'speed_limit120',
    9:  'no_overtaking',
    10: 'no_overtaking_by_heavy_goods_vehicles',
    11: 'crossroads_with_minor_road',
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

def predict_sign(image: np.array) -> str:
    
    image = cv2.resize(image, (32, 32))
    image = np.expand_dims(image, axis=0) 

    predicted_class = np.argmax(_model.predict(image))
    return _traffic_signs.get(predicted_class, 'Unknown')
