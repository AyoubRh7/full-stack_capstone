import os
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import DateTime
from flask_sqlalchemy import SQLAlchemy
from datetime import date

# setting database config

#database_name ='capstone'
database_path = os.environ['DATABASE_URL']
#database_path = "postgresql://{}:{}@{}/{}".format('postgres','ayoub','localhost:5432', database_name)


db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# Initialise database and create tests data


def db_drop_create():
    db.drop_all()
    db.create_all()
    movie1 = Movie(title='War', release_date='01-02-2021')
    movie2 = Movie(title='Crime city', release_date='05-03-2051')
    movie3 = Movie(title='Kabsh', release_date='08-09-2001')

    movie1.insert()
    movie2.insert()
    movie3.insert()

    actor1 = Actor(name='Jeff', age=28, gender='M')
    actor2 = Actor(name='Sali', age=29, gender='F')
    actor3 = Actor(name='Rizk', age=45, gender='M')

    actor1.insert()
    actor2.insert()
    actor3.insert()

# Create Models

# Actor


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    age = db.Column(Integer)
    gender = db.Column(String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

# Movie


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(150), unique=True)
    release_date = db.Column(DateTime)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }
