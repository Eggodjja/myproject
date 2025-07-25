import os

class Config(object):
    USER =  os.environ.get('POSTGRES_USER', 's1319')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', '571518')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5432)
    DB = os.environ.get('POSTGRES_DB', 'mydb')
    SQLALCHEMY_DATABASE_URI = 'postgresql://s1319:571518@localhost:5432/mydb'
    SECRET_KEY = 'ghfdjksvhgfjdk567ufghcdfj'
    SQLALCHEMY_TRACK_MODIFICATIONS = True