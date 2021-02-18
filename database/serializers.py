from marshmallow import Schema, fields, post_load
from database.models import Song
import datetime
from  marshmallow.validate import Range
from marshmallow import validate

class SongSerializer(Schema):
    _id = fields.Int()
    name = fields.Str(required=True, validate=validate.Length(min=1,max=100))
    duration = fields.Int(required=True,validate=[Range(min=1, error="Value must be greater than 0")])
    uploaded_time = fields.DateTime(required=True, validate=lambda x: x > datetime.datetime.utcnow())


class PodcastSerializer(Schema):
    _id = fields.Int()
    name = fields.Str(required=True, validate=validate.Length(min=1,max=100))
    duration = fields.Int(required=True, validate=[Range(min=1, error="Value must be greater than 0")])
    uploaded_time = fields.DateTime(required=True, validate=lambda x: x > datetime.datetime.utcnow())
    host = fields.Str(required=True, validate=validate.Length(min=1,max=100))
    participants = fields.List(fields.Str(validate=validate.Length(min=1,max=100)), max_length=10, required=False)


class AudioBookSerializer(Schema):
    _id = fields.Int()
    title = fields.Str(required=True, validate=validate.Length(min=1,max=100))
    duration = fields.Int(required=True,validate=[Range(min=1, error="Value must be greater than 0")])
    uploaded_time = fields.DateTime(required=True, validate=lambda x: x > datetime.datetime.utcnow())
    narrator = fields.Str(required=True, validate=validate.Length(min=1,max=100))
    author = fields.Str(required=True, validate=validate.Length(min=1,max=100))

