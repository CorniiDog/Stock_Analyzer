import os
import pandas as pd
from toolbox import database
from toolbox import ticker_prices
import plotly.express as px


def set_storage_path(database_path: str, make_dir=False):
    """
    Params
    ------
    database_path: str
        Path to the database
    make_dir: bool
        If True, create the directory if it does not exist

    Returns
    -------
    None

    Notes
    -----
    This function is used to set the path to the database. The database is a

    Examples
    --------
    from toolbox import ticker_price_analysis
    ticker_price_analysis.set_storage_path('~/Desktop/database', make_dir=True)
    """

    if make_dir:
        if not os.path.exists(database_path):
            os.makedirs(database_path)

    database.set_storage_path(database_path)
    ticker_prices.set_storage_path(database_path)


def get_figure(trend: pd.DataFrame, columns: list, title: str, yaxis_name: str = "Price ($)", key_name: str = "Type"):
    """
    Parameters
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

    Returns
    -------
    fig: plotly.graph_objects.Figure
        Plotly figure

    Notes
    -----
    This function is used to plot the trend of the data. The trend is a dataframe where the index is the date and the
    columns are the different types of data. The columns are the different types of data.

    Examples
    --------
    from toolbox import ticker_price_analysis
    from toolbox import ticker_prices
    ticker_price_analysis.set_storage_path('~/Desktop/database', make_dir=True)
    ticker_prices.set_storage_path('~/Desktop/database')

    trend = ticker_prices.get_ticker_historical_trend('AAPL')
    fig = ticker_price_analysis.get_figure(trend, ['Close', 'Open'], 'AAPL')
    fig.show()
    fig.write_image(f"AAPL_closing_price.png")
    """

    # First create Date column for the plot
    for index, row in trend.iterrows():
        trend.at[index, "Date"] = index

    return px.line(trend, x="Date", y=columns, title=title, color_discrete_sequence=px.colors.qualitative.Plotly,
                   labels={"value": yaxis_name, "variable": key_name})
