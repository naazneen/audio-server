from .db import db
from mongoengine import *
import datetime


class Song(db.Document):
  
    id = db.SequenceField(primary_key=True)
    name = db.StringField(required=True)
    duration = db.IntField(required=True)
    uploaded_time = db.DateTimeField(default=datetime.datetime.utcnow,required=True)


class Podcast(db.Document):
    id = db.SequenceField(primary_key=True)
    name = db.StringField(required=True)
    duration = db.IntField(required=True)
    uploaded_time = db.DateTimeField(default=datetime.datetime.utcnow,required=True)
    host = db.StringField(max_length=100 ,required=True)
    participants = db.ListField(db.StringField(max_length=100),max_length=10, required=False)

class AudioBook(db.Document):
    id = db.SequenceField(primary_key=True)
    title = db.StringField(required=True)
    duration = db.IntField(required=True)
    uploaded_time = db.DateTimeField(default=datetime.datetime.utcnow,required=True)
    narrator = db.StringField(max_length=100 ,required=True)
    author = db.StringField(max_length=100 ,required=True)
    