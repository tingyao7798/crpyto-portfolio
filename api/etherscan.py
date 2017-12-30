""" wrapper module that calls etherscan api"""
# core modules
import logging
import math

# third party modules
import requests

# self modules
from api.api import BaseApi

class Etherscan(BaseApi):
    """ etherscan REST API class
    """
    # Constants
    PREFIX = "https://api.etherscan.io/api?"
    MODULE = "module=account"
    ACTION = "&action="
    CONTRACT_ADDRESS = '&contractaddress='
    ADDRESS = '&address='
    API_KEY = '&apikey='
    TAG = '&tag='

    def __init__(self, key, account, tokens=None):
        self._key = key
        self.address = str(account)
        self.tokens = tokens
        self.http = requests.session()

    def _build_url(self, action, contract_address=None):
        """ method to construct url for api call"""
        if action == 'balance':
            params = [self.PREFIX, self.MODULE, self.ACTION, action,
                      self.ADDRESS, self.address, self.TAG, 'latest',
                      self.API_KEY, self._key]

        elif action == "tokenbalance":
            params = [self.PREFIX, self.MODULE, self.ACTION, action,
                      self.CONTRACT_ADDRESS, contract_address,
                      self.ADDRESS, self.address, self.TAG, 'latest',
                      self.API_KEY, self._key]

        url = ''.join(params)
        return url


    def _get_balance(self):
        """ method to get balances from bitfinex
        Returns:
            wallet: list of dict e.g.
            [{'currency': 'btc', 'amount': '0.0',
              'available': '0.0', 'type': 'exchange'}]
        """
        wallet = {"ETH": 0}
        logger = logging.getLogger(__name__)

        # Query etherscan api for etheruem balance
        logger.debug("Retrieving Ethereum account balance from Etherscan...")
        url = self._build_url("balance")
        resp = self.http.get(url)

        if resp.status_code == 200:
            wallet["ETH"] = float(resp.json()['result']) * math.pow(10, -18)
        else:
            logger.error(resp.json()['message'])

        # Query etherscan api for erc token balance
        logger.debug("Retrieving ERC20 token balance from Etherscan...")
        for tok in self.tokens:
            tok = list(tok.items())[0]
            url = self._build_url("tokenbalance", tok[1])
            resp = self.http.get(url)

            if resp.status_code == 200:
                wallet[tok[0]] = float(resp.json()['result']) * pow(10, -18)
            else:
                logger.error(resp.json()['message'])

        return wallet

    def get_wallet(self):
        """ method to return whatever is in the wallet
        Returns:
            wallet_dict: dict: float e.g.{'ETH':222}
        """
        wallet = self._get_balance()
        return wallet





   