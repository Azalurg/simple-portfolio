from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import uuid
from functools import wraps

from ..entities.entity import Session
from ..entities.user import User, UserSchema

def token_required(f):  
    @wraps(f)  
    def decorator(*args, **kwargs):

       token = None 

       if 'x-access-tokens' in request.headers:  
          token = request.headers['x-access-tokens'] 


       if not token:  
          return jsonify({'message': 'a valid token is missing'})   


       try:  
          data = jwt.decode(token, app.config[SECRET_KEY]) 
          current_user = Users.query.filter_by(public_id=data['public_id']).first()  
       except:  
          return {'message': 'token is invalid'}


          return f(current_user, *args,  **kwargs)  
    return decorator 

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
            email=data[email])

        session = Session()
        session.add(new_user)
        session.commit()
        session.close()

        return {'message': 'registered successfully'}
