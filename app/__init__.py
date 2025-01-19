from flask import Flask
from config import Config
from .models import db
from .views import main_bp
import dotenv

# Load the environment variables from the .env file
dotenv.load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TraS.db'

db.init_app(app)
app.register_blueprint(main_bp)

from app import routes, models
