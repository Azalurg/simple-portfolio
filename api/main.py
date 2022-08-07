from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@127.0.0.1:5432/test'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'Users'
    Id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(64))
    Email = db.Column(db.String(64))
    Description = db.Column(db.String(255))
    JoiningDate = db.Column(db.Date)

    def __init__(self, username, email, description, joining_date):
        self.Username = username
        self.Email = email
        self.Description = description
        self.JoiningDate = joining_date


class Users(Resource):
    def get(self):
        result = User.query.all()
        output = []
        for user in result:
            new_user = {}
            new_user["Username"] = user.Username
            output.append(new_user)

        return jsonify(output)

    def post(self):
        today = date.today()
        user = User("Admin", "admin@xd.com", "", today)
        db.session.add(user)
        db.session.commit()
        return {"message": "Done"}


api.add_resource(Users, "/users")

if __name__ == "__main__":
    app.run(debug=True)
