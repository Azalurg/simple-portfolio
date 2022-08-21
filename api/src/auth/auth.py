from flask import request
import jwt
from functools import wraps

from ..entities.user import User
from ..entities.entity import Session


def token_required(function):

    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return {'message': 'a valid token is missing'}

        try:
            data = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        except:
            return {'message': 'token is invalid'}

        session = Session()
        current_user = session.query(User).filter_by(PublicId=data['public_id']).first()
        session.close()

        return function(user=current_user, *args, **kwargs)

    return decorator
