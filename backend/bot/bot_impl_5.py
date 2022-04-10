from .bot_interface import BotInterface
from .bot_utils import BotUtils

import numpy as np

'''
The Three White Soldiers is a multiple candlestick pattern that is formed after a downtrend indicating a bullish reversal.

These candlestick charts are made of three long bullish bodies which do not have long shadows and are open within the real body of the previous candle in the pattern.
'''

class BotImplementation5(BotInterface):
    botId = "5"

    @staticmethod
    def get_decision(market_data):
        close_list = market_data['Close'].to_numpy() # This numpy array will store all the closing prices
        open_list = market_data['Open'].to_numpy() # This numpy array will store all the opening prices
        if(len(close_list) < 4):
            return "none"
        
        indexes = [i for i in range(len(close_list[:-3]))]
        close_list_trend_of_old_sticks = BotUtils.get_trend_line(indexes, close_list[:-3])

        indexes_new = [i for i in range(3)]
        close_list_trend_of_new_sticks = BotUtils.get_trend_line(indexes_new, close_list[-3:])

        if(close_list_trend_of_new_sticks <= 0):
            return "none"
        else:
            if close_list_trend_of_old_sticks < 0 and\
               open_list[-3] <= open_list[-2] <= close_list[-3] and\
               open_list[-2] <= open_list[-1] <= close_list[-2]:
                return "buy"

        return "none"

if __name__=="__main__":
    print("Hello From The Fifth Implementation")