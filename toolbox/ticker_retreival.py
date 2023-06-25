import os, datetime, requests, time
from toolbox import database
import yahoo_fin.stock_info as si
import yfinance as yf
import pandas as pd


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
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    """
    if make_dir:
        if not os.path.exists(database_path):
            os.makedirs(database_path)

    database.set_storage_path(database_path)


def get_tickers(days_reset_frequency=7, request_fresh=False):
    """
    Params
    ------
    days_reset_frequency: int
        Number of days before the tickers are reset, to avoid making too many API calls

    request_fresh: bool
        If True, then the tickers are requested fresh from the API, regardless of the last update time

    Returns
    -------
    tickers: list
        List of tickers

    Reference
    ---------
    https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b

    Notes
    -----
    This function is used to get the list of tickers. The tickers are saved in the database. If the tickers are older

    Examples
    --------
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    tickers = ticker_retreival.get_tickers()
    """
    # Get time since last update
    last_update = database.get_modified_date('tickers')
    if last_update is None:
        last_update = datetime.datetime(2000, 1, 1)

    current_datetime = datetime.datetime.now()

    # Days since last update
    days_since_last_update = (current_datetime - last_update).days

    # If within 7 days, then return the tickers
    if days_since_last_update < days_reset_frequency and not request_fresh:
        return database.get('tickers')

    # Else, update the tickers
    # Reference: https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b
    df1 = pd.DataFrame(si.tickers_sp500())
    df2 = pd.DataFrame(si.tickers_nasdaq())
    df3 = pd.DataFrame(si.tickers_dow())
    df4 = pd.DataFrame(si.tickers_other())

    # We convert to a list and then to a set to remove duplicates
    tickers = list(set(list(df1[0]) + list(df2[0]) + list(df3[0]) + list(df4[0])))
    tickers.sort()

    # Remove non-alphanumeric characters
    tickers = [x for x in tickers if x.isalnum()]

    approved_tickers = []
    rejected_tickers = []
    my_list = ['W', 'R', 'P', 'Q']
    for ticker in tickers:
        if len(ticker) > 4 and ticker[-1] in my_list:
            rejected_tickers.append(ticker)
        else:
            approved_tickers.append(ticker)

    # Save to database
    database.save("tickers", approved_tickers)

    # Save rejected tickers
    database.save("rejected_tickers", rejected_tickers)

    return tickers


def get_rejected_tickers(days_reset_frequency=7, request_fresh=False):
    """
    Params
    ------
    days_reset_frequency: int
        Number of days before the tickers are reset, to avoid making too many API calls

    request_fresh: bool
        If True, then the tickers are requested fresh from the API, regardless of the last update time


    Returns
    -------
    rejected_tickers: list
        List of rejected tickers


    Notes
    -----
    This function is used to get the list of rejected tickers.
    W = When Issued, or can be arrested for fraud
    R = Rights Issue
    P = “First Preferred Issue”. Preferred stocks are a separate entity.
    Q = Bankruptcy

    Reference
    ---------
    https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b

    Examples
    --------
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    rejected_tickers = ticker_retreival.get_rejected_tickers()
    """
    get_tickers(days_reset_frequency, request_fresh)
    return database.get('rejected_tickers')


def get_ticker_information(symbol: str, days_reset_frequency=14, request_fresh=False, cooldown_counter=0):
    """
    Params
    ------
    symbol: str
        Ticker symbol

    days_reset_frequency: int
        Number of days before the tickers are reset, to avoid making too many API calls

    request_fresh: bool
        If True, then the tickers are requested fresh from the API, regardless of the last update time

    Returns
    -------
    stock_info: dict
        Dictionary of stock information

    Notes
    -----
    This function is used to get the information for a given ticker. The information is saved in the database. If the

    Examples
    --------
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    stock_info = ticker_retreival.get_ticker_information('MSFT')
    name = stock_info['shortName']
    website = stock_info['website']
    description = stock_info['longBusinessSummary']
    """

    last_update = database.get_modified_date(symbol + "_info")
    if last_update is None:
        last_update = datetime.datetime(2000, 1, 1)

    current_datetime = datetime.datetime.now()

    # Days since last update
    days_since_last_update = (current_datetime - last_update).days

    # If within 7 days, then return the tickers
    if days_since_last_update < days_reset_frequency and not request_fresh:
        return database.get(symbol + "_info")

    try:
        time.sleep(5)
        stock_info = yf.Ticker(symbol).info
    except Exception as e:
        # If 404 error, then the ticker is not found
        if '404' in str(e):
            print("404 Not Found for " + symbol)
            # Try to get the information from the database
            try:
                print("Trying to get the information from the database for " + symbol)
                stock_info = database.get(symbol + "_info")
                if stock_info is not None:
                    return stock_info
            finally:
                pass
            return None

        print(e)
        if cooldown_counter < 5:
            print("Cooldown counter: " + str(cooldown_counter) + " of 5 for " + symbol)
            time.sleep(60*cooldown_counter)
            return get_ticker_information(symbol, days_reset_frequency, request_fresh, cooldown_counter + 1)
        else:
            # See if we already have the information
            try:
                print("As last resort, trying to get the information from the database for " + symbol)
                stock_info = database.get(symbol + "_info")
                if stock_info is not None:
                    return stock_info
            finally:
                pass
            return None
    database.save(symbol + "_info", stock_info)
    return stock_info


def get_all_ticker_information(days_reset_frequency=1, request_fresh=False):
    """
    Params
    ------
    days_reset_frequency: int
        Number of days before the tickers are reset, to avoid making too many API calls

    request_fresh: bool
        If True, then the tickers are requested fresh from the API, regardless of the last update time

    Returns
    -------
    all_info: dict
        Dictionary of stock information for all tickers

    Notes
    -----
    This function is used to get the information for all tickers. The information is saved in the database. If the

    Examples
    --------
    from toolbox import ticker_retreival
    ticker_retreival.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    all_info = ticker_retreival.get_all_ticker_information()
    print(all_info['MSFT']['shortName'])
    """

    last_update = database.get_modified_date('all_ticker_info')
    if last_update is None:
        last_update = datetime.datetime(2000, 1, 1)

    current_datetime = datetime.datetime.now()

    # Days since last update
    days_since_last_update = (current_datetime - last_update).days

    # If within 1 day, then return the tickers
    if days_since_last_update < days_reset_frequency and not request_fresh:
        return database.get('all_ticker_info')

    tickers = get_tickers()

    # get information for all tickers
    all_info = database.get('all_ticker_info')
    if all_info is None:
        all_info = {}

    current_ticker = database.get("ticker_info_current_ticker")

    for i in range(len(tickers)):
        ticker = tickers[i]

        if current_ticker is None:
            current_ticker = i
            database.save("ticker_info_current_ticker", current_ticker)
        else:
            if i < current_ticker:
                continue
            else:
                if current_ticker % 10 == 0:
                    database.save("ticker_info_current_ticker", i)

        info = get_ticker_information(ticker)
        if info is None:
            print("Could not get information for " + ticker)
        else:
            print("Got information for " + ticker)

        all_info[ticker] = info

    # Set current ticker back to 0
    database.save("ticker_info_current_ticker", 0)

    database.save('all_ticker_info', all_info)

    return all_info
