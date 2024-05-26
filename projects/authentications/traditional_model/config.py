
USER_NAME = 'postgres'
PASSWORD = 'admin'
HOSTNAME = 'localhost'
PORT = '5433'
DB_NAME='trad_login'
import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_really_hard_to_guess_secret_key'
    SECRET_KEY = 'a_really_hard_to_guess_secret_key'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/dbname'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5433/trad_login'

    SQLALCHEMY_TRACK_MODIFICATIONS = False