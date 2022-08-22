from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from datetime import datetime

from ..entities.user import User
from ..entities.wallet import Wallet
from ..entities.entity import Session
from ..entities.transaction import Transaction
from ..auth.auth import token_required
from ..common.check_user import check_user


class Transactions(Resource):

    @token_required
    def get(self, user=None):
        session = Session()
        wallet_id = request.headers['wallet-id']
        if not check_user(user.Id, wallet_id):
            return {'message': 'It is not your wallet'}

        transactions = session.query(Transaction).filter_by(WalletId=wallet_id).all()
        session.close()

        transactions_list = []
        for transaction in transactions:
            transactions_list.append(transaction.json())

        return jsonify(transactions_list)

    @token_required
    def post(self, user=None):
        data = request.get_json()
        keys = data.keys()
        all_keys = ["wallet_id", "transaction_type", "date", "buy_amount", "buy_cur", "sell_amount", "sell_curr",
                    "commission_amount", "commission_curr", "description"]
        for key in all_keys:
            if key not in keys:
                data[key] = None

        if not data["wallet_id"] or not data["transaction_type"]:
            return {"message": "not enough data"}

        if not data["date"]:
            data["date"] = datetime.now()

        new_transaction = Transaction(
            wallet_id=data["wallet_id"],
            transaction_type=data["transaction_type"],
            date=data["date"],
            buy_amount=data["buy_amount"],
            buy_cur=data["buy_cur"],
            sell_amount=data["sell_amount"],
            sell_cur=data["sell_cur"],
            commission_amount=data["commission_amount"],
            commission_curr=data["commission_curr"],
            description=data["description"]
        )

        session = Session()
        session.add(new_transaction)
        session.commit()
        session.close()

        return {'message': 'transaction created'}
