import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import os

# Auth0 parameters
#AUTH0_DOMAIN = 'dev-0aj0c-52.us.auth0.com'
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = 'capstone'
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
API_AUDIENCE = os.environ.get('API_AUDIENCE')

# AuthError Exception


class AuthError(Exception):

    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Get Auth Header
def get_token_auth_header():
    token_auth_header = request.headers.get('Authorization', None)
    if not token_auth_header:
        raise AuthError({
            'code': 'authorization_header_missing',
            'descreption': 'authorization is expected'
        }, 401)
    token_header_parts = token_auth_header.split(' ')
    if(token_header_parts[0].lower() != 'bearer'):
        raise AuthError({
            'code': 'ivalid_bearer',
            'description': 'authorization must starts with bearer'
        }, 401)
    elif (len(token_header_parts) != 2):
        raise AuthError({
            'code': 'ivalid_header',
            'description': 'authorization must be in bearer token format'
        }, 401)
    token = token_header_parts[1]
    return token


# Checking permissions
def check_permissions(payload, permission):
    if ('permissions' not in payload):
        raise AuthError({
            'code': 'ivalid_claims',
            'description': 'permissions are not included in the token'
        }, 400)
    if (permission not in payload['permissions']):
        raise AuthError({
            'code': 'unauthorized',
            'description': 'permissions not found'
        }, 403)
        return True


# Verifying the token
def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    rsa_key = {}
    unvirefied_header = jwt.get_unverified_header(token)

    if 'kid' not in unvirefied_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'authorization malformed'
        }, 401)
    for key in jwks['keys']:
        if key['kid'] == unvirefied_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
            break
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f'https://{AUTH0_DOMAIN}/'
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'token expired'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorect claims, pleas check the audience and issuer'
            }, 401)

        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'unable to parse authentication token'
            }, 400)

    raise AuthError({
        'code': 'invalid_header',
        'description': 'unable to find the appropriate key'
    }, 400)


'''
 @requires_auth(permission) decorator method

    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims and check the requested permission
    return the decorator which passes the decoded payload to the decorated method
'''


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(payload, permission)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
