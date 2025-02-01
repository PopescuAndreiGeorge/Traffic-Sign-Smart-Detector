from flask import render_template, request, jsonify, url_for
from flask_cors import CORS
from app import app
from http import HTTPStatus
from PIL import UnidentifiedImageError
import numpy as np
import cv2

from .tools.sign_recognition import predict_sign
from .tools.utils import *
from .tools.sparql_queries import *

CORS(app)  # Enable CORS for all routes


@app.route('/')
def index():
    """ Main page on which the user can upload an image to identify the traffic sign or access the camera page. 
    """
    return render_template('main_page.html'), HTTPStatus.OK


@app.errorhandler(404)
def page_not_found(e):
    """ Error handler for 404 - Page Not Found. 
    """
    return render_template(
        'error_page.html',
        title = 'Error 404 - Page Not Found',
        info = 'Sorry, the page you are looking for does not exist.'
    ), HTTPStatus.NOT_FOUND


@app.route('/live')
def camera():
    """ Camera page on which the user can use the camera to identify the traffic sign in real-time. 
        After identifying the sign, the user can access the sign about page.
    """	
    return render_template('camera_page.html'), HTTPStatus.OK


@app.route('/recognize', methods=['POST'])
def sign():
    """ /sign API route to predict the traffic sign from the image and return minimal information about the sign. 
    """

    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'}), HTTPStatus.BAD_REQUEST

    try:
        # Read the image from the request and predict the sign.
        image = cv2.imdecode(np.frombuffer(request.files['image'].read(), np.uint8), cv2.IMREAD_COLOR)
        prediction = predict_sign(image)

        # Get the sign information from the ontology.
        sign_name_in_ontology = link_name_to_sparql(prediction)

        response = {
            'name'             : url_name_to_label(prediction),
            'meaning'          : get_sign_meaning(sign_name_in_ontology),
            'legal_regulation' : get_sign_legal_regulation(sign_name_in_ontology),
            'redirect_url'     : '/about?sign=' + prediction
        }

        return jsonify(response), HTTPStatus.OK

    except UnidentifiedImageError as e:
        return jsonify({'error': 'Image processing error: ' + str(e)}), HTTPStatus.BAD_REQUEST

@app.route('/info', methods=['GET'])
def info():
    """ /info?sign=<sign> API route to get as json all the information about the sign like type, category, meaning, legal regulation, etc.
    """

    sign_name = request.args.get('sign')

    # If the sign argument is missing or invalid, return an error page.
    if sign_name is None or sign_name == '':
       return render_template (
           'error_page.html', 
           title = 'Error - Missing or invalid Sign Argument',
           info = 'Sorry, the required sign argument is missing for the /about page.'
        ), HTTPStatus.BAD_REQUEST
    
    # Parse the url type sign name to the ontology type and use it to get the sign information.
    sign_name_in_ontology = link_name_to_sparql(sign_name)
    sign_found , sign_ontology_infos = get_sign_ontology_infos(sign_name_in_ontology)

    if not sign_found:
        return jsonify({'error': 'Sign not found'}), HTTPStatus.NOT_FOUND
    
    response = {
        'name'                 : url_name_to_label(sign_name),
        'type'                 : sign_ontology_infos['label'],
        'category'             : sign_ontology_infos['category'],
        'meaning'              : sign_ontology_infos['meaning'],
        'legal_regulation'     : sign_ontology_infos['legal_regulation'],
        'color'                : sign_ontology_infos['color'],
        'shape'                : sign_ontology_infos['shape'],
        'remove_speed_limit'   : sign_ontology_infos['remove_speed_limit'],
        'has_speed_limit'      : sign_ontology_infos['has_speed_limit'],
        'precede_signs'        : sign_ontology_infos['precede_signs'],
        'precede_by'           : sign_ontology_infos['precede_by'],
        'removes_restrictions' : sign_ontology_infos['removes_restrictions'],
    }

    return jsonify(response), HTTPStatus.OK


@app.route('/about', methods=['GET'])
def about():
    """ /about?sign=<sign> route to display the sign information like type, category, meaning, legal regulation, etc.
    """

    sign_name = request.args.get('sign')

    # If the sign argument is missing or invalid, return an error page.
    if sign_name is None or sign_name == '':
       return render_template (
           'error_page.html', 
           title = 'Error - Missing or invalid Sign Argument',
           info = 'Sorry, the required sign argument is missing for the /about page.'
        ), HTTPStatus.BAD_REQUEST
    
    # Parse the url type sign name to the ontology type and use it to get the sign information.
    sign_name_in_ontology   = link_name_to_sparql(sign_name)
    sign_found , sign_ontology_infos = get_sign_ontology_infos(sign_name_in_ontology)

    if not sign_found:
        return render_template (
            'error_page.html', 
            title = 'Error - Sign Not Found',
            info = 'Sorry, the sign \'' + sign_name + '\' was not found in the ontology.'
        ), HTTPStatus.NOT_FOUND

    return render_template (
        template_name_or_list   = 'about_sign_page.html', 
        sign_name               = url_name_to_label(sign_name),
        sign_type               = sign_ontology_infos['label'],
        sign_category           = sign_ontology_infos['category'],
        sign_meaning            = sign_ontology_infos['meaning'],
        legal_regulation        = sign_ontology_infos['legal_regulation'],
        sign_color              = sign_ontology_infos['color'],
        sign_shape              = sign_ontology_infos['shape'],
        sign_remove_speed_limit = sign_ontology_infos['remove_speed_limit'],
        sign_has_speed_limit    = sign_ontology_infos['has_speed_limit'],
        sign_image              = url_for('static', filename = get_image_path(sign_name_in_ontology)),
        precede_signs           = get_signs_list(sign_ontology_infos['precede_signs']),
        precede_by              = get_signs_list(sign_ontology_infos['precede_by']),
        removes_restrictions    = get_signs_list(sign_ontology_infos['removes_restrictions']),
    ), HTTPStatus.OK
    
    
if __name__ == '__main__':
    app.run(debug=True)
