from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# App configurations 
app = Flask(__name__)

# DB configurations 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
## Data base instance 
# db = SQLAlchemy(app)

from sgp import views