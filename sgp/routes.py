from flask import  render_template, url_for
from sgp import  app
from sgp.forms import sperAdminLoginForm, adminLoginForm

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/superAdmin", methods=['GET', 'POST'])
def sperAdminLogin():
    form = sperAdminLoginForm()
    return render_template('admin/SuperAdminLogin.html', title="Super-Admin-Login", form=form)

@app.route("/admin", methods=['GET', 'POST'])
def adminLogin():
    form = adminLoginForm()
    return render_template('admin/adminLogin.html', title="Super-Admin-Login", form=form)