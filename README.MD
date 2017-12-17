# crypto_portfolio

crypto_portfolio is a tool that shows how much your precious metals are currently worth. It will connect across exchanges e.g. Bittrex, Bitfinex to get your coin balances and aggregate your total coin worth in USD. 

Currently, Bittrex and Bitfinex are supported. 


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
The API clients available in this package are deprecated and will be no longer available in their current form starting with version 2.0!
2017-12-17 18:18:50,535 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTPS connection (1): bittrex.com
2017-12-17 18:18:51,174 - __main__ - INFO - Bitrex worth(USD):$100.00
2017-12-17 18:18:51,192 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTPS connection (1): api.bitfinex.com
2017-12-17 18:18:52,578 - __main__ - INFO - Bitrex worth(USD):$23.456
2017-12-17 18:18:52,578 - __main__ - INFO - Total crpyto worth(usd):$123.456
```
## Logs
Logs are stored at log folder.
