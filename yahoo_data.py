import pandas as pd
import yfinance as yf
import pandas_datareader.data
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt

#dates go in YYYY, MM, DD format
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2021, 1, 1)
Apple = web.DataReader('AAPL', 'yahoo', start, end)
print(Apple)
Apple['Adj Close'].plot(label='AAPL',title='Apple Adjusted Closing Price' )
plt.savefig('Apple2.png')


