from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError
from models import User

class LoginForm(Form):
    email = StringField('Email',validators=[Required(), Length(1,64),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(Form):
    email = StringField('Email',validators=[Required(), Length(1,64),Email()])
    password = PasswordField('Password',validators=[Required(),
    EqualTo('password_confirmation',message="Passwords must match")])
    password_confirmation = PasswordField('Confirm Password',validators=[ Required()])
    submit = SubmitField('Register')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

class SettingsForm(Form):
    email = StringField('Email',validators=[Required(), Length(1,64),Email()])
    password = PasswordField('Password',validators=[EqualTo('password_confirmation',
    message="Passwords must match")])
    password_confirmation = PasswordField('Confirm Password')
    submit = SubmitField('Register')
    def validate_email(self,field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            print(field.data)
            print(user.email)
            if field.data != user.email:
                raise ValidationError('Email already registered')

class ForgotPasswordForm(Form):
    email = StringField('Email',validators =[Required(),Length(1,64),Email()])
    submit = SubmitField('Register')
