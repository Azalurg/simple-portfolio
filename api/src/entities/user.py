from sqlalchemy import Column, String
from marshmallow import Schema, fields

from .entity import Entity, Base


class User(Entity, Base):
    __tablename__ = 'Users'

    PublicId = Column(String, nullable=False, unique= True)
    Username = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False, unique= True)
    Email = Column(String, nullable=False, unique=True)
    Description = Column(String)

    def __init__(self, public_id, username, password, email, created_by="server", description=None):
        Entity.__init__(self, created_by)
        self.PublicId = public_id
        self.Username = username
        self.Password = password
        self.Email = email
        self.Description = description


class UserSchema(Schema):
    id = fields.Number()
    publicId = fields.Str()
    username = fields.Str()
    password = fields.Str()
    email = fields.Str()
    description = fields.Str()
    createdAt = fields.DateTime()
    updatedAt = fields.DateTime()
    lastUpdatedBy = fields.Str()
