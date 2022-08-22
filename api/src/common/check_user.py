from ..entities.wallet import Wallet
from ..entities.entity import Session


def check_user(user_id, wallet_id):
    session = Session()
    wallets = session.query(Wallet).filter_by(UserId=user_id)
    session.commit()
    for wallet in wallets:
        if wallet.Id == wallet_id:
            session.close()
            return True

    session.close()
    return False
