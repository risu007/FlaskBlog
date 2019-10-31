from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import validators
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username=StringField('Username',[validators.DataRequired(),validators.Length(min=2,max=20)])
    email=StringField('Email',[validators.DataRequired(),validators.Email()])
    password=PasswordField('Password',[validators.DataRequired(),validators.Length(min=8)])
    confirm_password= PasswordField('Confirm Password',
                                    [validators.DataRequired(),validators.Length(min=8),validators.EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise validators.ValidationError('That email is taken.Please choose different one!')
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise validators.ValidationError('That username is taken.Please choose different one!')

class LoginForm(FlaskForm):
    email=StringField('Email',[validators.DataRequired(),validators.Email()])
    password=PasswordField('Password',[validators.DataRequired(),validators.Length(min=8)])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username=StringField('Username',[validators.DataRequired(),validators.Length(min=2,max=20)])
    email=StringField('Email',[validators.DataRequired(),validators.Email()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed (  [ 'jpg',  'png' ] )])
    submit=SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise validators.ValidationError('That email is taken.Please choose different one!')
    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise validators.ValidationError('That username is taken.Please choose different one!')



class RequestResetForm(FlaskForm):
    email=StringField('Email',[validators.DataRequired(),validators.Email()])
    submit=SubmitField('Password Reset Request')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise validators.ValidationError('There is no account with this email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password=PasswordField('Password',[validators.DataRequired(),validators.Length(min=8)])
    confirm_password= PasswordField('Confirm Password',
                                    [validators.DataRequired(),validators.Length(min=8),validators.EqualTo('password')])
    submit=SubmitField('Reset Password')
