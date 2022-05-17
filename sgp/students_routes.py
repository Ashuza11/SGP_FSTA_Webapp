from crypt import methods
from turtle import title
from flask import  render_template, url_for, flash, redirect
import flask
from sgp import  app
from sgp.forms import StudentRegistrationForm, studentLoginForm


@app.route("/studentRegister", methods=['GET','POST'])
def studentRegister():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.studentName.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('student/studentRegister.html', title='Student-Register', form=form)

@app.route("/studentLogin", methods=['GET', 'POST'])
def studentLogin():
    form = studentLoginForm()
    if form.validate_on_submit():
        if form.matricule.data =='15635' and form.password.data == 'ashpwd':
            flask('vous avez été connecté', 'success')
            return redirect(url_for('student_Home'))
        else:
            flash('Erreur: Veuillez verifier vos parametres de connection!', 'danger')
    return render_template('student/studentLogin.html', title="Student-Login", form=form)
