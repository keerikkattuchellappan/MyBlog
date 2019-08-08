from flask import Flask
from config import Config 

blog = Flask(__name__)
blog.config.from_object(Config)

from app import routes
