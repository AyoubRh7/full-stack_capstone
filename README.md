# Capstone (Casting agency)

Udacity Full Stack Nanodegree capstone (Casting Agency)

## Motivation

This is a graduation project is for Udacity Full Stack web development nanondegree.

It is the fruit of the whole course using all capabilities learned.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Run this command to install all the required packages

```bash
pip install -r requirements.txt
```

- Set up database
After installing PostgresSQL create a new database and change the url in setup.sh


Then run the following command:

```bash
source setup.sh
```

- Start the server by running the command:
```bash
flask run
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


## Authentication 

For authentication we used Auth0 (a third party authentication app), it enable ust to assign roles and permissions to users.

Auth0 params to configure :
```py
AUTH0_DOMAIN = '<Auth domain>'
ALGORITHMS = ['RS256']
API_AUDIENCE = '<Api audience>'
```
### Tokens available for the next 24h:

CASTING_DIRECTOR = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imd2VmxzaXhwUk04SFNOWWZpeWFSVCJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYWowYy01Mi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzZjNmODA4ZjQ3MTQwMDcwZjAzNmIwIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzE3MTM4NTQsImV4cCI6MTYzMTgwMDI1NCwiYXpwIjoiYjdoYVJNS2RRdEc0aWVNOWQ2NWNna1dmY2dGMFQ5NU4iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.qsLmykQm03SzxKGc4iMkXhYQxZrHPHfN9VW5xvo7hsExjGMRs5GGZ4rLQtG8cRqwdV3x0J7uvfeLQllIP3dN_mbWkqFaBbk9CJzguuOrB8SQU_MZ2ncMdIlKYA2xs6U-RJ2fRBJYjbPJDpDhmIHxEWfaFZQbzrsUFgaEUDS8xl-VD8jUFTcPu2ujyl8Ij5mxV1KTFFoOrjesFs8A6gKy27S1nSwsNbDebQt-U8M7e2TkjTI_g145DQ2i6_LYjHTHbcZ3Zmq3enbQzyqPQNTFRq144y9Xc4O6jE2prfBg-pwb6C0R9rzzFyT1ohwfO-UYDcX_Rimyp6JCSPXOs5ob2g'

EXECUTIVE_PRODUCER = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imd2VmxzaXhwUk04SFNOWWZpeWFSVCJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYWowYy01Mi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzZjk0MjUwMDg0MjYwMDY5ZGI4N2U3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzE2NTk5MTUsImV4cCI6MTYzMTc0NjMxNSwiYXpwIjoiYjdoYVJNS2RRdEc0aWVNOWQ2NWNna1dmY2dGMFQ5NU4iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.WGMHPjDn8Z74ZBunGl473bP4Tik7jXSsKfqv0jSBvPuw3basQZC1RRg8ZOksvnACjxhPSDQvo4gtrKKZfgmZRxsuJy5vqwlQb-wb1C50Q98xR_nPDIAinxmfRIGgQU70vQGAzGqoRN3eeUYEJkmawYxVyQYtM9ezifaMBonMP3XqT7Mal-VqeKKx6JUmMkwEt1XyruiNp9D4FHz78shoHK2HjrmEI-9yKFIhQ7NSlevuSF9iBDXmHBhBvBeGDQ7WMcsPov8JNW41ROjo8bsaOae2ctSgfwXG2GXp8x9UZvVAL9DRZUGfTYgTSsdmoj2y5p4J5W9F8pAQP9C7B4T6rA'

CASTING_ASSISTANT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imd2VmxzaXhwUk04SFNOWWZpeWFSVCJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYWowYy01Mi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzZjNlZWZjYmQyNzAwMDY5Zjk2ZDMyIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzE3MTM2MjYsImV4cCI6MTYzMTgwMDAyNiwiYXpwIjoiYjdoYVJNS2RRdEc0aWVNOWQ2NWNna1dmY2dGMFQ5NU4iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.uJGSc3NHh0bMtH7o-DKEkNjbt4BP3KR3TXpKOIucKVNll3DGM3BS9BiysorsAUFsVzF2vt5OZzZrHufvTDXK8iJCgGTEDe8b-YkMTOaQBDH6D-Y0mSTBqFKMHjsmnEIiIIClyZEm5Ol4AYQ30tQjTGrM10RRYPVK10cHCiLEeyzjK8LHwLIcUn2GStGUyCI3YYJfsy24ob-XObPdU-4g04wNNZIOMSY4Vdl06o5x8UrUSxYA6ClSmWRCqkjdnuo9ZH2fNwEuhZ3VZ1kpqBkLcFfVLruyVpB8CdoIms2ou12S5h03Zdj2sIq-S4XoMMGS_jawJQPZV0wwEe6PrxZqDg'


### App roles with their permissions :


1. Casting Assistant:

- GET /actors (get:actors): can get all actors
- GET /movies (get:movies): can get all movies

2. Casting Director:
- GET /actors (get:actors): can get all actors
- GET /movies (get:movies): can get all movies
- POST /actors (create:actors): can create new actors
- PATCH /actors (update:actors): can update existing actors
- PATCH /movies (update:movies): can update existing movies
- DELETE /actors (delete:actors): can delete actors from database

3. Exectutive Director:
- GET /actors (get:actors): can get all actors
- GET /movies (get:movies): can get all movies
- POST /actors (create:actors): can create new actors
- POST /movies (create:movies): Can create new movies
- PATCH /actors (update:actors): can update existing actors
- PATCH /movies (update:movies): can update existing movies
- DELETE /actors (delete:actors): can delete actors from database
- DELETE /movies (delete:movies): Can delete movies from database


## Testing
Create another database and change the database path in test_app.py.
Then run the following cmd to run tests :
```
python test_app.py
```

## API Documentation

This section will introduce you to API endpoints and error handling


### Error handling

Errors are returned in JSON format:

```json
{
  "success": false,
  "error": 404,
  "message": "resource not found"
}
```

Returned errors types:

- 400 – bad request
- 404 – resource not found
- 422 – unprocessable
- 500 - internal server error

### API Endpoints

#### GET /movies

- General:
  - Returns all the movies data.
  - Authorized for : Executive Producer,Casting Assistant,Casting Director.

- Sample response:

```json
{
    "movies": [
        {
            "id": 1,
            "release_date": "Tue, 01 April 1956 00:00:00 GMT",
            "title": "Cukur"
        },
        {
            "id": 2,
            "release_date": "Mon, 01 May 2089 00:00:00 GMT",
            "title": "EDHO"
        }
    ],
    "success": true
}
```

#### GET /movies/\<int:id\>

- General:
  - Return one movie based on id.
  - Authorized for : Executive Producer,Casting Assistant,Casting Director.

- Sample response:

```json
{
    "movie": {
        "id": 1,
        "release_date": "Tue, 01 April 1956 00:00:00 GMT",
        "title": "Cukur"
    },
    "success": true
}
```

#### POST /movies

- General:
  - Create a new movie based .
  - Authorized for : Executive Producer.

- Sample response:
}'`

```json
{
    "movie": {
        "id": 3,
        "release_date": "Sun, 02 July 2020 00:00:00 GMT",
        "title": "Blacklist"
    },
    "success": true
}
```

#### PATCH /movies/\<int:id\>

- General:
  - Update a movie found by id .
  - Authorized for : Executive Producer,Casting Director.

- Sample response:

```json
{
    "movie": {
        "id": 3,
        "release_date": "Sun, 02 May 2045 00:00:00 GMT",
        "title": "Blacklist 2"
    },
    "success": true
}
```


#### DELETE /movies/<int:id\>


- General:
  - Delete a movies by found by passed id.
  - Authorized for: Executive Producer.

- Sample response:

```json
{
    "success": true,
    "message": "Movie was deleted successfully"
}
```

#### GET /actors

- General:
  - Returns all the actors data.
  - Authorized for: Casting Assistant,Casting Director,Executive Producer.

- Sample response:

```json
{
    "actors": [
        {
            "id": 1,
            "name": "Aras bulut",
            "age": 35,
            "gender": "M"
            
        },
        {
            "id": 2,
            "name": "Fatima weshay",
            "age": 50,
            "gender": "F"
            
        }
    ],
    "success": true
}
```

#### GET /actors/\<int:id\>

- General:
  - Returns an actor based on passed id.
  - Authorized for : Executive Producer,Casting Assistant,Casting Director.

- Sample response:

```json
{
    "actor": {
            "id": 1,
            "name": "Aras bulut",
            "age": 35,
            "gender": "M"
    },
    "success": true
}
```

#### POST /actors

- General:
  - Create an actor.
  - Authorized for : Executive Producer,Casting Director.

- Sample response:

```json
{
    "actor": {
            "id": 4,
            "name": "Oktay",
            "age": 55,
            "gender": "M"
    },
    "success": true
}
```

#### PATCH /actors/\<int:id\>

- General:
  - Update an actor using passed id.
  - Authorized for : Executive Producer,Casting Director.

- Sample response:

```json
{
    "actor": {
            "id": 4,
            "name": "Oktay kaynarca",
            "age": 58,
            "gender": "M"
    },
    "success": true
}
```


#### DELETE /actors/<int:id\>


- General:
  - Delete an actor using passed id.
  - Authorized for :Executive Producer,Casting Director.

- Sample response:

```json
{
    "message": "actor was deleted successfully",
    "success": true
}
```

## Authors
- Ayoub RHOUTTAISS
- Thanks to Udacity for providing the instructions
