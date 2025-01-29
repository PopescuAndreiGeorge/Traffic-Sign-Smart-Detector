from flask import render_template, request, jsonify, url_for
from flask_cors import CORS
from app import app
from http import HTTPStatus
from PIL import UnidentifiedImageError
import numpy as np
from datetime import datetime
import cv2

from .tools.sign_recognition import predict_sign
from .tools.utils import get_image_path, sparql_name_to_label, sparql_name_to_link, url_name_to_label, link_name_to_sparql
from .tools.sparql_queries import get_sign_category, get_sign_type, get_sign_meaning, get_sign_legal_regulation, get_sign_precede_by, get_sign_precede_signs, get_sign_removes_restriction

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

        sign_name_label = url_name_to_label(prediction)
        sign_name_in_ontology = link_name_to_sparql(prediction)

        category = get_sign_category(sign_name_in_ontology)
        meaning = get_sign_meaning(sign_name_in_ontology)
        legal_regulation = get_sign_legal_regulation(sign_name_in_ontology)

        return_json = {
            'name' : sign_name_label,
            'meaning' : meaning,
            'legal_regulation' : legal_regulation,
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
    
    sign_name_label = url_name_to_label(sign_name)
    sign_name_in_ontology = link_name_to_sparql(sign_name)

    sign_type = get_sign_type(sign_name_in_ontology)
    sign_category = get_sign_category(sign_name_in_ontology)
    legal_regulation = get_sign_legal_regulation(sign_name_in_ontology)
    sign_meaning = get_sign_meaning(sign_name_in_ontology)
    sign_image = url_for('static', filename = get_image_path(sign_name_in_ontology))

    print(f'Sign Image: {sign_image}')

    precede_signs = []
    precede_by = []
    removes_restrictions = []

    signs = get_sign_precede_signs(sign_name_in_ontology)
    for sign in signs:
        precede_signs.append ( { 
            'name': sparql_name_to_label(sign), 
            'about_url': url_for('about', sign = sparql_name_to_link(sign)), 
            'image_url': url_for('static', filename = get_image_path(sign))
        } )

    signs = get_sign_precede_by(sign_name_in_ontology)
    for sign in signs:
        precede_by.append ( { 
            'name': sparql_name_to_label(sign), 
            'about_url': url_for('about', sign = sparql_name_to_link(sign)), 
            'image_url': url_for('static', filename = get_image_path(sign))
        } )

    signs = get_sign_removes_restriction(sign_name_in_ontology)
    for sign in signs:
        removes_restrictions.append ( { 
            'name': sparql_name_to_label(sign), 
            'about_url': url_for('about', sign = sparql_name_to_link(sign)), 
            'image_url': url_for('static', filename = get_image_path(sign))
        } )

    return render_template (
        template_name_or_list = 'about_sign.html', 
        sign_name = sign_name_label,
        sign_meaning = sign_meaning,
        legal_regulation = legal_regulation,
        sign_category = sign_category,
        sign_type = sign_type,
        sign_image = sign_image,
        precede_signs = precede_signs,
        precede_by = precede_by,
        removes_restrictions = removes_restrictions,
    )
    
    
if __name__ == '__main__':
    app.run(debug=True)
