from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), 
        EqualTo('confirm_pass', message='Passwords is different')])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    # password = PasswordField('Password', validators=[DataRequired(), 
    #     EqualTo('confirm_pass', message='Passwords is different')])
    # confirm_pass = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
