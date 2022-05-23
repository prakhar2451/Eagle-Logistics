import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5272a1ed792b550511e4f43'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # For creating the database and its location for flask
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from logistics import routes