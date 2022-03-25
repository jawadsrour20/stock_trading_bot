import yfinance as yf
from .time_utils import Interval, Period

class Yfinance_Data_Fetcher(object):

    @staticmethod
    def get_ticker_data(ticker):
        ticker_data = yf.Ticker(ticker)
        return ticker_data

    @staticmethod
    def get_stock_info(ticker):
        return Yfinance_Data_Fetcher.get_ticker_data(ticker).info
    
    @staticmethod
    # start and end dates should have the following format : "YYYY-MM-DD"
    def get_history_between_two_dates(ticker, start_date, end_date, interval):
        return Yfinance_Data_Fetcher.get_ticker_data(ticker).history(start = start_date, end = end_date, interval = interval)
    
    @staticmethod
    def get_history_by_period(ticker, period, interval):
        return Yfinance_Data_Fetcher.get_ticker_data(ticker).history(period = period, interval = interval)

'''
# remove multiline comment to see how the output is
print(Yfinance_Data_Fetcher.get_history_between_two_dates("AAPL", "2022-01-01", "2022-03-11", Interval.ONE_HOUR))
print(Yfinance_Data_Fetcher.get_history_by_period("AAPL", Period.ONE_MONTH, Interval.ONE_WEEK))
'''     