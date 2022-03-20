import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = 'postgres://nvufudlsptqkwj:c8d074f0773f578cc5009ad1eff5797c443b768893fc4ed092924366a0aac6f7@ec2-54-159-176-167.compute-1.amazonaws.com:5432/dagve64caeqoij'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = "./uploads"