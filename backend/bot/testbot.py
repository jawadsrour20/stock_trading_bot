# Requirments to install in enviroment:
#pip install pandas_datareader





import pandas_datareader.data as web
import datetime as dt
import numpy as np
import time




'''
The strategy we're going to use is to buy and sell whenever the 300 minute moving average crosses our price.
 Now, this is FAR from a good trading strategy, but the logic is relatively simple and will
 allow us to focus on the general structure of a trading bot
'''

def bot(company):
    
    while True:
        pos_held = False
        print("")
        print("Checking Price")
        
        now = dt.datetime.now()
        min5 = now - dt.timedelta(minutes=300)
        
        end = now.strftime("%H:%M")
        start = min5.strftime("%H:%M")
        print(start,end)
        market_data = web.DataReader(company, 'yahoo', start, end) # Get one bar object for each of the past 300 minutes
    
        close_list =  market_data['Adj Close'].to_numpy() # This numpy array will store all the closing prices from the last 5 minutes
        
    
        last_price = close_list[-1] # Most recent closing price
        ma = np.mean(close_list)
    
        print("Moving Average: " + str(ma))
        print("Last Price: " + str(last_price))
    
        
        if ma + 0.1 < last_price and not pos_held: # If MA is more than 10cents under price, and we haven't already bought
            print("Buy")
            # here put the api call this is a real one from alpaca_trade_api
            # api.submit_order(
            #     symbol=symb,
            #     qty=1,
            #     side='buy',
            #     type='market',
            #     time_in_force='gtc'
            # )
            pos_held = True
        elif ma - 0.1 > last_price and pos_held: # If MA is more than 10cents above price, and we already bought
            print("Sell")
            # api.submit_order(
            #     symbol=symb,
            #     qty=1,
            #     side='sell',
            #     type='market',
            #     time_in_force='gtc'
            # )
            pos_held = False
         
        time.sleep(60)
        

bot('AAPL') 