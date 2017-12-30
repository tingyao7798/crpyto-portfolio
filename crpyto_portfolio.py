""" main module to run crypto_portfolio"""
# core modules
import argparse
import logging
import yaml

# third-party modules

# self modules
from utils.common import setup_logging
from api import bittrex, bitfinex, coinbase, etherscan


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

    for account, auth in api_keys.items():
        if account == "bittrex":
            client = bittrex.Bittrex(auth['key'], auth['secret'])
        elif account == "bitfinex":
            client = bitfinex.Bitfinex(auth['key'], auth['secret'])
        elif account == "coinbase":
            client = coinbase.Coinbase(auth['key'], auth['secret'])
        elif account == "etherscan":
            client = etherscan.Etherscan(auth['key'], auth['account'], auth['contract_address'])

        wallet = client.get_wallet()
        value = client.get_wallet_value(wallet)
        logger.info("%s worth(USD):$%s" % (account, value))
        total_value = total_value + value

    logger.info("Total crpyto worth(usd):$%s" %total_value)

if __name__ == "__main__":
    main()



