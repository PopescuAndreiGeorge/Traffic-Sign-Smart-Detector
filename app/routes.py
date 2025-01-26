from flask import render_template, request, jsonify, url_for
from flask_cors import CORS
from app import app
from http import HTTPStatus
from PIL import Image, UnidentifiedImageError
import numpy as np
from datetime import datetime
import socket
import cv2
from .tools.sign_recognition import predict_sign
from .tools.utils import get_image_path, parse_Sparql_name
from .sparql_queries import *

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        'error_page.html',
        title = 'Error 404 - Page Not Found',
        info = 'Sorry, the page you are looking for does not exist.'
    ), HTTPStatus.NOT_FOUND


@app.route('/camera')
def camera():
    """ Camera route to display the camera page.
    """	
    return render_template('camera.html')


@app.route('/sign', methods=['POST'])
def sign():
    """ Get a sign image and identify the sign. After identifying the sign, return the sign information.
    """

    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'}), HTTPStatus.BAD_REQUEST

    try:
        image = cv2.imdecode(np.frombuffer(request.files['image'].read(), np.uint8), cv2.IMREAD_COLOR)
        prediction = predict_sign(image)

        # no_passing -> NoPassing

        # Get from an ontology the meaning of the sign.

        return_json = {
            'name' : prediction,
            'meaning' : 'And image with shape: ' + str(image.shape),
            'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'url': 'https://localhost:5050/traffic_sign/no_passing'
        }

        return jsonify(return_json), HTTPStatus.OK

    except UnidentifiedImageError as e:
        return jsonify({'error': 'Image processing error: ' + str(e)}), HTTPStatus.BAD_REQUEST


@app.route('/traffic_sign/api_test', methods=['GET'])
def traffic_sign():
    results = test_query()
    return results


@app.route('/about', methods=['GET'])
def about():
    sign_name = request.args.get('sign')

    if sign_name is None:
       return render_template (
           'error_page.html', 
           title = 'Error - Missing Sign Argument',
           info = 'Sorry, the required sign argument is missing for the /about page.'
        ), HTTPStatus.BAD_REQUEST

    sign_name = sign_name[0].upper() + sign_name[1:]

    # Stupid example

    sign_meaning = 'A stop sign is a regulatory sign that indicates that a driver must stop before proceeding. It is usually found at intersections, where drivers are required to stop and yield the right-of-way to other vehicles and pedestrians.'
    sign_type = 'Regulatory'
    precede_signs = []
    precede_by = []

    signs = ["PaharSign", "FootpathSign", "OtherDangerSign", "PedestrianCrossingSign", "PriorityRoadSign", "RoundaboutSign", "StopSign", "TrafficSignalsSign", "YieldSign"]

    for sign in signs:
        precede_signs.append({'name': parse_Sparql_name(sign), 'image_url': url_for('static', filename = get_image_path(sign))})

    sign_image = url_for('static', filename = get_image_path(sign_name + 'Sign'))


    return render_template (
        template_name_or_list = 'about_sign.html', 
        sign_name = sign_name,
        sign_meaning = sign_meaning,
        sign_type = sign_type,
        sign_image = sign_image,
        precede_signs = precede_signs,
        precede_by = precede_by,
    )
    
    
if __name__ == '__main__':
    app.run(debug=True)
