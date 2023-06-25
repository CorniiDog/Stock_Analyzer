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


def get_ticker_historical_trend(ticker: str, start_date: datetime.datetime, end_date: datetime.datetime, historical_buffer_days = 1) -> pd.DataFrame:
    """
    Params
    ------
    ticker: str
        Ticker symbol
    start_date: datetime.datetime
        Start date
    end_date: datetime.datetime
        End date
    historical_buffer_days: int
        Number of days to subtract from the end date

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
    # If end date's day is today, subtract the historical buffer days'
    if end_date.date() == datetime.datetime.today().date():
        end_date = end_date - datetime.timedelta(days=historical_buffer_days)


    def get_trend_request(ticker, start, end, cooldown_counter=0, interval="1h"):
        time.sleep(3)
        try:
            trend = yf.download(ticker, start, end, interval=interval)
        except Exception as e:
            if "404" in str(e):
                print('404 error, returning None')
                return None
            else:
                print('Error, retrying in 5 seconds')
                time.sleep(5 * cooldown_counter)
                if cooldown_counter < 5:
                    return get_trend_request(start, end, cooldown_counter + 1, interval=interval)
                else:
                    print('Cooldown counter reached, returning None')
                    return None
        return trend

    def get_trend(ticker, start_date, end_date):
        start_end_dates = []
        pre_existing_trend = None
        while start_date < end_date:
            interval = "1h"

            # If the time delta is greater than 2 years, use 1d interval
            if (end_date - start_date).days > 365 * 2:
                interval = "1d"

            days = 365
            if (end_date - start_date).days < 365:
                days = (end_date - start_date).days

            if (end_date - start_date).days == 0:
                break

            start_end_dates.append((start_date, start_date + datetime.timedelta(days=days), interval))
            start_date = start_date + datetime.timedelta(days=days)
        for start, end, interval in start_end_dates:
            if end > end_date:
                end = end_date
            if pre_existing_trend is None:
                pre_existing_trend = get_trend_request(ticker, start, end, interval=interval)
            else:
                pre_existing_trend = pd.concat([pre_existing_trend, get_trend_request(ticker, start, end, interval=interval)])
            time.sleep(1)

        return pre_existing_trend

    pre_existing_trend = database.get(ticker + '_trend')
    if pre_existing_trend is None:
        pre_existing_trend = get_trend(ticker, start_date, end_date)
    else:
        # Get the last date in the pre-existing trend
        last_date = pre_existing_trend.index[-1]
        # Localize to the same timezone as the end date
        end_date_timezone = end_date.tzinfo
        last_date = last_date.replace(tzinfo=pytz.utc).astimezone(end_date_timezone)

        if last_date < end_date:
            pre_existing_trend = pd.concat([pre_existing_trend, get_trend(ticker, last_date, end_date)])

    database.save(ticker + '_trend', pre_existing_trend)
    # Print last item in the trend
    print(ticker, pre_existing_trend.tail(1))
    return pre_existing_trend

if __name__ == '__main__':
    date = '09/10/2019'
    datetime_object = datetime.datetime.strptime(date, '%m/%d/%Y')

    today = datetime.datetime.today()
    print(get_ticker_historical_trend('MSFT', datetime_object, today))