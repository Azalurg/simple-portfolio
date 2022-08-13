from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/users')
def get_exams():
    # fetching from the database
    session = Session()
    exam_objects = session.query(User).all()

    # transforming into JSON-serializable objects
    schema = UserSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(exams.data)


@app.route('/users', methods=['POST'])
def add_exam():
    # mount exam object
    posted_user = UserSchema(only=('title', 'description'))\
        .load(request.get_json())

    user = User(**posted_user.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(user)
    session.commit()

    # return created exam
    new_user = UserSchema().dump(user).data
    session.close()
    return jsonify(new_user), 201