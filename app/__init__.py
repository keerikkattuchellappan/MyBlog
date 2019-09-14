from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

blog = Flask(__name__)
blog.config.from_object(Config)
db = SQLAlchemy(blog)
migrate = Migrate(blog,db)

from app import routes, models #models needs to be added.



