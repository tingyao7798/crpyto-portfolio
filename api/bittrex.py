""" wrapper module that calls bittrex api"""
# core modules
import logging

# third party modules
import bittrex

# self modules
from api.coinmarketcap import Coinmarketcap

class Bittrex:
    """ wrapper class on top of Bittrex
    Init:
        api_key: string
        api_secret: string
    """
    def __init__(self, api_key, api_secret):
        self.__api_key = api_key
        self.__api_secret = api_secret

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

        client = bittrex.Bittrex(self.__api_key, self.__api_secret)
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

    def get_wallet_value(self):
        """ method to get wallet value
        Args:
            wallet: list of dict
        Returns:
            wallet_value: float
        """
        # get wallet balance
        wallet = self. _format_wallet()

        # get latest prices from coinmarketcap
        cmc_client = Coinmarketcap()
        ticker_prices = cmc_client.get_ticker_prices()

        wallet_value = 0.

        for coin, amt in wallet.items():
            price_usd = float(ticker_prices[coin])
            wallet_value = wallet_value + (amt * price_usd)

        return wallet_value






    