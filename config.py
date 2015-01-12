DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Database connection
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

#Enable csrf protection
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secert"

#Secret key for signing cookies
SECRET_KEY = "secret"
