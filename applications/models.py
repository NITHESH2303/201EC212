from applications.config import *
from applications.models import *
from applications.database import db
from datetime import datetime

class train(db.Model):
    __tablename__ = 'train'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    time = db.Column(db.DateTime, index = True, default = datetime.now())
    seats = db.Column(db.Integer, index = True, default = 500)