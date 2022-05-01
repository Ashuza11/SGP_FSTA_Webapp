from flask import Flask


# App configurations 
app = Flask(__name__)
app.config['SECRET_KEY'] = '_0ff424c986ca38f387558a452257306522_'

# DB configurations 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
## Data base instance 
# db = SQLAlchemy(app)

from sgp import routes
from sgp import students_routes

