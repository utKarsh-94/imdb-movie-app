from flask import request, jsonify
from flask_restplus import Resource
from http import HTTPStatus
from typing import List
import marshmallow

from models.movie import Movie, Genre
from schemas.movie import MovieSchema, GenreSchema
from extenstions import db


movie_schema = MovieSchema()
movie_list_schema = MovieSchema(many=True)
genre_schema = GenreSchema()
genre_list_schema = GenreSchema(many=True)


class MovieListResource(Resource):

    def get(self):
        movie = Movie.get_all()
        return movie_list_schema.dump(movie), HTTPStatus.OK

    def post(self):
        data = request.get_json()
        movie_data = {}

        if Movie.get_movie_by_name(data['name']):
            return {'message': 'movie already exist'}, HTTPStatus.BAD_REQUEST

        movie_data = movie_schema.load(data)

        new_movie = Movie(**movie_data)
        db.session.add(new_movie)
        db.session.commit()

        new_movie = movie_schema.dump(new_movie)
                
        return new_movie, HTTPStatus.CREATED


class MovieResource(Resource):

    def get(self, movie_name):
        movie = Movie.get_movie_by_name(movie_name)
        if movie:
            mov = movie_schema.dump(movie)
            return mov, HTTPStatus.OK

        return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND

    def put(self, movie_name):
        data = request.get_json()
        mov = Movie.get_movie_by_name(movie_name)
        if mov:
            return movie_schema.dump(mov), HTTPStatus.OK

        return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND
