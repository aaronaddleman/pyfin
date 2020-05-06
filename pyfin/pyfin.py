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
        self.exp_moving_averages = [3,5,8,10,12,15,30,35,40,45,50,60]

    def getData(self):
        '''Fetch the stock data for the date range provided'''
        df = pdr.get_data_yahoo(self.symbol, self.startdate, self.enddate)
        self.stock_data = df

    def addMovingAverage(self, moving_average_days=10, remove_nil=False):
        '''Add moving average to the stock'''
        smaString="Sma_"+str(moving_average_days)
        df = self.stock_data
        self.stock_data[smaString]=df.iloc[:,4].rolling(window=moving_average_days).mean()
        if remove_nil :
            self.stock_data = self.stock_data.iloc[moving_average_days:]

    def addExpMovingAverage(self):
        for moving_average in self.exp_moving_averages:
            mean_value = self.stock_data['Adj Close'].ewm(span=moving_average,adjust=False).mean()
            mean_df = pd.DataFrame()
            self.stock_data.loc[self.stock_data['Adj Close'], "ExpMovAvg_"+str(moving_average)] = round(mean_value)
