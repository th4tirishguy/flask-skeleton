# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

#Define a base model for the other models to inherit
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

#A sample user model that extends the base model

# class User(base):
#     __tablename__ = 'users'
#
#     firstname   = db.Column(db.String(255), nullable=False)
#     lastname    = db.Column(db.String(255), nullable=False)
#     username    = db.Column(db.String(255), nullable=False, unique=True)
#     email       = db.Column(db.String(255), nullable=False, unique=True)
#     pw_salt     = db.Column(db.String(255), nullable=False)
#     pw_hash     = db.Column(db.String(255), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % (self.username)
