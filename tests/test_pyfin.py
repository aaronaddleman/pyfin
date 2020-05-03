from pyfin.pyfin import Stock
import pandas as pd
import datetime as dt
import pytest

@pytest.fixture
def apple_stock():
    startDate = dt.datetime(2020, 1 , 1)
    endDate = dt.datetime(2020, 2, 1)
    return Stock("AAPL", startDate, endDate)

def test_stock(apple_stock):
    assert isinstance(apple_stock, Stock)

def test_stock_getdata(apple_stock):
    apple_stock.getData()
    assert len(apple_stock.stock_data) == 21
