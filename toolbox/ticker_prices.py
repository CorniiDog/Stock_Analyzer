import os, datetime, requests, time
import yfinance as yf
import pandas as pd
import datetime
from toolbox import database
import pytz

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
    from toolbox import ticker_prices
    ticker_prices.set_storage_path('C:/Users/username/PycharmProjects/stock_analysis/database')
    """

    if make_dir:
        if not os.path.exists(database_path):
            os.makedirs(database_path)

    database.set_storage_path(database_path)


def _get_trend_request_(ticker, start, end, cooldown_counter=0, interval="1h", cooldown=True):
    if cooldown:
        time.sleep(3)
    try:
        trend = yf.download(ticker, start=start, end=end, interval=interval)
        trend.index = pd.to_datetime(trend.index, utc=True)
        trend.index = trend.index.tz_convert('America/New_York')
    except Exception as e:
        print(e)
        if "404" in str(e):
            print('404 error, returning None')
            return None
        else:
            print('Error, retrying in 5 seconds')
            time.sleep(5 * cooldown_counter)
            if cooldown_counter < 5:
                return _get_trend_request_(start, end, cooldown_counter + 1, interval=interval)
            else:
                print('Cooldown counter reached, returning None')
                return None
    return trend


def _get_trend_(ticker, start_date, end_date, cooldown=True):
    start_end_dates = []
    pre_existing_trend = None
    start_date_none = start_date is None
    if start_date_none:
        # Set to 5 years ago
        start_date = end_date - datetime.timedelta(days=365 * 5)
    while start_date < end_date:
        a = start_date+datetime.timedelta(days=365)
        interval = "1h"
        # If the time delta is greater than 2 years, use 1d interval
        if (end_date - start_date).days > 365 * 2-1:
            interval = "1d"
        days = 365
        if (end_date - start_date).days < days:
            start_end_dates.append((start_date, end_date, interval))
            break
        else:
            start_end_dates.append((start_date, start_date + datetime.timedelta(days=days), interval))
            start_date = start_date + datetime.timedelta(days=days)

    # Combine all dates with "1d" intervals
    new_start_end_dates = []
    earliest_start_date = None
    latest_end_date = None
    for i, value in enumerate(start_end_dates):
        # Find earliest date with "1d" interval
        if value[2] == "1d":
            if earliest_start_date is None:
                earliest_start_date = value[0]
            else:
                if value[0] < earliest_start_date:
                    earliest_start_date = value[0]
            # Find latest date with "1d" interval
            if latest_end_date is None:
                latest_end_date = value[1]
            else:
                if value[1] > latest_end_date:
                    latest_end_date = value[1]
    if start_date_none:
        earliest_start_date = None
    if latest_end_date is not None:
        new_start_end_dates.append((earliest_start_date, latest_end_date, "1d"))
    for i, value in enumerate(start_end_dates):
        if value[2] != "1d":
            new_start_end_dates.append(value)
    start_end_dates = new_start_end_dates
    for start, end, interval in start_end_dates:
        if end > end_date:
            end = end_date
        if pre_existing_trend is None:
            pre_existing_trend = _get_trend_request_(ticker, start, end, interval=interval, cooldown=cooldown)
            if pre_existing_trend is None:
                return None
        else:
            pre_existing_trend = pd.concat([pre_existing_trend, _get_trend_request_(ticker, start, end, interval=interval, cooldown=cooldown)])
    return pre_existing_trend

def get_ticker_historical_trend(ticker: str, start_date: datetime.datetime = None, end_date: datetime.datetime = None, cooldown=True, database_only=False) -> pd.DataFrame:
    """
    Params
    ------
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


    Returns
    -------
    pd.DataFrame
        Historical trend of the ticker

    Notes
    -----
    This function is used to get the historical trend of a ticker. The historical trend is stored in the database. If the
    historical trend is not in the database, it will be downloaded from Yahoo Finance and stored in the database.

    Examples
    --------
    from toolbox import ticker_prices
    import datetime
    date = '09/10/2019'
    datetime_object = datetime.datetime.strptime(date, '%m/%d/%Y')
    today = datetime.datetime.today()
    print(ticker_prices.get_ticker_historical_trend('MSFT', datetime_object, today))
    """

    # If end date is none, set it to today
    if end_date is None:
        end_date = datetime.datetime.today()

    # Set time zone to New York
    end_date = end_date.astimezone(pytz.timezone('America/New_York'))
    if start_date is not None:
        start_date = start_date.astimezone(pytz.timezone('America/New_York'))

    # If end date's day is today, subtract the historical buffer days'
    #if end_date.date() == datetime.datetime.today().date():
    #    end_date = end_date - datetime.timedelta(days=historical_buffer_days)





    pre_existing_trend = database.get(ticker + '_trend')
    if pre_existing_trend is None or len(pre_existing_trend.index) == 0:
        pre_existing_trend = _get_trend_(ticker, start_date, end_date, cooldown=cooldown)
        database.save(ticker + '_trend', pre_existing_trend)
    else:
        # Get the last date in the pre-existing trend
        last_date = pre_existing_trend.index[-1]
        # Localize to the same timezone as the end date

        # If the place is closed, set it to the previous day
        if end_date.hour < 9 or end_date.hour > 16:
            end_date = end_date - datetime.timedelta(days=1)

        # If the end date is during the weekend, set it to the previous Friday
        if end_date.weekday() == 5:
            end_date = end_date - datetime.timedelta(days=1)
        elif end_date.weekday() == 6:
            end_date = end_date - datetime.timedelta(days=2)

        if last_date < end_date and not database_only:
            trend = _get_trend_(ticker, last_date, end_date, cooldown=cooldown)
            if trend is None:
                return pre_existing_trend
            else:
                pre_existing_trend = pd.concat([pre_existing_trend, trend])

            database.save(ticker + '_trend', pre_existing_trend)


    # Get closest index to the end date
    end = pre_existing_trend.index.searchsorted(end_date)

    if start_date is not None:
        # Get closest index to the start date
        start = pre_existing_trend.index.searchsorted(start_date)

        pre_existing_trend = pre_existing_trend.iloc[start:end]
    else:
        pre_existing_trend = pre_existing_trend.iloc[:end]

    # Print last item in the trend
    return pre_existing_trend

if __name__ == '__main__':
    date = '09/10/2019'
    datetime_object = datetime.datetime.strptime(date, '%m/%d/%Y')

    today = datetime.datetime.today()
    print(get_ticker_historical_trend('MSFT', datetime_object, today))