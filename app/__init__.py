from flask import Flask

blog = Flask(__name__)

from app import routes
