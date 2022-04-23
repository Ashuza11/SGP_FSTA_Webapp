from flask import Flask, render_template

app = Flask(__name__)

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