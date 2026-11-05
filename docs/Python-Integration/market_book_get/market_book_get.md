# market_book_get

market\_book\_get

Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol.

|  |
| --- |
| market\_book\_get(     symbol      // financial instrument name  ) |

symbol

[in]  Financial instrument name. Required unnamed parameter.

Return Value

Returns the Market Depth content as a tuple from BookInfo entries featuring order type, price and volume in lots. BookInfo is similar to the [MqlBookInfo](../../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md) structure.

Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The subscription to the Market Depth change events should be preliminarily performed using the [market\_book\_add()](../market_book_add/market_book_add.md) function.

The function is similar to [MarketBookGet](../../Market-Info/MarketBookGet/MarketBookGet.md).

 

Example:

|  |
| --- |
| import MetaTrader5 as mt5  import time  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)  print("")     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())     # shut down connection to the MetaTrader 5 terminal      mt5.shutdown()      quit()     # subscribe to market depth updates for EURUSD (Depth of Market)  if mt5.market\_book\_add('EURUSD'):    # get the market depth data 10 times in a loop     for i in range(10):          # get the market depth content (Depth of Market)          items = mt5.market\_book\_get('EURUSD')          # display the entire market depth 'as is' in a single string          print(items)          # now display each order separately for more clarity          if items:              for it in items:                  # order content                  print(it.\_asdict())          # pause for 5 seconds before the next request of the market depth data          time.sleep(5)    # cancel the subscription to the market depth updates (Depth of Market)     mt5.market\_book\_release('EURUSD')  else:      print("mt5.market\_book\_add('EURUSD') failed, error code =",mt5.last\_error())     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.34     (BookInfo(type=1, price=1.20038, volume=250, volume\_dbl=250.0), BookInfo(type=1, price=1.20032, volume=100, volume...  {'type': 1, 'price': 1.20038, 'volume': 250, 'volume\_dbl': 250.0}  {'type': 1, 'price': 1.20032, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 1, 'price': 1.2003, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 1, 'price': 1.20028, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20026, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20025, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 2, 'price': 1.20023, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 2, 'price': 1.20017, 'volume': 250, 'volume\_dbl': 250.0}  (BookInfo(type=1, price=1.2004299999999999, volume=250, volume\_dbl=250.0), BookInfo(type=1, price=1.20037, volume...  {'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume\_dbl': 250.0}  {'type': 1, 'price': 1.20037, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 1, 'price': 1.20036, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 1, 'price': 1.20034, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20031, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20029, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 2, 'price': 1.20028, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 2, 'price': 1.20022, 'volume': 250, 'volume\_dbl': 250.0}  (BookInfo(type=1, price=1.2004299999999999, volume=250, volume\_dbl=250.0), BookInfo(type=1, price=1.20037, volume...  {'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume\_dbl': 250.0}  {'type': 1, 'price': 1.20037, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 1, 'price': 1.20036, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 1, 'price': 1.20034, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20031, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20029, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 2, 'price': 1.20028, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 2, 'price': 1.20022, 'volume': 250, 'volume\_dbl': 250.0}  (BookInfo(type=1, price=1.20036, volume=250, volume\_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...  {'type': 1, 'price': 1.20036, 'volume': 250, 'volume\_dbl': 250.0}  {'type': 1, 'price': 1.20029, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 1, 'price': 1.20028, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 1, 'price': 1.20026, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20023, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20022, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 2, 'price': 1.20021, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 2, 'price': 1.20014, 'volume': 250, 'volume\_dbl': 250.0}  (BookInfo(type=1, price=1.20035, volume=250, volume\_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...  {'type': 1, 'price': 1.20035, 'volume': 250, 'volume\_dbl': 250.0}  {'type': 1, 'price': 1.20029, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 1, 'price': 1.20027, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 1, 'price': 1.20025, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20023, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20022, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 2, 'price': 1.20021, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 2, 'price': 1.20014, 'volume': 250, 'volume\_dbl': 250.0}  (BookInfo(type=1, price=1.20037, volume=250, volume\_dbl=250.0), BookInfo(type=1, price=1.20031, volume=100, volume...  {'type': 1, 'price': 1.20037, 'volume': 250, 'volume\_dbl': 250.0}  {'type': 1, 'price': 1.20031, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 1, 'price': 1.2003, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 1, 'price': 1.20028, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20025, 'volume': 36, 'volume\_dbl': 36.0}  {'type': 2, 'price': 1.20023, 'volume': 50, 'volume\_dbl': 50.0}  {'type': 2, 'price': 1.20022, 'volume': 100, 'volume\_dbl': 100.0}  {'type': 2, 'price': 1.20016, 'volume': 250, 'volume\_dbl': 250.0} |

 

See also

[market\_book\_add](../market_book_add/market_book_add.md), [market\_book\_release](../market_book_release/market_book_release.md), [Market Depth structure](../../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md)
