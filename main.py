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

    start_date = None #datetime.datetime.now() - datetime.timedelta(days=365*3)
    trend = ticker_prices.get_ticker_historical_trend(ticker, cooldown=False, database_only=False, start_date=start_date)

    # Interpolate missing values
    trend = ticker_price_analysis.interpolate(trend)

    columns = trend.columns
    columns = columns.drop("Volume")

    # Show trend
    trend_fig = ticker_plotter.get_figure(trend, columns, title=f"{ticker} Price")
    trend_fig.write_image(f"{ticker}_trend.png")
    #print(trend)

    trend_log = ticker_price_analysis.df_log(trend)

    stationary_trend = ticker_price_analysis.get_stationary_trend(trend, window=12)

    stationary_trend = ticker_price_analysis.rolling_mean(stationary_trend, window=93)

    stationary_trend_fig = ticker_plotter.get_figure(stationary_trend, columns, title=f"{ticker} Stationary Price")
    stationary_trend_fig.write_image(f"{ticker}_stationary_trend.png")

    print(stationary_trend)


    # Create a candlestick figure
    #candlestick_fig = ticker_plotter.get_candlestick_figure(trend, title=f"{ticker} Candlestick")
    #candlestick_fig.write_image(f"{ticker}_candlestick.png")

    # Get pct change of prices
    print("Getting Percent Change")
    pct_change = ticker_price_analysis.get_pct_change(trend)

    pct_change = ticker_price_analysis.rolling_mean(pct_change, window=93)

    print("Plotting Percent Change")
    pct_fig = ticker_plotter.get_figure(pct_change, columns, title=f"{ticker} Percent Change", yaxis_name="Percent Change")
    pct_fig.write_image(f"{ticker}_pct.png")

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
