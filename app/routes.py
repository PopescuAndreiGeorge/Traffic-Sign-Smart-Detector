from flask import render_template, request, jsonify 
from flask_cors import CORS
from app import app
from http import HTTPStatus
from PIL import Image, UnidentifiedImageError
import numpy as np
from datetime import datetime
import socket
import cv2
from .tools.sign_recognition import predict_sign

CORS(app) 

@app.route('/api/ip', methods=['GET'])
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify({'ip': ip_address}), HTTPStatus.OK

@app.route('/')
def index():
    """ Main route to display the main page.
    """
    return render_template('main.html')

@app.route('/camera')
def camera():
    """ Camera route to display the camera page.
    """	
    print('here camera')
    return render_template('camera.html')

@app.route('/sign', methods=['POST'])
def sign():
    """ Get a sign image and identify the sign. After identifying the sign, return the sign information.
    """

    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'}), HTTPStatus.BAD_REQUEST

    try:
        # image = np.array(Image.open(request.files['image']))

        # image = cv2.imread(request.files['image'])

        image = cv2.imdecode(np.frombuffer(request.files['image'].read(), np.uint8), cv2.IMREAD_COLOR)

        #   • inputs=tf.Tensor(shape=(1, 32, 32, 4), dtype=uint8)

        prediction = predict_sign(image)

        stub_sign_info = {
            'name' : prediction,
            'meaning' : 'And image with shape: ' + str(image.shape),
            'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

        return jsonify(stub_sign_info), HTTPStatus.OK

    except UnidentifiedImageError as e:
        return jsonify({'error': 'Image processing error: ' + str(e)}), HTTPStatus.BAD_REQUEST

    
if __name__ == '__main__':
    app.run(debug=True)
