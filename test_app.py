import os
import json
import unittest
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor, db_drop_create

# users tokens
CASTING_DIRECTOR = os.environ.get('CASTING_DIRECTsOR')
EXECUTIVE_PRODUCER = os.environ.get('EXECUTIVE_PRODUCER')
CASTING_ASSISTANT = os.environ.get('CASTING_ASSISTANT')


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ.get('TEST_DATABASE_URL')
        setup_db(self.app, self.database_path)
        db_drop_create()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

# Movies tests:

    # Test getting all movies
    def test_get_movies(self):
        res = self.client().get(
            '/movies',
            headers={
                'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # Test getting one movie by id
    def test_get_one_movie(self):
        res = self.client().get(
            '/movies/1',
            headers={
                'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Test getting a movie that does not exist (failing)
    def test_not_found_movie(self):
        res = self.client().get('/movies/55555',
                                headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    # Test adding a new movie
    def test_create_movie(self):
        test_movie = {
            'title': 'Cukur',
            'release_date': '01/02/2022'
        }
        res = self.client().post(
            '/movies',
            json=test_movie,
            headers={
                'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie']['title'], 'Cukur')

    # Test adding a movie with no data (failing)
    def test_create_empty_movie(self):
        test_movie = {}
        res = self.client().post(
            '/movies',
            json=test_movie,
            headers={
                'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    # Test updating a movie
    def test_update_movie(self):
        test_movie = {
            'title': 'EDHO',
            'release_date': '11/05/2028'
        }
        res = self.client().patch(
            '/movies/2',
            json=test_movie,
            headers={
                'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie']['title'], 'EDHO')

    # Test updating a movie that does not exist
    def test_update_inexistent_movie(self):
        test_movie = {
            'title': 'ko',
            'release_date': '11/05/2028'
        }
        res = self.client().patch(
            '/movies/123456',
            json=test_movie,
            headers={
                'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    # Test deleting a movie

    def test_delete_movie(self):

        res = self.client().delete('/movies/3',
                                   headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Movie was deleted successfully')

    # Test deleting a movie that does not exist
    def test_delete_inexistent_movie(self):

        res = self.client().delete('/movies/157518',
                                   headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')


# Actors tests:

    # Test getting all actors


    def test_get_actors(self):
        res = self.client().get(
            '/actors',
            headers={
                'Authorization': f'Bearer {CASTING_DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # Test getting one actor by id
    def test_get_one_actore(self):
        res = self.client().get(
            '/actors/1',
            headers={
                'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    # Test getting an actor that does not exist (failing)
    def test_not_found_actor(self):
        res = self.client().get('/actors/33333',
                                headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    # Test adding a new actor
    def test_create_actor(self):
        test_actor = {
            'name': 'Aras',
            'age': '35',
            'gender': 'M'
        }
        res = self.client().post(
            '/actors',
            json=test_actor,
            headers={
                'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertEqual(data['actor']['name'], 'Aras')

    # Test adding an actor with no data (failing)
    def test_create_empty_actor(self):
        test_actor = {}
        res = self.client().post(
            '/actors',
            json=test_actor,
            headers={
                'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    # Test updating an actor
    def test_update_actor(self):
        test_actor = {
            'name': 'Mohammed',
            'age': '20',
            'gender': 'M'
        }
        res = self.client().patch(
            '/actors/2',
            json=test_actor,
            headers={
                'Authorization': f'Bearer {CASTING_DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertEqual(data['actor']['name'], 'Mohammed')

    # Test updating an actor that does not exist
    def test_update_inexistent_actor(self):
        test_actor = {
            'name': 'simo',
            'age': '88',
            'gender': 'M'
        }
        res = self.client().patch(
            '/actors/869445',
            json=test_actor,
            headers={
                'Authorization': f'Bearer {CASTING_DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    # Test deleting an actor
    def test_delete_actor(self):

        res = self.client().delete('/actors/3',
                                   headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'actor was deleted successfully')

    # Test deleting an actor that does not exist
    def test_delete_inexistent_actor(self):

        res = self.client().delete('/actors/187218',
                                   headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')


# Failed authentication RBAC tests:

    def test_update_actor_no_permissions(self):
        test_actor = {
            'name': 'Salma',
            'age': '33',
            'gender': 'F'
        }
        res = self.client().patch(
            '/actors/1',
            json=test_actor,
            headers={
                'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 403)
        self.assertEqual(data['message'], 'permissions not found')

    def test_update_movie_no_permissions(self):
        test_movie = {
            'title': 'Inception',
            'release_date': '03/05/2021'
        }
        res = self.client().patch(
            '/movies/1',
            json=test_movie,
            headers={
                'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 403)
        self.assertEqual(data['message'], 'permissions not found')

    def test_create_movie_no_permissions(self):
        test_movie = {
            'title': 'GOT',
            'release_date': '07/02/2021'
        }
        res = self.client().post(
            '/movies',
            json=test_movie,
            headers={
                'Authorization': f'Bearer {CASTING_DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 403)
        self.assertEqual(data['message'], 'permissions not found')

    def test_no_permission_delete_movie(self):

        res = self.client().delete('/movies/1',
                                   headers={'Authorization': f'Bearer {CASTING_DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['error'], 403)
        self.assertEqual(data['message'], 'permissions not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
