# history_orders_total

history\_orders\_total

Get the number of orders in trading history within the specified interval.

|  |
| --- |
| history\_orders\_total(     date\_from,    // date the orders are requested from     date\_to       // date, up to which the orders are requested     ) |

Parameters

date\_from

[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

date\_to

[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

Return Value

Integer value.

Note

The function is similar to [HistoryOrdersTotal](../../Trade-Functions/HistoryOrdersTotal/HistoryOrdersTotal.md).

Example:

|  |
| --- |
| from datetime import datetime  import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # get the number of orders in history  from\_date=datetime(2020,1,1)  to\_date=datetime.now()  history\_orders=mt5.history\_orders\_total(from\_date, datetime.now())  if history\_orders>0:      print("Total history orders=",history\_orders)  else:      print("Orders not found in history")     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown() |

See also

[history\_orders\_get](../history_orders_get/history_orders_get.md), [history\_deals\_total](../history_deals_total/history_deals_total.md)
