from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

from ..entities.entity import Session
from ..entities.user import User


class Register(Resource):
    def post(self):
        data = request.get_json()

        if not data['username'] or not data['password'] or not data['email']:
            return {'message': 'not enough data'}

        hashed_password = generate_password_hash(data['password'], method='sha256')

        new_user = User(
            username=data['username'],
            password=hashed_password,
            email=data['email'])

        session = Session()
        session.add(new_user)
        session.commit()
        session.close()

        return {'message': 'registered successfully'}


class Login(Resource):
    def post(self):
        auth = request.get_json()
        if not auth or not auth["username"] or not auth["password"]:
            return {'message': "Could not verify"}, 401

        session = Session()
        user = session.query(User).filter_by(Username=auth["username"]).first()
        session.commit()

        if check_password_hash(user.Password, auth["password"]):
            token = jwt.encode(
                {'id': user.Id, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=120)},
                'SECRET_KEY', algorithm="HS256")

            return {'token': token}

        session.close()

        return {'message': 'could not verify'}, 401
