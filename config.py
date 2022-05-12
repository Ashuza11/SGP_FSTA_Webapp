import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Form validation Key
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_0ff424c986ca38f387558a452257306522_'
  
    # Data Base configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False