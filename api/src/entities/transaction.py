from sqlalchemy import Column, String, ForeignKey, Integer, Float, DateTime

from .entity import Entity, Base


class Transaction(Entity, Base):
    __tablename__ = 'Transactions'

    WalletId = Column(String, ForeignKey('Wallets.Id'), nullable=False)
    Type = Column(String(31), nullable=False)
    BuyAmount = Column(Float)
    BuyCur = Column(String(15))
    SellAmount = Column(Float)
    SellCur = Column(String(15))
    CommissionAmount = Column(Float)
    CommissionCur = Column(String(15))
    Description = Column(String)
    Date = Column(DateTime, nullable=False)
    Api = Column(String(15), nullable=False)

    def __init__(self, wallet_id, transaction_type, date, api, buy_amount=None, buy_cur=None, sell_amount=None,
                 sell_cur=None, commission_amount=None, commission_curr=None, description=None):
        Entity.__init__(self, "script")
        self.WalletId = wallet_id
        self.Type = transaction_type
        self.BuyAmount = buy_amount
        self.BuyCur = buy_cur
        self.SellAmount = sell_amount
        self.SellCur = sell_cur
        self.CommissionAmount = commission_amount
        self.CommissionCur = commission_curr
        self.Description = description
        self.Date = date
        self.Api = api

    def json(self):
        return {
            "Id": self.Id,
            "WalletId": self.WalletId,
            "Type": self.Type,
            "BuyAmount": self.BuyAmount,
            "BuyCur": self.BuyCur,
            "SellAmount": self.SellAmount,
            "SellCur": self.SellCur,
            "CommissionAmount": self.CommissionAmount,
            "CommissionCur": self.CommissionCur,
            "Description": self.Description,
            "Date": self.Date.strftime("%y-%m-%d"),
            "Api": self.Api,
            "CreatedAt": self.CreatedAt.strftime("%y-%m-%d"),
            "UpdatedAt": self.UpdatedAt.strftime("%y-%m-%d"),
            "LastUpdatedBy": self.LastUpdatedBy,
        }
