from flask_login import current_user, login_required, login_user,logout_user
from sgp.models import SuperAdmin, admin
from flask import  flash, redirect, render_template, url_for, request
from werkzeug.urls import url_parse
from sgp import  app
from sgp.forms import sperAdminLoginForm, adminLoginForm

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/superAdmin", methods=['GET', 'POST'])
def sperAdminLogin():
    if current_user.is_authenticated:
        return redirect(url_for('superAdminHome'))
    form = sperAdminLoginForm()
    if form.validate_on_submit():
        user = SuperAdmin.query.filter_by(userName=form.userName.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Erreur: Veuillez verifier vos parametres de connection!')
            return redirect(url_for('sperAdminLogin'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('superAdminHome')
        return redirect(url_for(next_page))
    return render_template('admin/SuperAdminLogin.html', title="Super-Admin-Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('sperAdminLogin'))


@app.route('/superAdminHome')
@login_required
def superAdminHome():
    return render_template('admin/adminLogin.html', title="Super-Admin-Home")




@app.route("/admin", methods=['GET', 'POST'])
def adminLogin():
    form = adminLoginForm()
    return render_template('admin/adminLogin.html', title="Super-Admin-Login", form=form)

