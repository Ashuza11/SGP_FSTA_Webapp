from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# App configurations 
app = Flask(__name__)
app.config.from_object(Config)

# DB configurations 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from sgp import routes
from sgp import students_routes

