from functools import wraps
from werkzeug.exceptions import BadRequest


def validate_input(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            raise BadRequest()

    return decorated

