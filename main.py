import datetime
import os
import time

from toolbox import database
from toolbox import ticker_prices
from toolbox import ticker_retreival

storage_path = "/mnt/nvme1n1p1/"

database_path = os.path.join(storage_path, "database")
ticker_retreival.set_storage_path(database_path)
ticker_prices.set_storage_path(database_path)

days_to_refresh = 1
delete_trends = False # Set to true to delete all trends

def get_ticker_prices(ticker):
    # Get the ticker info. This will be obtained as yf.Ticker(symbol).info
    # Get the ticker info. This will be obtained as yf.Ticker(symbol).info
    ticker_info = ticker_retreival.get_ticker_information(ticker)
    # Get firstTradeDateEpochUtc
    if "firstTradeDateEpochUtc" in ticker_info:
        first_trade_date = ticker_info["firstTradeDateEpochUtc"]
    else:
        # We set to 1960 if we don't have the first trade date
        first_trade_date = None

    # Get the start date
    start_date = datetime.datetime.fromtimestamp(first_trade_date)

    trend = ticker_prices.get_ticker_historical_trend(ticker, start_date)

    return trend


def main():

    if delete_trends:
        approved_tickers = ticker_retreival.get_tickers()
        # Remove all ticker_trends
        for ticker in approved_tickers:
            try:
                database.delete_database(ticker + "_trend")
                print(ticker)
            except:
                pass
        database.save("price_last_ticker", None)
        print("done")
        return

    last_updated = 0
    while True:
        now = time.time()
        # If it is a new day, update the database
        if now - last_updated > 86400 * days_to_refresh:
            print("New Day, updating database")

            approved_tickers = ticker_retreival.get_tickers()
            for i, ticker in enumerate(approved_tickers):
                last_ticker = database.get("price_last_ticker")
                if last_ticker is not None:
                    if ticker != last_ticker:
                        continue
                print(ticker)
                get_ticker_prices(ticker)

                if i < len(approved_tickers) - 1:
                    database.save("price_last_ticker", approved_tickers[i + 1])

            database.save("price_last_ticker", None)

            last_updated = now
        time.sleep(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

