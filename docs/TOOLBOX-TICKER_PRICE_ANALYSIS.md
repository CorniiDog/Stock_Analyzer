[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import ticker_price_analysis`

Alternative Import Statement: `from toolbox.ticker_price_analysis import *`

# >  function set_storage_path #

### [def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_price_analysis.py#L8) 

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

### [def diff(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L39) 

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

# >  function get_pct_change #

### [def get_pct_change(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L74) 

Note

```python
    This function is used to get the percent change between the price of each datetime
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
    pct_change_df: pd.DataFrame
        Dataframe with datetime index and columns of percent change in prices
```

Example

```python
    from toolbox import ticker_price_analysis
    import pandas as pd
    df = pd.DataFrame({'price': [1, 2, 3, 4, 5]}, index=pd.date_range('2020-01-01', periods=5, freq='1min'))
    pct_change_trend = ticker_price_analysis.get_pct_change(df)
    print(pct_change_trend)
```

# >  function get_velocity #

### [def get_velocity(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L110) 

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

### [def get_acceleration(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L151) 

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

### [def get_jerk(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L192) 

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

# >  function get_pct_change_velocity #

### [def get_pct_change_velocity(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L233) 

Note

```python
    This function is used to get the percent change velocity of the ticker
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
    pct_change_velocity_df: pd.DataFrame
        Dataframe with datetime index and columns of percent change velocity
```

Example

```python
    from toolbox import ticker_price_analysis
    pct_change_velocity_df = ticker_price_analysis.get_pct_change_velocity('AAPL')
    print(pct_change_velocity_df)
```

# >  function get_pct_change_acceleration #

### [def get_pct_change_acceleration(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L274) 

Note

```python
    This function is used to get the percent change acceleration of the ticker
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
    pct_change_acceleration_df: pd.DataFrame
        Dataframe with datetime index and columns of percent change acceleration
```

Example

```python
    from toolbox import ticker_price_analysis
    pct_change_acceleration_df = ticker_price_analysis.get_pct_change_acceleration('AAPL')
    print(pct_change_acceleration_df)
```

# >  function get_pct_change_jerk #

### [def get_pct_change_jerk(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L311) 

Note

```python
    This function is used to get the percent change jerk of the ticker
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
    pct_change_jerk_df: pd.DataFrame
        Dataframe with datetime index and columns of percent change jerk
```

Example

```python
    from toolbox import ticker_price_analysis
    pct_change_jerk_df = ticker_price_analysis.get_pct_change_jerk('AAPL')
    print(pct_change_jerk_df)
```

# >  function interpolate #

### [def interpolate(trend, resample='D', create_dates_column=False):](./../toolbox/ticker_price_analysis.py#L348) 

Note

```python
    This function is used to interpolate the dataframe. It will interpolate the dataframe based upon the resample.
    This function is an alias for toolbox.ticker_prices.interpolate
```

Param

```python
ters
    ----------
    trend: pd.DataFrame
        Dataframe to interpolate
    resample: str
        Resample the dataframe to this frequency
        'H' = Hourly
        'D' = Daily
```

Return

```python
    trend: pd.DataFrame
        Interpolated dataframe
```

Example

```python
    from toolbox import ticker_prices
    df = ticker_prices.get_ticker_historical_trend('AAPL', start_date=datetime.datetime(2020, 1, 1), end_date=datetime.datetime(2020, 1, 2))
    df = ticker_prices.interpolate(df)
    print(df)
```

# >  function average #

### [def average(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L378) 

Note

```python
    This function is used to get the average of the dataframe
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
```

Return

```python
    average_df: pd.DataFrame
        Dataframe with datetime index and columns of average
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    average_df = ticker_price_analysis.average(df)
    print(average_df)
```

# >  function standard_deviation #

### [def standard_deviation(df: pd.DataFrame, sample=True):](./../toolbox/ticker_price_analysis.py#L413) 

Note

```python
    This function is used to get the standard deviation of the dataframe
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
    sample: bool
        If True, use sample standard deviation, else use population standard deviation
```

Return

```python
    standard_deviation_df: pd.DataFrame
        Dataframe with datetime index and columns of standard deviation
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    standard_deviation_df = ticker_price_analysis.standard_deviation(df)
    print(standard_deviation_df)
```

# >  function max #

### [def max(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L450) 

Note

```python
    This function is used to get the max of the dataframe
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
```

Return

```python
    max_df: pd.DataFrame
        Dataframe with datetime index and columns of max
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    max_df = ticker_price_analysis.max(df)
    print(max_df)
```

# >  function min #

### [def min(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L485) 

Note

```python
    This function is used to get the min of the dataframe
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
```

Return

```python
    min_df: pd.DataFrame
        Dataframe with datetime index and columns of min
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    min_df = ticker_price_analysis.min(df)
    print(min_df)
```

# >  function skew #

### [def skew(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L520) 

Note

```python
    This function is used to get the skew of the dataframe.
    For each skew variable:
    skew = 0: normally distributed
    skew < 0: more weight in the right tail of the distribution
    skew > 0: more weight in the left tail of the distribution

    For instance, a skew of -0.35 means that there is more weight in the right tail of the distribution.
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
```

Return

```python
    skew_df: pd.DataFrame
        Dataframe with datetime index and columns of skew.
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    skew_df = ticker_price_analysis.skew(df)
    print(skew_df)
```

# >  function rolling_mean #

### [def rolling_mean(df: pd.DataFrame, window:int = 12):](./../toolbox/ticker_price_analysis.py#L562) 

Note

```python
    This function is used to get the rolling mean of the dataframe
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
    window: int
        The number of periods to use for calculating the statistic
```

Return

```python
    rolling_mean_df: pd.DataFrame
        Dataframe with datetime index and columns of rolling mean
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    rolling_mean_df = ticker_price_analysis.rolling_mean(df)
    print(rolling_mean_df)
```

# >  function rolling_std #

### [def rolling_std(df: pd.DataFrame, window:int = 12):](./../toolbox/ticker_price_analysis.py#L590) 

Note

```python
    This function is used to get the rolling standard deviation of the dataframe
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
    window: int
        The number of periods to use for calculating the statistic
```

Return

```python
    rolling_std_df: pd.DataFrame
        Dataframe with datetime index and columns of rolling standard deviation
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    rolling_std_df = ticker_price_analysis.rolling_std(df)
    print(rolling_std_df)
```

# >  function df_log #

### [def df_log(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L618) 

Note

```python
    This function is used to get the log of the dataframe
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
```

Return

```python
    df_log: pd.DataFrame
        Dataframe with datetime index and columns of log
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    df_log = ticker_price_analysis.df_log(df)
    print(df_log)
```

# >  function get_stationary_trend #

### [def get_stationary_trend(df: pd.DataFrame, window: int = 12):](./../toolbox/ticker_price_analysis.py#L645) 

Note

```python
    This function is used to get the stationary trend of the dataframe
```

Param

```python
ters
    ----------
    df: pd.DataFrame
        Dataframe with datetime index and columns of percent change
    window: int
        The number of periods to use for calculating the statistic
```

Return

```python
    stationary_trend_df: pd.DataFrame
        Dataframe with datetime index and columns of stationary trend
```

Example

```python
    from toolbox import ticker_price_analysis
    df = ticker_prices.get_ticker_historical_trend('AAPL')
    stationary_trend_df = ticker_price_analysis.get_stationary_trend(df)
    print(stationary_trend_df)
```

