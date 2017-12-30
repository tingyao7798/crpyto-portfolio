"""base class for the other api classes"""
# core modules
import logging

# third party modules

# self modules
from api.coinmarketcap import Coinmarketcap

class BaseApi:
    """
    Base API client class
    """
    def __init__(self, key=None, secret=None):
        self._key = key
        self._secret = secret

    def get_wallet_value(self, wallet):
        """ method to get wallet value
        Args:
            wallet: list of dict
        Returns:
            wallet_value: float
        """
        # get latest prices from coinmarketcap
        cmc_client = Coinmarketcap()
        ticker_prices = cmc_client.get_ticker_prices()

        wallet_value = 0.

        for coin, amt in wallet.items():
            price_usd = float(ticker_prices[coin])
            wallet_value = wallet_value + (amt * price_usd)

        return wallet_value
