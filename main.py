import datetime
import os
import time

import plotly.express as px

from toolbox import database
from toolbox import ticker_prices
from toolbox import ticker_retreival
from toolbox import ticker_price_analysis
from toolbox import ticker_plotter

storage_path = "/mnt/nvme1n1p1/"
database_path = os.path.join(storage_path, "database")

database.set_storage_path(database_path)
ticker_retreival.set_storage_path(database_path)
ticker_prices.set_storage_path(database_path)
ticker_price_analysis.set_storage_path(database_path)
ticker_plotter.set_storage_path(database_path)

days_to_refresh = 1


def main():

    ticker = "AMZN"
    print(f"Getting {ticker} historical data")
    start_time = time.time()

    start_date = datetime.datetime.now() - datetime.timedelta(days=31)
    trend = ticker_prices.get_ticker_historical_trend(ticker, cooldown=False, database_only=True, start_date=start_date)
    print("Getting trend data")
    # Create columns variable that does not contain the Date and Volume column
    #columns = trend.columns
    #columns = columns.drop("Volume")

    print("Plotting Trend")
    #trend_fig = ticker_plotter.get_figure(trend, columns, title=f"{ticker} Price")
    #trend_fig.write_image(f"{ticker}_trend.png")

    # Create a candlestick figure
    #candlestick_fig = ticker_plotter.get_candlestick_figure(trend, title=f"{ticker} Candlestick")
    #candlestick_fig.write_image(f"{ticker}_candlestick.png")

    # Get pct change of prices
    print("Getting Percent Change")
    pct_change = ticker_price_analysis.get_pct_change(trend)

    print("Plotting Percent Change")
    #pct_fig = ticker_plotter.get_figure(pct_change, columns, title=f"{ticker} Percent Change", yaxis_name="Percent Change")
    #pct_fig.write_image(f"{ticker}_pct.png")

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
