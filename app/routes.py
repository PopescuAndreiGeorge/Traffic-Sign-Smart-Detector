from flask import Flask, render_template, request, redirect, url_for 
from app import app

@app.route('/')
def index():

    sign_info = {
        'name' : 'Stop Sign',
        'color' : 'Red',
        'shape' : 'Octagon',
        'meaning' : 'Stop and make sure the intersection is safe before proceeding.'
    }
    return render_template('main.html', sign_info=sign_info)

if __name__ == '__main__':
    app.run(debug=True)