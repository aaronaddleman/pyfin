from pyfin import Stock
import datetime as dt

startDate = dt.datetime(2019, 5, 1)
endDate = dt.datetime.now()
apple = Stock("AAPL", startDate, endDate)
apple.getData()
apple.addMovingAverage(50)
print(apple.stock_data)
