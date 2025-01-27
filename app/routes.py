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
from .tools.utils import get_image_path, parse_Sparql_name, parse_Sparql_name_to_link
from .sparql_queries import *

CORS(app)  # Enable CORS for all routes


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
        sign_name = ' '.join(word.capitalize() for word in prediction.split('_'))
        
        # Parse the name to get the sign name in the ontology: no_overtaking -> NoOvertakingSign
        sign_name_in_ontology = ''.join(word.capitalize() for word in prediction.split('_'))
        sign_name_in_ontology += 'Sign'

        # TODO: call the sparql query to get the sign information....

        return_json = {
            'name' : sign_name,
            'category' : 'Traffic Control',
            'type' : 'Regulatory',
            'meaning' : 'A stop sign is a regulatory sign that indicates that a driver must stop before proceeding. It is usually found at intersections, where drivers are required to stop and yield the right-of-way to other vehicles and pedestrians.',
            'rules' : 'A stop sign is a regulatory sign that indicates that a driver must stop before proceeding. It is usually found at intersections, where drivers are required to stop and yield the right-of-way to other vehicles and pedestrians.',
            'url': 'https://localhost:5050/about?sign=' + prediction
        }

        return jsonify(return_json), HTTPStatus.OK

    except UnidentifiedImageError as e:
        return jsonify({'error': 'Image processing error: ' + str(e)}), HTTPStatus.BAD_REQUEST


@app.route('/about', methods=['GET'])
def about():
    sign_name = request.args.get('sign')

    # If the sign argument is missing or invalid, return an error page.
    if sign_name is None or sign_name == '':
       return render_template (
           'error_page.html', 
           title = 'Error - Missing or invalid Sign Argument',
           info = 'Sorry, the required sign argument is missing for the /about page.'
        ), HTTPStatus.BAD_REQUEST
    

    # Parse the sign name: no_overtaking -> NoOvertaking
    sign_name_text = ' '.join(word.capitalize() for word in sign_name.split('_'))

    # Parse the name to get the sign name in the ontology: no_overtaking -> NoOvertakingSign
    sign_name_in_ontology = ''.join(word.capitalize() for word in sign_name.split('_'))
    sign_name_in_ontology += 'Sign'

    # TODO: Get the sign information from the ontology....

    sign_type = 'Regulatory'
    sign_category = 'Traffic Control'
    sign_rules = 'A stop sign is a regulatory sign that indicates that a driver must stop before proceeding. It is usually found at intersections, where drivers are required to stop and yield the right-of-way to other vehicles and pedestrians.'
    sign_meaning = 'A stop sign is a regulatory sign that indicates that a driver must stop before proceeding. It is usually found at intersections, where drivers are required to stop and yield the right-of-way to other vehicles and pedestrians.'
    sign_image = url_for('static', filename = get_image_path(sign_name_in_ontology))
    precede_signs = []
    precede_by = []

    signs = ["PaharSign", "FootpathSign", "OtherDangerSign", "PedestrianCrossingSign", "PriorityRoadSign", "RoundaboutSign", "StopSign", "TrafficSignalsSign", "YieldSign"]

    for sign in signs:
        precede_signs.append ( { 
            'name': parse_Sparql_name(sign), 
            'about_url': url_for('about', sign = parse_Sparql_name_to_link(sign)), 
            'image_url': url_for('static', filename = get_image_path(sign))
        } )

    return render_template (
        template_name_or_list = 'about_sign.html', 
        sign_name = sign_name_text,
        sign_meaning = sign_meaning,
        sign_rules = sign_rules,
        sign_category = sign_category,
        sign_type = sign_type,
        sign_image = sign_image,
        precede_signs = precede_signs,
        precede_by = precede_by,
    )
    
    
if __name__ == '__main__':
    app.run(debug=True)
