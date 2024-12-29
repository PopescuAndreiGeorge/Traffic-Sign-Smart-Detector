from flask import render_template, request, jsonify 
from app import app
from http import HTTPStatus
from PIL import Image, UnidentifiedImageError
import numpy as np

@app.route('/')
def index():

    sign_info = {
        'name' : 'Stop Sign',
        'color' : 'Red',
        'shape' : 'Octagon',
        'meaning' : 'Stop and make sure the intersection is safe before proceeding.'
    }
    
    return render_template('main.html', sign_info=sign_info)

@app.route('/sign', methods=['POST'])
def sign():
    """ Get a sign image via POST request and log the image file infos
    """

    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'}), HTTPStatus.BAD_REQUEST

    try:
        image = np.array(Image.open(request.files['image']))

        sign_info = {
            'name' : request.files['image'].filename,
            'meaning' : 'And image with shape: ' + str(image.shape)
        }

        return jsonify(sign_info), HTTPStatus.OK

    except UnidentifiedImageError as e:
        return jsonify({'error': 'Image processing error: ' + str(e)}), HTTPStatus.BAD_REQUEST

    
if __name__ == '__main__':
    app.run(debug=True)