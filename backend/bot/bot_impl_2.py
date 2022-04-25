from .bot_interface import BotInterface

import numpy as np
import pandas as pd

'''
The Turtle Trading system was coined by Richard Dennis and worked brilliantly for the traders in the 1980’s.
 But it turns out that the system requires some tweaking for it to reflect new market conditions and be effective now. 
 That said, trends still happen which means there are a plethora of trading opportunities.

The core of the turtle trading strategy is to take a position on futures on a 55-day breakout.
 A 55-day breakout is when the price exceeds high or low of past 55 days price. 

'''
# https://blog.quantinsti.com/turtle-trading-in-python/ used this for strategy    



class BotImplementation2(BotInterface):
    botId = "2"

    @staticmethod
    def get_decision(market_data):
    
        # 5-days high
        market_data['high'] = market_data.Close.shift(1).rolling(window=5).max()
        # 5-days low
        market_data['low'] = market_data.Close.shift(1).rolling(window=5).min()
        # 5-days mean
        market_data['avg'] = market_data.Close.shift(1).rolling(window=5).mean()


        if market_data.Close[-1] > market_data.high[-1]: # If MA is more than 10cents under price, and we haven't already bought
            return("Buy")
            # here put the api call this is a real one from alpaca_trade_api
            # api.submit_order(
            #     symbol=symb,
            #     qty=1,
            #     side='buy',
            #     type='market',
            #     time_in_force='gtc'
            # )
        elif market_data.Close[-1] < market_data.avg[-1]: # If MA is more than 10cents above price, and we already bought
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
trial = Yfinance_Data_Fetcher.get_history_between_two_dates("AAPL", "2022-01-01", "2022-03-11", Interval.ONE_DAY )
BotImplementation2.get_decision(trial)
'''
if __name__=="__main__":
    print("Hello From The Second Implementation")