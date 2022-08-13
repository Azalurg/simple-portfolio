from sqlalchemy import Column, String, ForeignKey, Integer

from .entity import Entity, Base


class Wallet(Entity, Base):
    __tablename__ = 'Wallets'

    UserId = Column(Integer, ForeignKey('Users.Id'))
    Name = Column(String, nullable=False, unique=True)

    def __init__(self, user_id, name):
        Entity.__init__(self, "script")
        self.UserId = user_id
        self.Name = name
