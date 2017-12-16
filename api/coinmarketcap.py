""" wrapper module that calls coinmarketcap api"""
# core modules
import logging

# third party modules
import coinmarketcap

# self modules


class Coinmarketcap:
    """ wrapper class on top of coinmarketcap
    """
    def get_ticker(self):
        """ method to get coinmarketcap tickers
        Args: None
        Returns:
            ticker_resp: list of dict, each dict contains each coin's
            data e.g. [{'24h_volume_usd': '2119330000.0',
                        'available_supply': '96373480.0',
                        'cached': False,
                        'id': 'ethereum',
                        'last_updated': '1513423457',
                        'market_cap_usd': '67667289797.0',
                        'max_supply': None,
                        'name': 'Ethereum',
                        'percent_change_1h': '0.71',
                        'percent_change_24h': '7.6',
                        'percent_change_7d': '44.6',
                        'price_btc': '0.0390053',
                        'price_usd': '702.136',
                        'rank': '2',
                        'symbol': 'ETH',
                        'total_supply': '96373480.0'}]
        """
        logger = logging.getLogger(__name__)
        logger.info("Retrieving Coinmarketcap tickers...")
        client = coinmarketcap.Market()
        ticker_resp = client.ticker()

        return ticker_resp

    def get_ticker_prices(self):
        """ method to process ticker response to get a dictionary of symbols
        and its prices(usd)
        Args:
            ticker_resp: list of dict
        Returns:
            cm_prices: dict e.g. {'1ST': '0.626248'}
        """
        # get ticker resp
        ticker_resp = self.get_ticker()

        cm_prices = {}
        for coin in ticker_resp:
            cm_prices.update({coin['symbol']: coin['price_usd']})

        return cm_prices







    