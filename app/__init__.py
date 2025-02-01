from flask import Flask
from config import Config
import dotenv

# Load the environment variables from the .env file
if dotenv.load_dotenv('.env'):
    print('[INFO] The environment variables were loaded successfully.')
else:
    print('INFO] The environment variables were not loaded.')

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
