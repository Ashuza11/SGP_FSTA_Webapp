from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class StudentRegistrationForm(FlaskForm):
    studentName = StringField('Nom', 
                    validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    phone = StringField('Téléphone', validators=[DataRequired(), Length(10)]) 
    matricule = StringField('Matricule', validators=[DataRequired(), Length(6)])               
    password = PasswordField('Mot de pass', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmer mot de pass', 
                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("S'inscrire")

class studentLoginForm(FlaskForm):
    matricule = StringField('Matricule',
                    validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    # Secure cookie for keeping the user stay loged in for while 
    remember = BooleanField('Remember Me')
    submit = SubmitField('Se connecter')

     