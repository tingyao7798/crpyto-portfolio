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
    # init cur_address to store already processed eth addresses

    cur_address = []

    for exchange, auth in api_keys.items():
        if exchange == "bittrex":
            # instantiate Bittrex class
            client = bittrex.Bittrex(auth['key'], auth['secret'])

            # get wallet value
            wallet = client.get_wallet()
            value = client.get_wallet_value(wallet)
            logger.info("%s worth(USD):$%s" % (exchange, value))
            total_value = total_value + value

        elif exchange == "bitfinex":
            # instantiate Bitfinex class
            client = bitfinex.Bitfinex(auth['key'], auth['secret'])

            # get wallet value
            wallet = client.get_wallet()
            value = client.get_wallet_value(wallet)
            logger.info("%s worth(USD):$%s" % (exchange, value))
            total_value = total_value + value

        elif exchange == "coinbase":
            # instantiate Coinbase class
            client = coinbase.Coinbase(auth['key'], auth['secret'])

            # get wallet value
            wallet = client.get_wallet()
            value = client.get_wallet_value(wallet)
            logger.info("%s worth(USD):$%s" % (exchange, value))
            total_value = total_value + value

        elif exchange == "etherscan":

            # process each eth address
            for acc in auth['account']:
                if acc not in cur_address:

                    # save acc to cur_address
                    cur_address.append(acc)

                    # instantiate Etherscan class
                    client = etherscan.Etherscan(auth['key'],
                                                 acc)

                    # get wallet value
                    wallet = client.get_wallet()
                    value = client.get_wallet_value(wallet)
                    logger.info("Ethereum address %s worth(USD):$%s" % (acc['address'], value))
                    total_value = total_value + value

    logger.info("Total crpyto worth(usd):$%s" %total_value)

if __name__ == "__main__":
    main()



