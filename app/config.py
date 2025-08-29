import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    USER =  os.environ.get('POSTGRES_USER')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    HOST = os.environ.get('POSTGRES_HOST')
    PORT = os.environ.get('POSTGRES_PORT')
    DB = os.environ.get('POSTGRES_DB')
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-fallback-secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
=======
    DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-fallback-secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 677dfb4 (add everything without E2E tests)
