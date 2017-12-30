""" wrapper module that calls bitfinex api"""
# core modules
import logging

# third party modules
from bitex.api.REST import BitfinexREST


# self modules
from api.api import BaseApi

class Bitfinex(BaseApi):
    """ Bitfinex REST API class
    credits to https://github.com/nlsdfnbch/bitex
    """
    def __init__(self, key=None, secret=None):
        super().__init__(key, secret)

    def _get_balance(self):
        """ method to get balances from bitfinex
        Returns:
            wallet: list of dict e.g.
            [{'currency': 'btc', 'amount': '0.0',
              'available': '0.0', 'type': 'exchange'}]
        """
        logger = logging.getLogger(__name__)
        logger.debug("Retrieving Bitfinex account balances...")

        # init bitfinex client
        bf_client = BitfinexREST()
        # patch bitfinex load key method
        bf_client.key = self._key
        bf_client.secret = self._secret
        # Query a private (authenticated) endpoint
        resp = bf_client.query('POST', 'balances', authenticate=True)

        if resp.status_code == 200:
            logger.debug(resp.json())
            wallet = resp.json()
            return wallet
        else:
            logger.error("Failed to get Bittrex account balances!")

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
            if float(coin['amount']) > 0:
                wallet_dict.update({coin['currency'].upper(): float(coin['amount'])})

        # Fix for IOT not following the coinmarketcap symbol
        wallet_dict['MIOTA'] = wallet_dict.pop('IOT')

        return wallet_dict

    def get_wallet(self):
        """ method to return whatever is in the wallet
        Returns:
            wallet_dict: dict: float e.g.{'ETH':222}
        """
        wallet = self._format_wallet()
        return wallet







   