from .bot_interface import BotInterface
from .bot_utils import BotUtils

import numpy as np

'''

Piercing pattern is multiple candlestick chart pattern that is formed after a downtrend indicating a bullish reversal.

It is formed by two candles, the first candle being a bearish candle which indicates the continuation of the downtrend.

The second candle is a bullish candle which opens gap down but closes more than 50% of the real body of the previous candle which shows that the bulls are back in the market and a bullish reversal is going to take place.

'''

class BotImplementation4(BotInterface):
    botId = "4"

    @staticmethod
    def get_decision(market_data):
        close_list =  market_data['Close'].to_numpy() # This numpy array will store all the closing prices
        
        if(len(close_list) < 2):
            return "none"

        indexes = [i for i in range(len(close_list))]
        close_list_trend = BotUtils.get_trend_line(indexes, close_list)

        if (close_list_trend < 0) and (((close_list[-1] - close_list[-2]) / close_list[-2]) >= 0.5):
            return "buy"
        
        else:
            return "none"

    '''
        if the slope is a +ve value --> increasing trend

        if the slope is a -ve value --> decreasing trend

        if the slope is a zero value --> No trend
    '''

if __name__=="__main__":
    print("Hello From The Fourth Implementation")