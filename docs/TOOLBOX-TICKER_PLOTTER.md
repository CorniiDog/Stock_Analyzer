[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import ticker_plotter`

Alternative Import Statement: `from toolbox.ticker_plotter import *`

# >  function set_storage_path #

### [def set_storage_path(database_path: str, make_dir=False):](./../toolbox/ticker_plotter.py#L8) 

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

# >  function get_figure #

### [def get_figure(trend: pd.DataFrame, columns: list, title: str, yaxis_name: str = "Price ($)", key_name: str = "Type"):](./../toolbox/ticker_plotter.py#L39) 

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
    fig.write_image(f"AAPL_closing_price.png")
```

