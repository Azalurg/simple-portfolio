from sqlalchemy import Column, String, ForeignKey, Integer, Float, DateTime

from .entity import Entity, Base


class Transaction(Entity, Base):
    __tablename__ = 'Transactions'
    Id = Column(Integer, primary_key=True)
    WalletId = Column(Integer, ForeignKey('Wallets.Id'), nullable=False)
    Type = Column(String, nullable=False)
    BuyAmount = Column(Float)
    BuyCur = Column(String(16))
    SellAmount = Column(Float)
    SellCur = Column(String(16))
    CommissionAmount = Column(Float)
    CommissionCur = Column(String(16))
    Description = Column(String)
    Date = Column(DateTime, nullable=False)

    def __init__(self, wallet_id, type, date,
                 buy_amount=None, buy_cur=None, sell_amount=None, sell_curr=None,
                 commission_amount=None, commission_curr=None, description=None):
        Entity.__init__(self, "script")
        self.WalletId = wallet_id
        self.Type = type
        self.BuyAmount = buy_amount
        self.BuyCur = buy_cur
        self.SellAmount = sell_amount
        self.SellCur = sell_curr
        self.CommissionAmount = commission_amount
        self.CommissionCur = commission_curr
        self.Description = description
        self.Date = date
