""" main module to run crypto_portfolio"""
# core modules
import argparse
import logging
import yaml

# third-party modules

# self modules
from utils.common import setup_logging
from api import bittrex, bitfinex, coinbase


def main():
    """main method"""

    parser = argparse.ArgumentParser(description="Get your total worth of coins across exchanges")
    parser.add_argument("-f", default="settings/api_keys.yml",
                        help="File path for api keys")
    args = parser.parse_args()

    # load the logging configuration
    setup_logging()
    logger = logging.getLogger(__name__)
    # mute request log
    logging.getLogger("requests").setLevel(logging.WARNING)
    

    # load the api keys
    with open(args.f, 'r') as ymlfile:
        api_keys = yaml.load(ymlfile)

    # init total wallet
    total_value = 0.

    for exchange, auth in api_keys.items():
        if exchange == "bittrex":
            client = bittrex.Bittrex(auth['api_key'], auth['api_secret'])
        elif exchange == "bitfinex":
            client = bitfinex.Bitfinex(auth['api_key'], auth['api_secret'])
        elif exchange == "coinbase":
            client = coinbase.Coinbase(auth['api_key'], auth['api_secret'])

        value = client.get_wallet_value()
        logger.info("%s worth(USD):$%s" % (exchange, value))
        total_value = total_value + value

    logger.info("Total crpyto worth(usd):$%s" %total_value)

if __name__ == "__main__":
    main()



