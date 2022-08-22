from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from ..entities.user import User
from ..entities.wallet import Wallet
from ..entities.entity import Session
from ..auth.auth import token_required


class Wallets(Resource):

    @token_required
    def get(self, user=None):
        session = Session()
        wallets = session.query(Wallet).filter_by(UserId=user.Id).all()
        session.close()

        wallets_list = []
        for wallet in wallets:
            wallets_list.append(wallet.json())

        print(wallets_list)

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
