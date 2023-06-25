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

# >  function get_ticker_historical_trend #

### [def get_ticker_historical_trend(ticker: str, start_date: datetime.datetime, end_date: datetime.datetime, historical_buffer_days = 1) -> pd.DataFrame:](./../toolbox/ticker_prices.py#L38) 

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
    historical_buffer_days: int
        Number of days to subtract from the end date
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


 <details>
<summary>

#### Functions and Classes

</summary>

# >  >  function get_ticker_historical_trend.get_trend_request #

### [def get_trend_request(ticker, start, end, cooldown_counter=0, interval="1h"):](./../toolbox/ticker_prices.py#L75) 

# >  >  function get_ticker_historical_trend.get_trend #

### [def get_trend(ticker, start_date, end_date):](./../toolbox/ticker_prices.py#L93) 

</details>

