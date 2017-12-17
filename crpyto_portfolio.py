""" main module to run crypto_portfolio"""
# core modules
import argparse
import logging
import yaml

# third-party modules

# self modules
from utils.common import setup_logging
from api import bittrex, bitfinex


def main():
    """main method"""

    parser = argparse.ArgumentParser(description="Get your total worth of coins across exchanges")
    parser.add_argument("-f", default="settings/api_keys.yml",
                        help="File path for api keys")
    args = parser.parse_args()

    # load the logging configuration
    setup_logging()
    logger = logging.getLogger(__name__)

    # load the api keys
    with open(args.f, 'r') as ymlfile:
        api_keys = yaml.load(ymlfile)

    # init total wallet
    total_value = 0.

    for exchange, auth in api_keys.items():
        if exchange == "bittrex":
            bittrex_client = bittrex.Bittrex(auth['api_key'], auth['api_secret'])
            bitrex_value = bittrex_client.get_wallet_value()
            logger.info("Bitrex worth(USD):$%s" % bitrex_value)
            total_value = total_value + bitrex_value

        elif exchange == "bitfinex":
            bitfinex_client = bitfinex.Bitfinex(auth['api_key'], auth['api_secret'])
            bitfinex_value = bitfinex_client.get_wallet_value()
            logger.info("Bitrex worth(USD):$%s" % bitfinex_value)
            total_value = total_value + bitfinex_value

    logger.info("Total crpyto worth(usd):$%s" %total_value)

if __name__ == "__main__":
    main()



