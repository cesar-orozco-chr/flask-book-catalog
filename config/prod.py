import os

SECRET_KEY = 'mysecretkey'
ENV = 'production'
DEBUG = False
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] 
SQLALCHEMY_TRACK_MODIFICATIONS = False