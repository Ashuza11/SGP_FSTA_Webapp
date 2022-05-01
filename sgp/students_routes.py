from turtle import title
from flask import  render_template, url_for, flash, redirect
from sgp import  app
from sgp.forms import StudentRegistrationForm, studentLoginForm


@app.route("/studentRegister")
def studentRegister():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.studentName.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('studentRegister.html', title='Student Register', form=form)

@app.route("/studentLogin")
def studentLogin():
     return render_template('studentLogin.html')
