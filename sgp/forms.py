from random import choices
from secrets import choice
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers


Promotions = [
    "", "G0","L1","L2","L3", "G3", "Tech1", "Tech2"
]
class StudentRegistrationForm(FlaskForm):
    studentName = StringField('Nom', 
                    validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    phone = StringField('Téléphone', validators=[DataRequired()]) 
    matricule = StringField('Matricule', validators=[DataRequired(), Length(5)]) 
    promotion = SelectField("Promotion", choices=Promotions)              
    password = PasswordField('Mot de pass', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmer mot de pass', 
                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("S'inscrire")

    def validate_phone(form, field):
        if len(field.data) > 13:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+234"+field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')

    
class studentLoginForm(FlaskForm):
    matricule = StringField('Matricule',
                    validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    # Secure cookie for keeping the user stay loged in for while 
    remember = BooleanField('Remember Me')
    submit = SubmitField('Se connecter')

     
class sperAdminLoginForm(FlaskForm):
    userName = StringField('Email ou Username',
                    validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    # Secure cookie for keeping the user stay loged in for while 
    remember = BooleanField('Remember Me')
    submit = SubmitField('Se connecter')

class adminLoginForm(FlaskForm):
    userName = StringField('Email ou Username',
                    validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    # Secure cookie for keeping the user stay loged in for while 
    remember = BooleanField('Remember Me')
    submit = SubmitField('Se connecter')