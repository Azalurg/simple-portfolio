from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from .entities.entity import engine, Base
from .routes.users import Users
from .routes.auth import Register, Login

# creating the Flask application
app = Flask(__name__)
CORS(app)
api = Api(app)
# if needed, generate database schema
Base.metadata.create_all(engine)

api.add_resource(Register, "/register")
api.add_resource(Login, "/login")

if __name__ == "__main__":
    app.run(debug=True)
