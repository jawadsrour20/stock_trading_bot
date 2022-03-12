
# Requirments to install in enviroment:
#pip install pandas_datareader

import pandas_datareader.data as web
import datetime as dt



company = 'AAPL' #apple company

# get the data of the last year for the specefied stock 
today = dt.date.today()
week_ago = today - dt.timedelta(days=365)

start = week_ago
end = today


# Pandas web data reader is an extension of pandas library to communicate with most updated financial data.
# This will include sources as: Yahoo Finance

df = web.DataReader(company, 'yahoo', start, end)
print(df)

# For the rest of analysis, we will use the Closing Price which remarks
# the final price in which the stocks are traded by the end of the day.

'''
Rolling mean/Moving Average (MA) smooths out price data by creating a constantly updated average price.
 This is useful to cut down “noise” in our price chart.
 This will calculate the Moving Average for the last 100 windows (50 days) of stocks closing price 
 and take the average for each of the window’s moving average.
'''

close_px = df['Adj Close']
mavg = close_px.rolling(window=50).mean()


#For better understanding, let’s plot it out with Matplotlib. We will overlay the Moving Average with our Stocks Price Chart.


import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()
plt.show()
