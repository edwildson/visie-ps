from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}, methods = ["GET", "POST", "PATCH", "DELETE"], allow_headers = ["Content-Type", "Access-Control-Allow-Origin"])


db_username = os.environ.get('DB_USERNAME', '')
db_password = os.environ.get('DB_PASSWORD', '')
db_host = os.environ.get('DB_HOST', '')
db_name = os.environ.get('DB_NAME', '')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'

db = SQLAlchemy(app)

