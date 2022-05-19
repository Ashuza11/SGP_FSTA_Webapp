from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# App configurations 
app = Flask(__name__)
app.config.from_object(Config)

# Login Configuration
login = LoginManager(app)
login.login_view = 'sperAdminLogin'

# DB configurations 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from sgp import students_routes
from sgp import routes, models

