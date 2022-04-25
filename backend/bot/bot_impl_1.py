from .bot_interface import BotInterface

import numpy as np

class BotImplementation1(BotInterface):
    botId = "1"

    @staticmethod
    def get_decision(market_data):

        close_list =  market_data['Close'].to_numpy() # This numpy array will store all the closing prices from the last 5 minutes
        
    
        last_price = close_list[-1] # Most recent closing price
        ma = np.mean(close_list)
    
        print("Moving Average: " + str(ma))
        print("Last Price: " + str(last_price))
    
        
        if ma + 0.1 < last_price: # If MA is more than 10cents under price, and we haven't already bought
            return("Buy")
            # here put the api call this is a real one from alpaca_trade_api
            # api.submit_order(
            #     symbol=symb,
            #     qty=1,
            #     side='buy',
            #     type='market',
            #     time_in_force='gtc'
            # )
        elif ma - 0.1 > last_price: # If MA is more than 10cents above price, and we already bought
            return("Sell")
            # api.submit_order(
            #     symbol=symb,
            #     qty=1,
            #     side='sell',
            #     type='market',
            #     time_in_force='gtc'
            # )
        else:
            return("Buy/Sell")

'''
trial = Yfinance_Data_Fetcher.get_history_between_two_dates("AAPL", "2022-01-01", "2022-03-11", Interval.ONE_HOUR)
BotImplementation1.get_decision(trial)
'''
if __name__=="__main__":
    print("Hello From The First Implementation")