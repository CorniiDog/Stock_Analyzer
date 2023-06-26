[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import ticker_prices`

Alternative Import Statement: `from toolbox.ticker_prices import *`

# >  function set_storage_path #

### [def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_prices.py#L8) 

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
    from toolbox import ticker_prices
    ticker_prices.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
```

# >  function get_trend_request #

### [def _get_trend_request_(ticker, start, end, cooldown_counter=0, interval="1h", cooldown=True):](./../toolbox/ticker_prices.py#L38) 

# >  function get_trend #

### [def _get_trend_(ticker, start_date, end_date, cooldown=True):](./../toolbox/ticker_prices.py#L61) 

# >  function get_ticker_historical_trend #

### [def get_ticker_historical_trend(ticker: str, start_date: datetime.datetime = None, end_date: datetime.datetime = None, cooldown=True, database_only=False) -> pd.DataFrame:](./../toolbox/ticker_prices.py#L120) 

Note

```python
    This function is used to get the historical trend of a ticker. The historical trend is stored in the database. If the
    historical trend is not in the database, it will be downloaded from Yahoo Finance and stored in the database.
```

Param

```python
    ticker: str
        Ticker symbol
    start_date: datetime.datetime
        Start date
    end_date: datetime.datetime
        End date
    cooldown: bool
        If True, wait 3 seconds between requests
    database_only: bool
        If True, only get the historical trend from the database.
        Setting it to True will not download the historical trend from Yahoo Finance,
        but it is faster to retrieve the historical trend from the database.
```

Return

```python
    pd.DataFrame
        Historical trend of the ticker
```

Example

```python
    from toolbox import ticker_prices
    import datetime
    date = '09/10/2019'
    datetime_object = datetime.datetime.strptime(date, '%m/%d/%Y')
    today = datetime.datetime.today()
    print(ticker_prices.get_ticker_historical_trend('MSFT', datetime_object, today))
```

