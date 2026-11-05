# history_deals_total

history\_deals\_total

Get the number of deals in trading history within the specified interval.

|  |
| --- |
| history\_deals\_total(     date\_from,    // date the deals are requested from     date\_to       // date, up to which the deals are requested     ) |

Parameters

date\_from

[in]  Date the deals are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

date\_to

[in]  Date, up to which the deals are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

Return Value

Integer value.

Note

The function is similar to [HistoryDealsTotal](../../Trade-Functions/HistoryDealsTotal/HistoryDealsTotal.md).

Example:

|  |
| --- |
| from datetime import datetime  import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # get the number of deals in history  from\_date=datetime(2020,1,1)  to\_date=datetime.now()  deals=mt5.history\_deals\_total(from\_date, to\_date)  if deals>0:      print("Total deals=",deals)  else:      print("Deals not found in history")     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown() |

See also

[history\_deals\_get](../history_deals_get/history_deals_get.md), [history\_orders\_total](../history_orders_total/history_orders_total.md)
