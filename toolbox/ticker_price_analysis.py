import os, datetime, requests, time
import pandas as pd
import cupy as cp
from toolbox import database
from toolbox import ticker_prices


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


def get_velocity_graph(ticker):
    # Get the data

    start_date = datetime.datetime(1900, 1, 1)
    today = datetime.datetime.today()

    df = ticker_prices.get_ticker_historical_trend(ticker, start_date, today)
    # Put the data into a cupy array
    cf = cp.array(df)
    print(cf)

#get_velocity_graph("MSFT")