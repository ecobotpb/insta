from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "so-eu-sei"
from app import routes
