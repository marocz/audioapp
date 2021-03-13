from app import db
import datetime
#from datetime import datetime

class Song(db.Model):
    """
    Create a Song table
    """

    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    duration = db.Column(db.Integer)
    uploadtime  = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Song: {}>'.format(self.name)

class Podcast(db.Model):
    """
    Create a Podcast table
    """

    __tablename__ = 'podcast'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    duration = db.Column(db.Integer)
    uploadtime  = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    host = db.Column(db.String(100), unique=False)
    Participants = db.Column(db.String(100), unique=False)

    def __repr__(self):
        return '<Podcast: {}>'.format(self.name)

class Audiobook(db.Model):
    """
    Create a Audiobook table
    """

    __tablename__ = 'audiobook'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    duration = db.Column(db.Integer)
    uploadtime  = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    host = db.Column(db.String(100), unique=False)
    Narrator = db.Column(db.String(100), unique=False)

    def __repr__(self):
        return '<Audiobook: {}>'.format(self.name)