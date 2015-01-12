from flask import Flask, render_template

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

#import the 'main' blueprint
from app.main.views import main as main

#Register the 'main' blueprint
app.register_blueprint(main)
