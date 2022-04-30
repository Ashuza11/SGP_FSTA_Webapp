from flask import  render_template
from sgp import  app


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/register")
def register():
    return "<h1>Register</h1>"

@app.route("/login")
def login():
     return "<h1>Login</h1>"
