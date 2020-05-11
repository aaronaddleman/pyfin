from pyfin import Stock
from pyfin import Strategy
import datetime as dt

startDate = dt.datetime(2018, 3, 29)
#endDate = dt.datetime(2020, 1, 15)
endDate = dt.datetime.now()

### appl
apple = Stock("AAPL", startDate, endDate)
apple.getData()
#apple.addMovingAverage(moving_average_days=50, remove_nil=True)
#apple.addMovingAverage(moving_average_days=10, remove_nil=True)
#apple.addMovingAverage(moving_average_days=5, remove_nil=True)
apple.addExpMovingAverage()
apple_strategy_rwb = Strategy(name='rwb', stock_obj=apple)
apple_strategy_rwb.red_white_blue(dataframe=apple.stock_data)
apple.strategies.update({'rwb' : apple_strategy_rwb})

#print(apple.stock_data)
#print(apple.strategies['rwb'].dataframe)
#print(apple.strategies['rwb'].percentchange)
apple_strategy_rwb.build_report()
