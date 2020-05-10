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
        self.validate_stocks()
        self.strategies = {}

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

    def validate_stocks(self):
        try:
            # find remainder of dividing by 2
            # and compare if the remainder is 0
            len(self.exp_moving_averages) % 2 == 0
        except:
            print("current exp moving avg: ")
            print(self.exp_moving_averages)
            raise Exception('exp_moving_averages should be divisible by 2')

    def addExpMovingAverage(self):
        for moving_average in self.exp_moving_averages:
            mean_value = self.stock_data.loc[:,'Adj Close'].ewm(span=moving_average, adjust=False).mean()
            self.stock_data["Ema_"+str(moving_average)] = round(mean_value, 2)

class Strategy():
    def __init__(self, name=None):
        self.name = name
        self.results = {'df': None, 'success_rate': 0, 'percentchange': None}

    def red_white_blue(self, dataframe=None):
        # build vars for socks
        # filter columns based on name starting with Ema_
        df = dataframe.copy()
        exp_mov_avg = [col for col in df if col.startswith('Ema_')]
        exp_mov_avg_half_int = len(exp_mov_avg) / 2
        exp_mov_avg_half_cnt = 1
        exp_mov_avg_min = []
        exp_mov_avg_max = []

        # build min and max moving averages
        for exp in exp_mov_avg:
            if exp_mov_avg_half_cnt <= exp_mov_avg_half_int:
                # if the half count is less than or equal
                # to length of exp_mov_avg, it is a min value
                exp_mov_avg_min.append(exp)
                exp_mov_avg_half_cnt += 1
            else:
                exp_mov_avg_max.append(exp)

        df["Exp_Min"] = df[exp_mov_avg_min].min(axis=1)
        df["Exp_Max"] = df[exp_mov_avg_max].max(axis=1)
        pos = 0
        num = 0
        percentchange = []

        # if exp_min is greater than exp_max, buy
        # if not, then sell
        for i in df.index:
            cmin = df['Exp_Min'][i]
            cmax = df['Exp_Max'][i]
            close = df['Adj Close'][i]

            if (cmin > cmax):
                if (pos == 0):
                    bp = close
                    pos = 1
            elif (cmin < cmax):
                if (pos == 1):
                    pos = 0
                    sp = close
                    pc = (sp/bp-1)*100
                    percentchange.append(pc)

            if (num == df["Adj Close"].count()-1 and pos == 1):
                pos = 0
                sp = close
                print("selling now at " + str(sp))
                pc = (sp/bp-1)*100
                percentchange.append(pc)
            num+=1
        self.results['df'] = df
        self.results['percentchange'] = percentchange
