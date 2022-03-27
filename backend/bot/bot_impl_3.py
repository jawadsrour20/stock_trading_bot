from .bot_interface import BotInterface

import numpy as np

'''
We’ll build a mean reversion strategy that buys when a security reaches an extreme low, and sells when it reaches an extreme high. 
Properly tuned, this will allow us to extract returns from most any market regime
'''

# form : https://www.codearmo.com/python-tutorial/crypto-algo-trading-intraday-mean-reversion


class BotImplementation3(BotInterface):
    botId = "3"

    @staticmethod
    def get_decision(market_data):
        pos_held = False

        
        market_data['min_24'] = market_data.close.rolling(60*24).min()
        market_data['max_24'] = market_data.close.rolling(60*24).max()
        
    
        
    
      
        if ((market_data.close <= market_data.min_24) &(market_data.close > market_data.close.shift(60*24*30)*1.03))*1 and not pos_held: # If MA is more than 10cents under price, and we haven't already bought
            return("Buy")
            # here put the api call this is a real one from alpaca_trade_api
            # api.submit_order(
            #     symbol=symb,
            #     qty=1,
            #     side='buy',
            #     type='market',
            #     time_in_force='gtc'
            # )
            pos_held = True
        elif ((market_data.close >= market_data.min_24) &(market_data.close < market_data.close.shift(60*24*30)*1.03))*1 and pos_held: # If MA is more than 10cents above price, and we already bought
            return("Sell")
            # api.submit_order(
            #     symbol=symb,
            #     qty=1,
            #     side='sell',
            #     type='market',
            #     time_in_force='gtc'
            # )
            pos_held = False

'''
trial = Yfinance_Data_Fetcher.get_history_between_two_dates("AAPL", "2022-01-01", "2022-03-11", Interval.ONE_DAY )
BotImplementation3.get_decision(trial)
'''
if __name__=="__main__":
    print("Hello From The Third Implementation")