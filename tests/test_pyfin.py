from pyfin.pyfin import Stock
import pandas as pd
import datetime as dt
import pytest

@pytest.fixture
def apple_stock():
    startDate = dt.datetime(2020, 1 , 1)
    endDate = dt.datetime(2020, 2, 1)
    apple = Stock("AAPL", startDate, endDate)
    apple.getData()
    return apple

def test_stock(apple_stock):
    assert isinstance(apple_stock, Stock)

def test_stock_getdata(apple_stock):
    assert len(apple_stock.stock_data) == 21
    assert isinstance(apple_stock.stock_data, )

# def test_moving_average(apple_stock):
#     df = apple_stock.stock_data
#     moving_average_column = df.filter(regex='ma')
#     expected_list = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
#     assert len(expected_list) == len(df.columns)
