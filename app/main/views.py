from flask import Blueprint, request, render_template, redirect, url_for

#import the database object from the main app module
from app import db

#importmodule forms
from app.main.forms import LoginForm

#import module forms(i.e User)
#from app.main.models import User

#Define the blueprint
main = Blueprint('main', __name__)

#routes for this blueprint

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        return 'Success'
    else:
        return 'Home page'
