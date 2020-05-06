from pyfin import Stock
import datetime as dt

startDate = dt.datetime(2019, 5, 1)
endDate = dt.datetime.now()
apple = Stock("AAPL", startDate, endDate)
apple.getData()
apple.addMovingAverage(moving_average_days=50, remove_nil=True)
apple.addMovingAverage(moving_average_days=10, remove_nil=True)
apple.addMovingAverage(moving_average_days=5, remove_nil=True)
apple.addExpMovingAverage()
