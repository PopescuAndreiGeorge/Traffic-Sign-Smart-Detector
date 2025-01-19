import cv2, os
import numpy as np
from tensorflow import keras
from .utils import get_traffic_sign_name

_model = keras.models.load_model(os.getenv('TSR_MODEL'))

def predict_sign(image: np.array) -> str:
    
    image = cv2.resize(image, (32, 32))
    image = np.expand_dims(image, axis=0) 

    predicted_class = np.argmax(_model.predict(image))
    prediction = get_traffic_sign_name(predicted_class)

    return prediction
