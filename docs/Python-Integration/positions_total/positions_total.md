# positions_total

positions\_total

Get the number of open positions.

|  |
| --- |
| positions\_total() |

Return Value

Integer value.

Note

The function is similar to [PositionsTotal](../../Trade-Functions/PositionsTotal/PositionsTotal.md).

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # check the presence of open positions  positions\_total=mt5.positions\_total()  if positions\_total>0:      print("Total positions=",positions\_total)  else:      print("Positions not found")     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown() |

See also

[positions\_get](../positions_get/positions_get.md), [orders\_total](../orders_total/orders_total.md)
