import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

class Stock():
    def __init__(self, symbol, startDate, endDate):
        self.symbol = symbol
        self.startdate = startDate
        self.enddate = endDate

    def getData(self):
        df = pdr.get_data_yahoo(self.symbol, self.startdate, self.enddate)
        self.stock_data = df

    def addMovingAverage(self, moving_average_days=10, remove_nil=False):
        smaString="Sma_"+str(moving_average_days)
        df = self.stock_data
        self.stock_data[smaString]=df.iloc[:,4].rolling(window=moving_average_days).mean()
        if remove_nil :
            self.stock_data = self.stock_data.iloc[moving_average_days:]
