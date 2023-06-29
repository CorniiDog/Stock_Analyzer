[Back to README.md](/README.md)

# DOCUMENTATION TABLE OF CONTENTS #

This is the documentation for the project Stock_Analyzer.

## INSTRUCTIONS.md ##

[0. HOW TO USE THIS TEMPLATE](/docs/INSTRUCTIONS.md#0-how-to-use-this-template)

[1. HOW TO INSTALL ANACONDA](/docs/INSTRUCTIONS.md#1-how-to-install-anaconda)

[2. HOW TO CREATE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#2-how-to-create-conda-environment)

[3. HOW TO CONNECT INTERPRETER TO JETBRAINS GATEWAY](/docs/INSTRUCTIONS.md#3-how-to-connect-interpreter-to-jetbrains-gateway)

[4. HOW TO INSTALL REQUIREMENTS](/docs/INSTRUCTIONS.md#4-how-to-install-requirements)

[5. HOW TO INSTALL SERVICE](/docs/INSTRUCTIONS.md#5-how-to-install-service)

[6. HOW TO INSTALL SELENIUM AND CHROME](/docs/INSTRUCTIONS.md#6-how-to-install-selenium-and-chrome)

[A. HOW TO REMOVE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#a-how-to-remove-conda-environment)

[B. HOW TO UNINSTALL SERVICE](/docs/INSTRUCTIONS.md#b-how-to-uninstall-service)

# Documentation Notebooks #

 - [Plotting](/documentation/Plotting.ipynb)

# API #


<details>
<summary>

## Documentation For [main.py](/docs/MAIN.md)

</summary>


 <details>
<summary>

### > [function main](/docs/MAIN.md#function-main) 



</summary>

[def main():](./../main.py#L25) 



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/ticker_price_analysis.py](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md)

</summary>


 <details>
<summary>

### > [function set_storage_path](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-set_storage_path) 



</summary>

[def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_price_analysis.py#L7) 

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



</details>


 <details>
<summary>

### > [function diff](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-diff) 



</summary>

[def diff(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L38) 

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



</details>


 <details>
<summary>

### > [function get_pct_change](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-get_pct_change) 



</summary>

[def get_pct_change(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L73) 

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



</details>


 <details>
<summary>

### > [function get_velocity](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-get_velocity) 



</summary>

[def get_velocity(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L109) 

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



</details>


 <details>
<summary>

### > [function get_acceleration](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-get_acceleration) 



</summary>

[def get_acceleration(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L150) 

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



</details>


 <details>
<summary>

### > [function get_jerk](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-get_jerk) 



</summary>

[def get_jerk(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L191) 

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



</details>


 <details>
<summary>

### > [function get_pct_change_velocity](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-get_pct_change_velocity) 



</summary>

[def get_pct_change_velocity(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L231) 

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



</details>


 <details>
<summary>

### > [function get_pct_change_acceleration](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-get_pct_change_acceleration) 



</summary>

[def get_pct_change_acceleration(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L272) 

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



</details>


 <details>
<summary>

### > [function get_pct_change_jerk](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-get_pct_change_jerk) 



</summary>

[def get_pct_change_jerk(ticker: str, start_date=None, end_date=None, cooldown=True, database_only=False, interval="1d"):](./../toolbox/ticker_price_analysis.py#L309) 

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



</details>


 <details>
<summary>

### > [function average](/docs/TOOLBOX-TICKER_PRICE_ANALYSIS.md#function-average) 



</summary>

[def average(df: pd.DataFrame):](./../toolbox/ticker_price_analysis.py#L346) 

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



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/web_scraping_utility.py](/docs/TOOLBOX-WEB_SCRAPING_UTILITY.md)

</summary>


 <details>
<summary>

### > [function test_headless](/docs/TOOLBOX-WEB_SCRAPING_UTILITY.md#function-test_headless) 



</summary>

[def test_headless(website: str, screenshot_path, screen_width: int = 1920, screen_height: int = 1080):](./../toolbox/web_scraping_utility.py#L9) 

Note


```python
    The screenshot will be saved as a .png file
    This function is built just to test the headless option of selenium.
```

Param


```python
ters
    ----------
    website: str
        The website to take a screenshot of
    screenshot_path: str
        The path to save the screenshot to
    screen_width: int
        The width of the screen to take the screenshot of
    screen_height: int
        The height of the screen to take the screenshot of
```

Return


```python
    None
```

Example


```python
    from toolbox import web_scraping_utility
    import os
    current_dir = os.getcwd()

    screenshot_path = os.path.join(current_dir, 'test')
    web_scraping_utility.test_headless('https://www.youtube.com', screenshot_path)
```



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/ticker_retreival.py](/docs/TOOLBOX-TICKER_RETREIVAL.md)

</summary>


 <details>
<summary>

### > [function set_storage_path](/docs/TOOLBOX-TICKER_RETREIVAL.md#function-set_storage_path) 



</summary>

[def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_retreival.py#L8) 

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



</details>


 <details>
<summary>

### > [function get_tickers](/docs/TOOLBOX-TICKER_RETREIVAL.md#function-get_tickers) 



</summary>

[def get_tickers(days_reset_frequency=7, request_fresh=False):](./../toolbox/ticker_retreival.py#L37) 

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



</details>


 <details>
<summary>

### > [function get_rejected_tickers](/docs/TOOLBOX-TICKER_RETREIVAL.md#function-get_rejected_tickers) 



</summary>

[def get_rejected_tickers(days_reset_frequency=7, request_fresh=False):](./../toolbox/ticker_retreival.py#L112) 

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



</details>


 <details>
<summary>

### > [function get_ticker_information](/docs/TOOLBOX-TICKER_RETREIVAL.md#function-get_ticker_information) 



</summary>

[def get_ticker_information(symbol: str, days_reset_frequency=14, request_fresh=False, cooldown_counter=0):](./../toolbox/ticker_retreival.py#L151) 

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



</details>


 <details>
<summary>

### > [function get_all_ticker_information](/docs/TOOLBOX-TICKER_RETREIVAL.md#function-get_all_ticker_information) 



</summary>

[def get_all_ticker_information(days_reset_frequency=1, request_fresh=False):](./../toolbox/ticker_retreival.py#L232) 

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



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/ticker_prices.py](/docs/TOOLBOX-TICKER_PRICES.md)

</summary>


 <details>
<summary>

### > [function set_storage_path](/docs/TOOLBOX-TICKER_PRICES.md#function-set_storage_path) 



</summary>

[def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_prices.py#L8) 

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



</details>


 <details>
<summary>

### > [function get_trend_request](/docs/TOOLBOX-TICKER_PRICES.md#function-get_trend_request) 



</summary>

[def _get_trend_request_(ticker, start, end, cooldown_counter=0, interval="1h", cooldown=True):](./../toolbox/ticker_prices.py#L38) 



</details>


 <details>
<summary>

### > [function get_trend](/docs/TOOLBOX-TICKER_PRICES.md#function-get_trend) 



</summary>

[def _get_trend_(ticker, start_date, end_date, cooldown=True):](./../toolbox/ticker_prices.py#L61) 



</details>


 <details>
<summary>

### > [function get_ticker_historical_trend](/docs/TOOLBOX-TICKER_PRICES.md#function-get_ticker_historical_trend) 



</summary>

[def get_ticker_historical_trend(ticker: str, start_date: datetime.datetime = None, end_date: datetime.datetime = None, cooldown = True, database_only=False, interval: str = "1h") -> pd.DataFrame:](./../toolbox/ticker_prices.py#L120) 

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
    interval: str
        Interval of the historical trend. If None, it will be set to "1d" if the time delta is greater than 2 years,
        otherwise it will be set to "1h"
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



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/ticker_plotter.py](/docs/TOOLBOX-TICKER_PLOTTER.md)

</summary>


 <details>
<summary>

### > [function set_storage_path](/docs/TOOLBOX-TICKER_PLOTTER.md#function-set_storage_path) 



</summary>

[def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_plotter.py#L9) 

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



</details>


 <details>
<summary>

### > [function create_date_index](/docs/TOOLBOX-TICKER_PLOTTER.md#function-create_date_index) 



</summary>

[def create_date_index_(trend):](./../toolbox/ticker_plotter.py#L40) 



</details>


 <details>
<summary>

### > [function get_figure](/docs/TOOLBOX-TICKER_PLOTTER.md#function-get_figure) 



</summary>

[def get_figure(trend: pd.DataFrame, columns: list, title: str, yaxis_name: str = "Price ($)", key_name: str = "Type"):](./../toolbox/ticker_plotter.py#L53) 

Note


```python
    This function is used to plot the trend of the data. The trend is a dataframe where the index is the date and the
    columns are the different types of data. The columns are the different types of data.
```

Param


```python
ters
    ----------
    trend: pd.DataFrame
        Dataframe containing the trend

    columns: list
        List of columns to plot

    title: str
        Title of the plot

    yaxis_name: str
        Name of the y-axis

    key_name: str
        Name of the key
```

Return


```python
    fig: plotly.graph_objects.Figure
        Plotly figure
```

Example


```python
    from toolbox import ticker_price_analysis
    from toolbox import ticker_prices
    ticker_price_analysis.set_storage_path('~/Desktop/database', make_dir=True)
    ticker_prices.set_storage_path('~/Desktop/database')

    trend = ticker_prices.get_ticker_historical_trend('AAPL')
    fig = ticker_price_analysis.get_figure(trend, ['Close', 'Open'], 'AAPL')
    fig.show()
    fig.write_image(f"AAPL_trend.png")
```



</details>


 <details>
<summary>

### > [function get_candlestick_figure](/docs/TOOLBOX-TICKER_PLOTTER.md#function-get_candlestick_figure) 



</summary>

[def get_candlestick_figure(trend: pd.DataFrame, title: str, yaxis_name: str = "Price ($)"):](./../toolbox/ticker_plotter.py#L102) 

Note


```python
    This function is used to plot the trend of the data. The trend is a dataframe where the index is the date and the
    columns are the different types of data. The columns are the different types of data.
```

Param


```python
ters
    ----------
    trend: pd.DataFrame
        Dataframe containing the trend

    title: str
        Title of the plot

    yaxis_name: str
        Name of the y-axis
```

Return


```python
    fig: plotly.graph_objects.Figure
        Plotly figure
```

Example


```python
    from toolbox import ticker_price_analysis
    from toolbox import ticker_prices
    ticker_price_analysis.set_storage_path('~/Desktop/database', make_dir=True)
    ticker_prices.set_storage_path('~/Desktop/database')

    trend = ticker_prices.get_ticker_historical_trend('AAPL')
    fig = ticker_price_analysis.get_candlestick_figure(trend, 'AAPL')
    fig.show()
    fig.write_image(f"AAPL_candlestick.png")
```



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/queue_local.py](/docs/TOOLBOX-QUEUE_LOCAL.md)

</summary>


 <details>
<summary>

### > [class Queue](/docs/TOOLBOX-QUEUE_LOCAL.md#class-queue) 



</summary>

[class Queue:](./../toolbox/queue_local.py#L2) 

Note


```python
    A queue is a data structure that follows the First In First Out (FIFO) principle.
    This means that the first item added to the queue will be the first item removed from the queue.
    A queue can be implemented using a list or a linked list.
```

Param


```python
    queue_list: list
        The list to initialize the queue with
    max_size: int
        The maximum size of the queue
```

Example


```python
    queue = Queue([1, 2, 3, 4, 5], 10)

    a = queue.dequeue()
    print(a)
```

Reference


```python
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
```




 <details>
<summary>

### >  > [function Queue.init](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueinit) 



</summary>

[def __init__(self, queue_list: list = None, max_size: int = None):](./../toolbox/queue_local.py#L30) 

Note


```python
        If the queue_list is not None, then the queue will be initialized with the list
        If the max_size is not None, then the queue will be initialized with the max_size
```

Param


```python
        queue_list: list
            The list to initialize the queue with
        max_size: int
            The maximum size of the queue
```

Return


```python
        None
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], 10)

        a = queue.dequeue()
        print(a)
```



</details>


 <details>
<summary>

### >  > [function Queue.enqueue](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueenqueue) 



</summary>

[def enqueue(self, item):](./../toolbox/queue_local.py#L61) 

Note


```python
        Adds the item to the end of the queue
```

Param


```python
        item: any
            The item to add to the queue
```

Return


```python
        None
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.dequeue](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuedequeue) 



</summary>

[def dequeue(self):](./../toolbox/queue_local.py#L90) 

Note


```python
        Removes the first item from the queue
```

Param


```python
        None
```

Return


```python
        item: any
            The item that was removed from the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.dequeue()
        print(a)
```



</details>


 <details>
<summary>

### >  > [function Queue.size](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuesize) 



</summary>

[def size(self) -> int:](./../toolbox/queue_local.py#L118) 

Note


```python
        Returns the size of the queue
```

Param


```python
        None
```

Return


```python
        size: int
            The size of the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        print(queue.size())
```



</details>


 <details>
<summary>

### >  > [function Queue.is_empty](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueis_empty) 



</summary>

[def is_empty(self) -> bool:](./../toolbox/queue_local.py#L146) 

Note


```python
        Returns True if the queue is empty, False otherwise
```

Param


```python
        None
```

Return


```python
        is_empty: bool
            True if the queue is empty, False otherwise
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(queue.is_empty())
```



</details>


 <details>
<summary>

### >  > [function Queue.peek](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuepeek) 



</summary>

[def peek(self):](./../toolbox/queue_local.py#L173) 

Note


```python
        Returns the first item in the queue without removing it
```

Param


```python
        None
```

Return


```python
        item: any
            The first item in the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.peek()
        print(a)
```



</details>


 <details>
<summary>

### >  > [function Queue.get_list](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueget_list) 



</summary>

[def get_list(self):](./../toolbox/queue_local.py#L201) 

Note


```python
        Returns the list of items in the queue
```

Param


```python
        None
```

Return


```python
        list: list
            The list of items in the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.get_list()
        print(a)
```



</details>


 <details>
<summary>

### >  > [function Queue.len](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuelen) 



</summary>

[def __len__(self):](./../toolbox/queue_local.py#L230) 

Note


```python
        Returns the size of the queue
```

Param


```python
        None
```

Return


```python
        size: int
            The size of the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(len(queue))
```



</details>


 <details>
<summary>

### >  > [function Queue.copy](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuecopy) 



</summary>

[def copy(self):](./../toolbox/queue_local.py#L256) 

Note


```python
        Returns a copy of the queue
```

Param


```python
        None
```

Return


```python
        new_queue: Queue
            A copy of the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.copy](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuecopy) 



</summary>

[def __copy__(self):](./../toolbox/queue_local.py#L288) 

Note


```python
        Returns a copy of the queue
```

Param


```python
        None
```

Return


```python
        new_queue: Queue
            A copy of the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.eq](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueeq) 



</summary>

[def __eq__(self, other):](./../toolbox/queue_local.py#L317) 

Note


```python
        Returns True if the queues are equal, False otherwise
```

Param


```python
        other: Queue
            The other queue to compare to
```

Return


```python
        is_equal: bool
            True if the queues are equal, False otherwise
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue == other)
```



</details>


 <details>
<summary>

### >  > [function Queue.ne](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuene) 



</summary>

[def __ne__(self, other):](./../toolbox/queue_local.py#L348) 

Note


```python
        Returns True if the queues are not equal, False otherwise
```

Param


```python
        other: Queue
            The other queue to compare to
```

Return


```python
        is_not_equal: bool
            True if the queues are not equal, False otherwise
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue != other)
```



</details>


 <details>
<summary>

### >  > [function Queue.getitem](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuegetitem) 



</summary>

[def __getitem__(self, index):](./../toolbox/queue_local.py#L373) 

Note


```python
        Returns the item at the given index
```

Param


```python
        index: int
            The index of the item to get
```

Return


```python
        item: any
            The item at the given index
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue[2])
```



</details>


 <details>
<summary>

### >  > [function Queue.setitem](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuesetitem) 



</summary>

[def __setitem__(self, index, value):](./../toolbox/queue_local.py#L397) 

Note


```python
        Sets the item at the given index to the given value
```

Param


```python
        index: int
            The index of the item to set
        value: any
            The value to set the item to
```

Return


```python
        None
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue[2] = 10
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.delitem](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuedelitem) 



</summary>

[def __delitem__(self, index):](./../toolbox/queue_local.py#L423) 

Note


```python
        Deletes the item at the given index
```

Param


```python
        index: int
            The index of the item to delete
```

Return


```python
        None
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        del queue[2]
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.iter](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueiter) 



</summary>

[def __iter__(self):](./../toolbox/queue_local.py#L447) 

Note


```python
        Returns an iterator for the queue
```

Param


```python
        None
```

Return


```python
        iter: iter
            An iterator for the queue
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in queue:
            print(item)
```



</details>


 <details>
<summary>

### >  > [function Queue.reversed](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuereversed) 



</summary>

[def __reversed__(self):](./../toolbox/queue_local.py#L471) 

Note


```python
        Returns an iterator for the queue in reverse order
```

Param


```python
        None
```

Return


```python
        reversed: iter
            An iterator for the queue in reverse order
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in reversed(queue):
            print(item)
```



</details>


 <details>
<summary>

### >  > [function Queue.contains](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuecontains) 



</summary>

[def __contains__(self, item):](./../toolbox/queue_local.py#L495) 

Note


```python
        Returns True if the item is in the queue, False otherwise
```

Param


```python
        item: any
            The item to check for
```

Return


```python
        is_in: bool
            True if the item is in the queue, False otherwise
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(1 in queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.add](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueadd) 



</summary>

[def __add__(self, other):](./../toolbox/queue_local.py#L519) 

Note


```python
        Returns a new queue with the items from both queues
```

Param


```python
        other: Queue
            The other queue to add to this queue
```

Return


```python
        new_queue: Queue
            A new queue with the items from both queues
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        new_queue = queue + other
        print(new_queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.iadd](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueiadd) 



</summary>

[def __iadd__(self, other):](./../toolbox/queue_local.py#L550) 

Note


```python
        Returns this queue with the items from both queues
```

Param


```python
        other: Queue
            The other queue to add to this queue
```

Return


```python
        self: Queue
            This queue with the items from both queues
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        queue += other
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.mul](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuemul) 



</summary>

[def __mul__(self, other):](./../toolbox/queue_local.py#L578) 

Note


```python
        Returns a new queue with the items from this queue repeated the given number of times
```

Param


```python
        other: int
            The number of times to repeat the queue
```

Return


```python
        new_queue: Queue
            A new queue with the items from this queue repeated the given number of times
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        new_queue = queue * 3
        print(new_queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.imul](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueimul) 



</summary>

[def __imul__(self, other):](./../toolbox/queue_local.py#L607) 

Note


```python
        Returns this queue with the items from this queue repeated the given number of times
```

Param


```python
        other: int
            The number of times to repeat the queue
```

Return


```python
        self: Queue
            This queue with the items from this queue repeated the given number of times
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue *= 3
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.str](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuestr) 



</summary>

[def __str__(self):](./../toolbox/queue_local.py#L636) 

Note


```python
        Returns a string representation of the queue
```

Param


```python
        None
```

Return


```python
        string: str
            A string representation of the queue
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue)
```



</details>

</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/database.py](/docs/TOOLBOX-DATABASE.md)

</summary>


 <details>
<summary>

### > [function set_storage_path](/docs/TOOLBOX-DATABASE.md#function-set_storage_path) 



</summary>

[def set_storage_path(path):](./../toolbox/database.py#L9) 

Note


```python
    This function is used to set the path to the folder where the database files will be stored
```

Param


```python
ters
    ----------
    path : str
        The path to the folder where the database files will be stored
```

Return


```python
    None
        This function does not return anything
```

Example


```python
    set_storage_path('C:/Users/JohnDoe/Documents/MyDatabase')
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function slugify](/docs/TOOLBOX-DATABASE.md#function-slugify) 



</summary>

[def slugify(value, allow_unicode=False):](./../toolbox/database.py#L41) 

Note


```python
    This function is used to slugify strings, which basically means to remove all special characters and replace them with dashes.
    This is useful for creating file names from strings.
```

Param


```python
ters
    ----------
    value : str
        The string to be slugified
    allow_unicode : bool
        Whether or not to allow unicode characters
```

Return


```python
    str
        The slugified string
```

Example


```python
    a = slugify('Hello World')
```

Reference


```python
    https://github.com/django/django/blob/master/django/utils/text.py
```



</details>


 <details>
<summary>

### > [function get](/docs/TOOLBOX-DATABASE.md#function-get) 



</summary>

[def get(name: str):](./../toolbox/database.py#L77) 

Note


```python
    This function is used to load objects from the database folder
```

Param


```python
ters
    ----------
    name : str
        The name of the file to be loaded
```

Return


```python
    object or None
        The object loaded from the file, could be anything
```

Example


```python
    spreadsheet_data = get('spreadsheet_people')
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function get_modified_date](/docs/TOOLBOX-DATABASE.md#function-get_modified_date) 



</summary>

[def get_modified_date(name: str):](./../toolbox/database.py#L112) 

Note


```python
    This function is used to get the last modified date of a file in the database folder
```

Param


```python
ters
    ----------
    name : str
        The name of the file to be loaded
```

Return


```python
    datetime.datetime or None
        The datetime object of the last modified date
```

Example


```python
    date = get_modified_date('spreadsheet_people')
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function save](/docs/TOOLBOX-DATABASE.md#function-save) 



</summary>

[def save(name: str, data: any) -> None:](./../toolbox/database.py#L146) 

Note


```python
    This function is used to save objects to the database folder
```

Param


```python
ters
    ----------
    name : str
        The name of the file to be saved
    data : any
        The data to be saved
```

Return


```python
    None
        This function does not return anything
```

Example


```python
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function delete_database](/docs/TOOLBOX-DATABASE.md#function-delete_database) 



</summary>

[def delete_database(name: str) -> object:](./../toolbox/database.py#L182) 

Note


```python
    This function is used to delete objects from the database folder
```

Param


```python
ters
    ----------
    name : str
        The name of the file to be deleted
```

Return


```python
    object or None
        The object loaded from the file, could be anything
```

Example


```python
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)

    delete_database('spreadsheet_people')
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function save_key](/docs/TOOLBOX-DATABASE.md#function-save_key) 



</summary>

[def save_key(platform: str, key: str, override: bool = False) -> None:](./../toolbox/database.py#L220) 

Note


```python
    This function is used to save keys in a secure location
```

Param


```python
ters
    ----------
    platform: str
        The name of the platform to be saved (e.g. 'google')
    key: str
        The key to be saved (e.g. '<google_api_key>')
    override: bool
        Whether or not to override the key if it already exists
```

Return


```python
    None
        This function does not return anything
```

Example


```python
    save_key('google', '<google_api_key>')
```

Reference


```python
    https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```



</details>


 <details>
<summary>

### > [function load_key](/docs/TOOLBOX-DATABASE.md#function-load_key) 



</summary>

[def load_key(platform: str) -> str:](./../toolbox/database.py#L266) 

Note


```python
        This function is used to load keys from a secure location
```

Param


```python
ters
        ----------
        platform: str
            The key to be loaded (e.g. '<google_api_key>')
```

Return


```python
        str or None
            This function returns the key if it exists, otherwise it returns None
```

Example


```python
        key = load_key('google')
```

Reference


```python
        https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```



</details>

<br></details>

