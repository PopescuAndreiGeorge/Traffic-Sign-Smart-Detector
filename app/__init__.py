from flask import Flask
from config import Config
from .models import db
from .views import main_bp
import dotenv

# Load the environment variables from the .env file
if dotenv.load_dotenv('.env'):
    print('The environment variables were loaded successfully.')
else:
    print('The environment variables were not loaded.')

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TraS.db'

db.init_app(app)
app.register_blueprint(main_bp)

from app import routes, models
