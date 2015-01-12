from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

#Example login form

class LoginForm(Form):
    email = TextField('Email Address', [Email(), Required(message='Email is required')])
    password = PasswordField('Password', [Required(message='Password is required')])
