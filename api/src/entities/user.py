from sqlalchemy import Column, String
from marshmallow import Schema, fields

from .entity import Entity, Base


class User(Entity, Base):
    __tablename__ = 'Users'

    Username = Column(String, nullable=False, unique=True)
    Email = Column(String, nullable=False, unique=True)
    Description = Column(String)

    def __init__(self, username, email, created_by="server", description=None):
        Entity.__init__(self, created_by)
        self.Username = username
        self.Email = email
        self.Description = description


class UserSchema(Schema):
    id = fields.Number()
    username = fields.Str()
    email = fields.Str()
    description = fields.Str()
    createdAt = fields.DateTime()
    updatedAt = fields.DateTime()
    lastUpdatedBy = fields.Str()
