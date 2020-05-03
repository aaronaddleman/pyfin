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
        self.stock_data = []

    def getData(self):
        df = pdr.get_data_yahoo(self.symbol, self.startdate, self.enddate)
        self.stock_data = df
