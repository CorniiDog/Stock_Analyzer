[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import ticker_retreival`

Alternative Import Statement: `from toolbox.ticker_retreival import *`

# >  function set_storage_path #

### [def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_retreival.py#L8) 

Note

```python
    This function is used to set the path to the database. The database is a
```

Param

```python
    database_path: str
        Path to the database
    make_dir: bool
        If True, create the directory if it does not exist
```

Return

```python
    None
```

Example

```python
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
```

# >  function get_tickers #

### [def get_tickers(days_reset_frequency=7, request_fresh=False):](./../toolbox/ticker_retreival.py#L37) 

Note

```python
    This function is used to get the list of tickers. The tickers are saved in the database. If the tickers are older
```

Param

```python
    days_reset_frequency: int
        Number of days before the tickers are reset, to avoid making too many API calls

    request_fresh: bool
        If True, then the tickers are requested fresh from the API, regardless of the last update time
```

Return

```python
    tickers: list
        List of tickers
```

Example

```python
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    tickers = ticker_retreival.get_tickers()
```

Reference

```python
    https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b
```

# >  function get_rejected_tickers #

### [def get_rejected_tickers(days_reset_frequency=7, request_fresh=False):](./../toolbox/ticker_retreival.py#L112) 

Note

```python
    This function is used to get the list of rejected tickers.
    W = When Issued, or can be arrested for fraud
    R = Rights Issue
    P = “First Preferred Issue”. Preferred stocks are a separate entity.
    Q = Bankruptcy
```

Param

```python
    days_reset_frequency: int
        Number of days before the tickers are reset, to avoid making too many API calls

    request_fresh: bool
        If True, then the tickers are requested fresh from the API, regardless of the last update time
```

Return

```python
    rejected_tickers: list
        List of rejected tickers
```

Example

```python
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    rejected_tickers = ticker_retreival.get_rejected_tickers()
```

Reference

```python
    https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b
```

# >  function get_ticker_information #

### [def get_ticker_information(symbol: str, days_reset_frequency=14, request_fresh=False, cooldown_counter=0):](./../toolbox/ticker_retreival.py#L151) 

Note

```python
    This function is used to get the information for a given ticker. The information is saved in the database. If the
```

Param

```python
    symbol: str
        Ticker symbol

    days_reset_frequency: int
        Number of days before the tickers are reset, to avoid making too many API calls

    request_fresh: bool
        If True, then the tickers are requested fresh from the API, regardless of the last update time
```

Return

```python
    stock_info: dict
        Dictionary of stock information
```

Example

```python
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    stock_info = ticker_retreival.get_ticker_information('MSFT')
    name = stock_info['shortName']
    website = stock_info['website']
    description = stock_info['longBusinessSummary']
```

# >  function get_all_ticker_information #

### [def get_all_ticker_information(days_reset_frequency=1, request_fresh=False):](./../toolbox/ticker_retreival.py#L232) 

Note

```python
    This function is used to get the information for all tickers. The information is saved in the database. If the
```

Param

```python
    days_reset_frequency: int
        Number of days before the tickers are reset, to avoid making too many API calls

    request_fresh: bool
        If True, then the tickers are requested fresh from the API, regardless of the last update time
```

Return

```python
    all_info: dict
        Dictionary of stock information for all tickers
```

Example

```python
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    all_info = ticker_retreival.get_all_ticker_information()
    print(all_info['MSFT']['shortName'])
```

