from marshmallow import Schema, fields, pre_dump, post_dump, pre_load, post_load
from models.movie import Genre, Movie


class GenreSchema(Schema):
  
  id = fields.String(required=True)

  @pre_load
  def pre_load_id(self, data, *args, **kwargs):
    data = {'id': data}
    return data

  @post_load
  def post_load_id(self, data, *args, **kwargs):
    genre = Genre(**data)
    return genre

  @post_dump
  def pre_process_dump(self, data, *args, **kwargs):
    return data['id']


class MovieSchema(Schema):
  class Meta:
    ordered = True
  
  id = fields.Int(dump_only=True)
  name = fields.String(required=True)
  imdb_score = fields.Float(required=True)
  director = fields.String(required=True)
  popularity = fields.Float(required=True)
  genre = fields.Nested(GenreSchema(many=True))

  @pre_load
  def pre_load_data(self, data, *args, **kwrags):
    data['popularity'] = data['99popularity']
    del data['99popularity']
    return data






