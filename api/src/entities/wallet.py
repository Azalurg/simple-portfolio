from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from datetime import datetime

from .entity import Entity, Base


class Wallet(Entity, Base):
    __tablename__ = 'Wallets'

    UserId = Column(String, ForeignKey('Users.Id'))
    Name = Column(String, nullable=False, unique=True)
    BaseCurrency = Column(String, nullable=False)

    def __init__(self, user_id, name):
        Entity.__init__(self, "script")
        self.UserId = user_id
        self.Name = name
        self.BaseCurrency = "USD"

    def json(self):
        return {
            "Id": self.Id,
            "UserId": self.UserId,
            "Name": self.Name,
            "BaseCurrency": self.BaseCurrency,
            "LastCompilation": self.LastCompilation.strftime("%y-%m-%d"),
            "CreatedAt": self.CreatedAt.strftime("%y-%m-%d"),
            "UpdatedAt": self.UpdatedAt.strftime("%y-%m-%d"),
            "LastUpdatedBy": self.LastCompilation
        }
