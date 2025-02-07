import functools
from flask import jsonify, request, make_response as response

def auth(func):
    """
    Decorator to check if the request has a token in its headers,
    if it does, the function is executed, otherwise a 401 response
    is sent with a JSON containing an error key with value 'unauthorized'.
    """
    @functools
    def wrapper(*args, **kwargs):
        if request.headers.get('token'):
            return func(*args, **kwargs)
        else:
            return response(jsonify({'error': 'unauthorized'}), 401)
    return wrapper