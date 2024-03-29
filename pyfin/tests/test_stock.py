from pyfin.stock import Stock
import pandas as pd
import datetime as dt
import pytest

@pytest.fixture
def apple_stock():
    startDate = dt.datetime(2020, 1 , 1)
    endDate = dt.datetime(2020, 2, 1)
    apple = Stock(symbol="AAPL", startDate=startDate, endDate=endDate)
    apple.getData()
    return apple

def test_stock(apple_stock):
    assert isinstance(apple_stock, Stock)

def test_stock_getdata(apple_stock):
    assert 21 == len(apple_stock.stock_data.index)
    assert isinstance(apple_stock.stock_data, pd.DataFrame)

def test_moving_average(apple_stock):
    stock_data = apple_stock.stock_data
    apple_stock.addMovingAverage(10, remove_nil=True)
    moving_average_column = stock_data.filter(regex='ma')
    expected_list = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Sma_10']
    assert len(expected_list) == len(stock_data.columns)
    assert 'Sma_10' in stock_data.columns

def test_validate_params_fails():
    startDate = dt.datetime(2020, 1 , 1)
    endDate = dt.datetime(2020, 2, 1)
    bad_avg = Stock(symbol="AAPL", startDate=startDate, endDate=endDate, exp_moving_averages=[1,2,3])
    with pytest.raises(Exception):
        assert bad_avg.validate_stocks()


