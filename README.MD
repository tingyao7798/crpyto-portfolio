# crypto-portfolio

crypto-portfolio is a tool that shows how much your precious metals are currently worth. It will connect across exchanges e.g. Bittrex, Bitfinex to get your coin balances and aggregate your total coin worth in USD. 

## Supported Wallets
* Coinbase
* Bittrex
* Bitfinex

## WIP
* Binance
* Eth wallets on Etherscan.io
* Bitcoin wallets from Block.io

## Installation
```bash
pip install -r requirements.txt
```

## To Run
Update your api keys in settings/api_key.yaml file, you can create a new file using the template given
```python
python crpyto_portfolio.py -f settings/api_keys.yml
```

## Sample output
```bash
$ python crpyto_portfolio.py -f settings/api_keys.yml
he API clients available in this package are deprecated and will be no longer available in their current form starting with version 2.0!
2017-12-27 14:55:33,240 - __main__ - INFO - bitfinex worth(USD):$100.00
2017-12-27 14:55:33,501 - __main__ - INFO - bittrex worth(USD):$100.00
2017-12-27 14:55:33,887 - __main__ - INFO - coinbase worth(USD):$100.00
2017-12-27 14:55:33,887 - __main__ - INFO - Total crpyto worth(usd):$300.00
```
## Logs
Logs are stored at log folder.
