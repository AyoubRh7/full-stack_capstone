import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import db, setup_db, Actor, Movie
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

# Welcoming route
    @app.route('/')
    def home():
        return jsonify({
            'message': 'Welcome to ayb casting agency',
            'success': True
        }), 200

    # Movies routes:

    # Getting all movies data
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        try:
            movies = Movie.query.all()

            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in movies]
            }), 200
        except BaseException:
            abort(422)

    # Getting one movie based on passed id
    @app.route('/movies/<int:id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_one_movie(jwt, id):
        try:
            movie = Movie.query.filter_by(id=id).one_or_none()

            return jsonify({
                'success': True,
                'movie': movie.format()
            }), 200
        except BaseException:
            abort(404)

    # Add a new movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):
        data = request.get_json()
        title = data.get('title', None)
        release_date = data.get('release_date', None)
        if None in [title, release_date]:
            abort(400)
        try:
            movie = Movie(title=title, release_date=release_date)
            movie.insert()
            return jsonify({
                'success': True,
                'movie': movie.format()
            }), 201
        except BaseException:
            abort(500)

    # Update a movie
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(jwt, id):
        data = request.get_json()
        title = data.get('title', None)
        release_date = data.get('release_date', None)
        movie = Movie.query.filter_by(id=id).one_or_none()
        if None in [title, release_date]:
            abort(400)
        if movie is None:
            abort(404)
        try:
            movie.title = title
            movie.release_date = release_date
            movie.update()
            return jsonify({
                'success': True,
                'movie': movie.format()
            }), 200
        except BaseException:
            abort(500)

    # Delete a movie
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, id):
        movie = Movie.query.filter_by(id=id).one_or_none()
        if movie is None:
            abort(404)
        try:
            movie.delete()
            return jsonify({
                'success': True,
                'message': 'Movie was deleted successfully'
            })
        except BaseException:
            abort(500)

    # Actors routes:

    # Getting all actors data

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):
        try:
            actors = Actor.query.all()

            return jsonify({
                'success': True,
                'actors': [actor.format() for actor in actors]
            }), 200
        except BaseException:
            abort(422)

    # Getting an actor data based on passed  id
    @app.route('/actors/<int:id>', methods=['GET'])
    @requires_auth('get:actors')
    def get_one_actor(jwt, id):
        try:
            actor = Actor.query.filter_by(id=id).one_or_none()

            return jsonify({
                'success': True,
                'actor': actor.format()
            }), 200
        except BaseException:
            abort(404)

    # Add a new actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(jwt):
        data = request.get_json()
        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)
        if None in [name, age, gender]:
            abort(400)
        try:
            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()
            return jsonify({
                'success': True,
                'actor': actor.format()
            }), 201
        except BaseException:
            abort(500)

    # Update an actor
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(jwt, id):
        data = request.get_json()
        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)
        actor = Actor.query.filter_by(id=id).one_or_none()
        if None in [name, age, gender]:
            abort(400)
        if actor is None:
            abort(404)
        try:
            actor.name = name
            actor.age = age
            actor.gender = gender
            actor.update()
            return jsonify({
                'success': True,
                'actor': actor.format()
            }), 200
        except BaseException:
            abort(500)

    # Delete an actor
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, id):
        actor = Actor.query.filter_by(id=id).one_or_none()
        if actor is None:
            abort(404)
        try:
            actor.delete()
            return jsonify({
                'success': True,
                'message': 'actor was deleted successfully'
            })
        except BaseException:
            abort(500)

    # Error Handling

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable entity'
        }), 422

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    # handling AuthErrors
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code,

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
