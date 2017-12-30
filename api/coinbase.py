""" wrapper module that calls coinbase api"""
# core modules
import logging

# third party modules
from coinbase.wallet.client import Client

# self modules
from api.api import BaseApi

class Coinbase(BaseApi):
    """ wrapper class on top of Bittrex
    Init:
        api_key: string
        api_secret: string
    """
    def __init__(self, key=None, secret=None):
        super().__init__(key, secret)

    def _get_balance(self):
        """ method to get coinbase balances
        Returns:
            wallet: list of dict e.g.
                  [{"balance": {
                    "amount": "0.00058000",
                    "currency": "BTC"
                    },
                    "created_at": "2017-07-11T13:27:36Z",
                    "currency": "BTC",
                    "id": "3abaaa8a-d9e4-58d5-9143-df3ca8a3b67f",
                    "name": "BTC Wallet",
                    "native_balance": {
                        "amount": "12.81",
                        "currency": "SGD"
                    },
                    "primary": true,
                    "resource": "account",
                    "resource_path": "/v2/accounts/3abaaa8a-d9e4-58d5-9143-df3ca8a3b67f",
                    "type": "wallet",
                    "updated_at": "2017-12-13T09:31:31Z"}]
        """

        logger = logging.getLogger(__name__)
        logger.debug("Retrieving Coinbase account balances...")

        client = Client(self._key, self._secret)
        resp = client.get_accounts().data

        return resp

    def _format_wallet(self):
        """ method to format wallet
        Args:
            wallet: list of dict
        Returns:
            wallet_dict: dict: float e.g.{'iot':222}
        """
        wallet = self._get_balance()

        # init wallet dict
        wallet_dict = {}
        for coin in wallet:
            amount = float(coin['balance']['amount'])
            if amount > 0.:
                wallet_dict.update({coin['balance']['currency'].upper(): amount})

        return wallet_dict

    def get_wallet(self):
        """ method to return whatever is in the wallet
        Returns:
            wallet_dict: dict: float e.g.{'ETH':222}
        """
        wallet = self._format_wallet()
        return wallet



    