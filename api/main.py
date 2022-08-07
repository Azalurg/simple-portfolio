from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@127.0.0.1:5432/test'
db = SQLAlchemy(app)

# Models


class Wallet(db.Model):
    __tablename__ = 'Wallets'
    Id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey('Users.Id'))
    Name = db.Column(db.String(64))

    def __init__(self, user_id, name):
        self.UserId = user_id
        self.Name = name


class User(db.Model):
    __tablename__ = 'Users'
    Id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(64))
    Email = db.Column(db.String(64))
    Description = db.Column(db.String(255))
    JoiningDate = db.Column(db.Date)

    def __init__(self, username, email, description, joining_date):
        self.Username = username
        self.Email = email
        self.Description = description
        self.JoiningDate = joining_date


class Transaction(db.Model):
    __tablename__ = 'Transactions'
    Id = db.Column(db.Integer, primary_key=True)
    WalletId = db.Column(db.Integer, db.ForeignKey('Wallets.Id'))
    Type = db.Column(db.String(32))
    BuyAmount = db.Column(db.Float)
    BuyCur = db.Column(db.String(16))
    SellAmount = db.Column(db.Float)
    SellCur = db.Column(db.String(16))
    CommissionAmount = db.Column(db.Float)
    CommissionCur = db.Column(db.String(16))
    Description = db.Column(db.String(255))
    Date = db.Column(db.Date)

    def __init__(self, wallet_id, type, date,
                 buy_amount=None, buy_cur=None, sell_amount=None, sell_curr=None,
                 commission_amount=None, commission_curr=None, description=None):
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

# Resources


class Users(Resource):
    user_post_args = reqparse.RequestParser()

    def get(self):
        result = User.query.all()
        output = []
        for user in result:
            new_user = {"Username": user.Username}
            output.append(new_user)

        return jsonify(output)

    def post(self):
        today = date.today()
        args = self.user_post_args.parse_args()
        user = User(args.Username, args.Email, args.Description, today)
        db.session.add(user)
        db.session.commit()
        return {"message": "Done"}

    def __init__(self):
        self.user_post_args.add_argument("Username", type=str, help="Username", required=True)
        self.user_post_args.add_argument("Email", type=str, help="Email", required=True)
        self.user_post_args.add_argument("Description", type=str, required=False)


class Wallets(Resource):
    wallet_post_args = reqparse.RequestParser()

    def get(self):
        result = Wallet.query.all()
        output = []
        for wallet in result:
            new_wallet = {"Name": wallet.Name}
            output.append(new_wallet)

        return jsonify(output)

    def post(self):
        args = self.wallet_post_args.parse_args()
        wallet = Wallet(args.UserId, args.Name)
        db.session.add(wallet)
        db.session.commit()
        return {"message": "Done"}

    def __init__(self):
        self.wallet_post_args.add_argument("UserId", type=int, help="UserId", required=True)
        self.wallet_post_args.add_argument("Name", type=str, help="Name", required=True)


class Transactions(Resource):
    transaction_post_args = reqparse.RequestParser()

    def get(self):
        result = Transaction.query.all()
        output = []
        for transaction in result:
            new_transaction = {"Id": transaction.Id, "Type": transaction.Type}
            output.append(new_transaction)
        return jsonify(output)

    def post(self):
        args = self.transaction_post_args.parse_args()
        transaction = Transaction(
            args.WalletId, args.Type, args.Date, args.BuyAmount, args.BuyCur, args.SellAmount, args.SellCurr,
            args.CommissionAmount, args.CommissionCur, args.Description)
        db.session.add(transaction)
        db.session.commit()
        return {"message": "Done"}

    def __init__(self):
        self.transaction_post_args.add_argument("WalletId", type=int, help="WalletId", required=True)
        self.transaction_post_args.add_argument("Type", type=str, help="Type", required=True)
        self.transaction_post_args.add_argument("Date", type=str, help="Date", required=True)
        self.transaction_post_args.add_argument("BuyAmount", type=float, required=False)
        self.transaction_post_args.add_argument("BuyCur", type=str, required=False)
        self.transaction_post_args.add_argument("SellAmount", type=float, required=False)
        self.transaction_post_args.add_argument("SellCurr", type=str, required=False)
        self.transaction_post_args.add_argument("CommissionAmount", type=float, required=False)
        self.transaction_post_args.add_argument("CommissionCur", type=str, required=False)
        self.transaction_post_args.add_argument("Description", type=str, required=False)


class Aggregate(Resource):

    def patch(self, wallet_id):
        results = db.session.query(Transaction, Wallet).select_from(Wallet).join(Transaction).filter(Wallet.Id == wallet_id).all()

        for transaction, wallet in results:
            print(transaction.Type)
        return {"message": "Done"}
# API routs

api.add_resource(Users, "/users")
api.add_resource(Transactions, "/transactions")
api.add_resource(Wallets, "/wallets")
api.add_resource(Aggregate, "/aggregate/<int:wallet_id>")

if __name__ == "__main__":
    app.run(debug=True)
