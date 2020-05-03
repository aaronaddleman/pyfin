from pyfin import Stock
import datetime as dt

startDate = dt.datetime(2020, 1, 1)
endDate = dt.datetime.now()
apple = Stock("AAPL", startDate, endDate)
apple.getData()
print(apple.stock_data)
