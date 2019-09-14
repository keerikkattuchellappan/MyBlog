from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

blog = Flask(__name__)
blog.config.from_object(Config)
db = SQLAlchemy(blog)
migrate = Migrate(blog,db)
login = LoginManager(blog)
login.login_view = 'login'

from app import routes, models #models needs to be added.



