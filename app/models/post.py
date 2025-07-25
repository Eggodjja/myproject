from datetime import datetime, timezone
from ..extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    email = db.Column(db.String(250))
    