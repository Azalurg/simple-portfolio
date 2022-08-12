from sqlalchemy import Column, String

from .entity import Entity, Base


class User(Entity, Base):
    __tablename__ = 'Users'

    Username = Column(String, nullable=False, unique=True)
    Email = Column(String, nullable=False, unique=True)
    Description = Column(String)

    def __init__(self, username, email, description=None):
        Entity.__init__(self, "script")
        self.Username = username
        self.Email = email
        self.Description = description
