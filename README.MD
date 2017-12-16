# crypto_portfolio

crypto_portfolio is a tool that shows how much your precious metals are currently worth. It will connect across exchanges e.g. Bittrex, Bitfinex to get your coin balances and aggregate your total coin worth in USD. Currently, only Bittrex is supported.


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
2017-12-16 20:23:39,500 - api.bittrex - INFO - Retrieving Bittrex account balances...
2017-12-16 20:23:39,504 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTPS connection (1): bittrex.com
2017-12-16 20:23:39,943 - api.bittrex - INFO - [{'Available': 2000.0, 'Pending': 0.0, 'Currency': 'BTC', 'CryptoAddress': None, 'Balance': 123.0}]
2017-12-16 20:23:39,944 - api.coinmarketcap - INFO - Retrieving Coinmarketcap tickers...
2017-12-16 20:23:39,987 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTPS connection (1): api.coinmarketcap.com
2017-12-16 20:23:40,266 - __main__ - INFO - Total crpyto worth(usd):$1234.12345
```
## Logs
Logs are stored at log folder.
