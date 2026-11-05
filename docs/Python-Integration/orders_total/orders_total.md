# orders_total

orders\_total

Get the number of active orders.

|  |
| --- |
| orders\_total() |

Return Value

Integer value.

Note

The function is similar to [OrdersTotal](../../Trade-Functions/OrdersTotal/OrdersTotal.md).

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # check the presence of active orders  orders=mt5.orders\_total()  if orders>0:      print("Total orders=",orders)  else:      print("Orders not found")     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown() |

See also

[orders\_get](../orders_get/orders_get.md), [positions\_total](../positions_total/positions_total.md)
