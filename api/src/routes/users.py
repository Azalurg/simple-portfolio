from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from ..entities.user import User, UserSchema
from ..entities.entity import Session


class Users(Resource):
    def get(self):
        session = Session()
        exam_objects = session.query(User).all()

        # transforming into JSON-serializable objects
        schema = UserSchema(many=True)
        users = schema.dump(exam_objects)

        # serializing as JSON
        session.close()
        return jsonify(users)

    def post(self):
        # mount exam object
        posted_user = UserSchema(only=('username', 'email', 'description'))\
            .load(request.get_json())

        user = User(**posted_user, created_by="HTTP post request")

        # persist exam
        session = Session()
        session.add(user)
        session.commit()

        # return created exam
        session.close()
        return {"message": "User added"}, 201