import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from http import HTTPStatus
from flask_restplus import Api
from flask import Flask, jsonify, request
from flask_migrate import Migrate

from resources.movie import MovieListResource, MovieResource
from resources.user import UserListResource, UserResource
from resources.token import TokenResource


from config import Config
from extenstions import db, jwt


def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  regsiter_extensions(app)
  register_resources(app)

  return app


def regsiter_extensions(app):
  db.init_app(app)
  migrate = Migrate(app, db)
  jwt.init_app(app)


def register_resources(app):
  api = Api(app)

  api.add_resource(MovieListResource, '/movies')
  api.add_resource(MovieResource, '/movies/<string:movie_name>')
  
  api.add_resource(UserListResource, '/users')
  api.add_resource(UserResource, '/users/<string:username>')

  api.add_resource(TokenResource, '/token')


# if __name__ == "__main__":
#   app = create_app()
#   app.run(host='localhost', port=5000)
