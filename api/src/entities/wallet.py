from sqlalchemy import Column, String, ForeignKey, Integer, JSON, DateTime

from .entity import Entity, Base


class Wallet(Entity, Base):
    __tablename__ = 'Wallets'

    UserId = Column(String, ForeignKey('Users.Id'))
    Name = Column(String, nullable=False, unique=True)
    State = Column(JSON)
    WrongTransactions = Column(JSON)
    LastCompilation = Column(DateTime)

    def __init__(self, user_id, name):
        Entity.__init__(self, "script")
        self.UserId = user_id
        self.Name = name
        self.State = {}
        self.WrongTransactions = {"transactions": []}
        self.LastCompilation = None

    def json(self):
        return {
            "Id": self.Id,
            "UserId": self.UserId,
            "Name": self.Name,
            "State": self.State,
            "WrongTransactions": self.WrongTransactions,
            "LastCompilation": self.LastCompilation.strftime("%y-%m-%d"),
            "CreatedAt": self.State.strftime("%y-%m-%d"),
            "UpdatedAt": self.WrongTransactions.strftime("%y-%m-%d"),
            "LastUpdatedBy": self.LastCompilation
        }
