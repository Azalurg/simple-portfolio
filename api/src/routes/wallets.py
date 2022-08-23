from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from datetime import datetime

from ..entities.user import User
from ..entities.wallet import Wallet
from ..entities.entity import Session
from ..entities.transaction import Transaction
from ..auth.auth import token_required
from ..common.check_user import check_user


class Wallets(Resource):

    @token_required
    def get(self, user=None):
        session = Session()
        wallets = session.query(Wallet).filter_by(UserId=user.Id).all()
        session.close()

        wallets_list = []
        for wallet in wallets:
            wallets_list.append(wallet.json())

        return jsonify(wallets_list)

    @token_required
    def post(self, user=None):
        data = request.get_json()

        if not data["name"]:
            return {'message': 'name is required'}

        new_wallet = Wallet(
            user_id=user.Id,
            name=data["name"]
        )

        session = Session()
        session.add(new_wallet)
        session.commit()
        session.close()

        return {'message': 'wallet created successfully'}

    @token_required
    def patch(self, user=None):
        wallet_id = request.get_json()['wallet_id']
        if not check_user(user.Id, wallet_id):
            return {'message': 'It is not your wallet'}
        session = Session()
        transactions = session.query(Transaction).filter_by(WalletId=wallet_id).all()
        transactions_list = []
        for transaction in transactions:
            transactions_list.append(transaction.json())
        sorted_transactions = sorted(transactions_list, key=lambda t: datetime.strptime(t["Date"], '%y-%m-%d'))
        state = {}
        wrong = []
        for t in sorted_transactions:

            if t["Type"] == "Add":
                if type(t['BuyAmount']) == float and type(t['BuyCur']) == str:
                    state.setdefault(t['BuyCur'], 0)
                    state[t['BuyCur']] += (t['BuyAmount'])
                else:
                    wrong.append(t['Id'])
            elif t["Type"] == "Remove":
                if type(t['SellAmount']) == float and type(t['SellCur']) == str:
                    state.setdefault(t['SellCur'], 0)
                    state[t['SellCur']] -= (t['SellAmount'])
                else:
                    wrong.append(t['Id'])
            elif t["Type"] in ["Buy", "Sell", "Transfer"]:
                if type(t['BuyAmount']) == float and type(t['BuyCur']) == str and type(
                        t['SellAmount']) == float and type(
                        t['SellCur']) == str:
                    state.setdefault(t['BuyCur'], 0)
                    state[t['BuyCur']] += (t['BuyAmount'])
                    state.setdefault(t['SellCur'], 0)
                    state[t['SellCur']] -= (t['SellAmount'])
                else:
                    wrong.append(t['Id'])
            else:
                wrong.append(t['Id'])
        session.close()

        return {"state": state, "wrong": wrong}
