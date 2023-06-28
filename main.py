import datetime
import os
import time

from toolbox import database
from toolbox import ticker_prices
from toolbox import ticker_retreival
from toolbox import ticker_price_analysis

storage_path = "/mnt/nvme1n1p1/"
database_path = os.path.join(storage_path, "database")

ticker_retreival.set_storage_path(database_path)
ticker_prices.set_storage_path(database_path)
ticker_price_analysis.set_storage_path(database_path)

days_to_refresh = 1


def main():

    ticker = "MSFT"
    print(f"Getting {ticker} historical data")
    start_time = time.time()
    # trend = ticker_prices.get_ticker_historical_trend(stock, cooldown=False, database_only=False)
    velocity_trend = ticker_price_analysis.get_acceleration(ticker, database_only=True)
    print(velocity_trend)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
