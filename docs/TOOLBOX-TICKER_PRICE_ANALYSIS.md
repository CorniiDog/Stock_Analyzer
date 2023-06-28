[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import ticker_price_analysis`

Alternative Import Statement: `from toolbox.ticker_price_analysis import *`

# >  function set_storage_path #

### [def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_price_analysis.py#L7) 

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
    from toolbox import ticker_price_analysis
    ticker_price_analysis.set_storage_path('~/Desktop/database', make_dir=True)
```

# >  function diff #

### [def diff(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L38) 

Note

```python
    This function is used to get the difference between the price of each datetime
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of prices
```

Return

```python
    diff_df: pd.DataFrame
        Dataframe with datetime index and columns of differences in prices
```

Example

```python
    from toolbox import ticker_price_analysis
    import pandas as pd
    df = pd.DataFrame({'price': [1, 2, 3, 4, 5]}, index=pd.date_range('2020-01-01', periods=5, freq='1min'))
    velocity_df = ticker_price_analysis.diff(df)
    print(velocity_df)
```

# >  function get_velocity #

### [def get_velocity(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False):](./../toolbox/ticker_price_analysis.py#L74) 

Note

```python
    This function is used to get the velocity of the ticker
```

Param

```python
ters
    ----------
    ticker: str
        Ticker symbol

    start_date: datetime.datetime
        Start date of the data

    end_date: datetime.datetime
        End date of the data

    cooldown: bool
        If True, wait 1 second between each request to the API

    database_only: bool
        If True, only use the database, do not make any requests to the API
```

Return

```python
    velocity_df: pd.DataFrame
        Dataframe with datetime index and columns of velocity
```

Example

```python
    from toolbox import ticker_price_analysis
    velocity_df = ticker_price_analysis.get_velocity('AAPL')
    print(velocity_df)
```

# >  function get_acceleration #

### [def get_acceleration(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False):](./../toolbox/ticker_price_analysis.py#L115) 

Note

```python
    This function is used to get the acceleration of the ticker
```

Param

```python
ters
    ----------
    ticker: str
        Ticker symbol

    start_date: datetime.datetime
        Start date of the data

    end_date: datetime.datetime
        End date of the data

    cooldown: bool
        If True, wait 1 second between each request to the API

    database_only: bool
        If True, only use the database, do not make any requests to the API
```

Return

```python
    acceleration_df: pd.DataFrame
        Dataframe with datetime index and columns of acceleration
```

Example

```python
    from toolbox import ticker_price_analysis
    acceleration_df = ticker_price_analysis.get_acceleration('AAPL')
    print(acceleration_df)
```

# >  function get_jerk #

### [def get_jerk(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False):](./../toolbox/ticker_price_analysis.py#L156) 

Note

```python
    This function is used to get the jerk of the ticker
```

Param

```python
ters
    ----------
    ticker: str
        Ticker symbol

    start_date: datetime.datetime
        Start date of the data

    end_date: datetime.datetime
        End date of the data

    cooldown: bool
        If True, wait 1 second between each request to the API

    database_only: bool
        If True, only use the database, do not make any requests to the API
```

Return

```python
    jerk_df: pd.DataFrame
        Dataframe with datetime index and columns of jerk
```

Example

```python
    from toolbox import ticker_price_analysis
    jerk_df = ticker_price_analysis.get_jerk('AAPL')
    print(jerk_df)
```

