import cv2, os
import numpy as np
from tensorflow import keras
from .utils import get_traffic_sign_name

script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'resources', 'traffic_sign_recognition_model.h5')

_model = keras.models.load_model(model_path)

def predict_sign(image: np.array) -> str:
    
    image = cv2.resize(image, (32, 32))
    image = np.expand_dims(image, axis=0) 

    predicted_class = np.argmax(_model.predict(image))

    prediction = get_traffic_sign_name(predicted_class)

    print('Prediction:', prediction)

    return prediction
