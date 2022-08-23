from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from ..entities.user import User
from ..entities.entity import Session
from ..auth.auth import token_required


class Users(Resource):

    @token_required
    def get(self, user=None):
        return user.json()
