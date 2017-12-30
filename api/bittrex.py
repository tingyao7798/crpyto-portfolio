""" wrapper module that calls bittrex api"""
# core modules
import logging

# third party modules
import bittrex

# self modules
from api.api import BaseApi

class Bittrex(BaseApi):
    """ wrapper class on top of Bittrex
    Init:
        api_key: string
        api_secret: string
    """
    def __init__(self, key=None, secret=None):
        super().__init__(key, secret)

    def _get_balance(self):
        """ method to get bittrex balances
        Returns:
            wallet: list of dict e.g. 
                  [{'Available': 8011.86885714,
                    'Balance': 8011.86885714,
                    'CryptoAddress': None,
                    'Currency': 'ADA',
                    'Pending': 0.0}]
        """
        logger = logging.getLogger(__name__)
        logger.debug("Retrieving Bittrex account balances...")

        client = bittrex.Bittrex(self._key, self._secret)
        resp = client.get_balances()

        if resp['success']:
            logger.debug(resp['result'])
            wallet = resp['result']
            return wallet
        else:
            logging.error("Failed to get Bittrex account balances!")

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
            if coin['Balance'] > 0:
                wallet_dict.update({coin['Currency'].upper():coin['Balance']})

        return wallet_dict

    def get_wallet(self):
        """ method to return whatever is in the wallet
        Returns:
            wallet_dict: dict: float e.g.{'ETH':222}
        """
        wallet = self._format_wallet()
        return wallet








    