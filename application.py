from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# App configurations 
app = Flask(__name__)

# DB configurations 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
## Data base instance 
db = SQLAlchemy(app)


# DataBase Model 


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/register")
def register():
    return "<h1>Register</h1>"

@app.route("/login")
def login():
     return "<h1>Login</h1>"


if __name__ == "__main__":
    app.run(debug=True)