from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import uuid
from functools import wraps

from ..entities.entity import Session
from ..entities.user import User, UserSchema


# def token_required(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
#
#         token = None
#
#         if 'x-access-tokens' in request.headers:
#             token = request.headers['x-access-tokens']
#
#         if not token:
#             return jsonify({'message': 'a valid token is missing'})
#
#         try:
#             data = jwt.decode(token, app.config[SECRET_KEY])
#             current_user = Users.query.filter_by(public_id=data['public_id']).first()
#         except:
#             return {'message': 'token is invalid'}
#
#             return f(current_user, *args, **kwargs)
#
#     return decorator


class Register(Resource):
    def post(self):
        data = request.get_json()

        if not data['username'] or not data['password'] or not data['email']:
            return {'message': 'not enough data'}

        hashed_password = generate_password_hash(data['password'], method='sha256')

        new_user = User(
            public_id=str(uuid.uuid4()),
            username=data['username'],
            password=hashed_password,
            email=data["email"])

        session = Session()
        session.add(new_user)
        session.commit()
        session.close()

        return {'message': 'registered successfully'}


class Login(Resource):
    def post(self):
        auth = request.get_json()
        print("XD")
        if not auth or not auth["username"] or not auth["password"]:
            return {'message': "Could not verify"}, 401

        session = Session()
        user = session.query(User).filter_by(Username=auth["username"]).first()
        session.commit()

        if check_password_hash(user.Password, auth["password"]):
            token = jwt.encode(
                {'public_id': user.PublicId, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                'SECRET_KEY', algorithm="HS256")

            return {'token': token}

        session.close()

        return {'message': 'could not verify'}, 401
