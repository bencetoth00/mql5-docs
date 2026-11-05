# orders_get

orders\_get

Get active orders with the ability to filter by symbol or ticket. There are three call options.

Call without parameters. Return active orders on all symbols.

|  |
| --- |
| orders\_get() |

Call specifying a symbol active orders should be received for.

|  |
| --- |
| orders\_get(     symbol="SYMBOL"      // symbol name  ) |

Call specifying a group of symbols active orders should be received for.

|  |
| --- |
| orders\_get(     group="GROUP"        // filter for selecting orders for symbols  ) |

Call specifying the order ticket.

|  |
| --- |
| orders\_get(     ticket=TICKET        // ticket  ) |

symbol="SYMBOL"

[in]  Symbol name. Optional named parameter. If a symbol is specified, the ticket parameter is ignored.

group="GROUP"

[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only active orders meeting a specified criteria for a symbol name.

ticket=TICKET

[in]  Order ticket ([ORDER\_TICKET](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_integer)). Optional named parameter.

Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function allows receiving all active orders within one call similar to the [OrdersTotal](../../Trade-Functions/OrdersTotal/OrdersTotal.md) and [OrderSelect](../../Trade-Functions/OrderSelect/OrderSelect.md) tandem.

The group parameter allows sorting out orders by symbols. '\*' can be used at the beginning and the end of a string.

The group parameter may contain several comma separated conditions. A condition can be set as a mask using '\*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="\*, !EUR" means that orders for all symbols should be selected first and the ones containing "EUR" in symbol names should be excluded afterwards.

Example:

|  |
| --- |
| import MetaTrader5 as mt5  import pandas as pd  pd.set\_option('display.max\_columns', 500) # number of columns to be displayed  pd.set\_option('display.width', 1500)      # max table width to display  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)  print()  # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # display data on active orders on GBPUSD  orders=mt5.orders\_get(symbol="GBPUSD")  if orders is None:      print("No orders on GBPUSD, error code={}".format(mt5.last\_error()))  else:      print("Total orders on GBPUSD:",len(orders))      # display all active orders      for order in orders:          print(order)  print()     # get the list of orders on symbols whose names contain "\*GBP\*"  gbp\_orders=mt5.orders\_get(group="\*GBP\*")  if gbp\_orders is None:      print("No orders with group=\"\*GBP\*\", error code={}".format(mt5.last\_error()))  else:      print("orders\_get(group=\"\*GBP\*\")={}".format(len(gbp\_orders)))      # display these orders as a table using pandas.DataFrame      df=pd.DataFrame(list(gbp\_orders),columns=gbp\_orders[0].\_asdict().keys())      df.drop(['time\_done', 'time\_done\_msc', 'position\_id', 'position\_by\_id', 'reason', 'volume\_initial', 'price\_stoplimit'], axis=1, inplace=True)      df['time\_setup'] = pd.to\_datetime(df['time\_setup'], unit='s')      print(df)     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()     Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29     Total orders on GBPUSD: 2  TradeOrder(ticket=554733548, time\_setup=1585153667, time\_setup\_msc=1585153667718, time\_done=0, time\_done\_msc=0, time\_expiration=0, type=3, type\_time=0, ...  TradeOrder(ticket=554733621, time\_setup=1585153671, time\_setup\_msc=1585153671419, time\_done=0, time\_done\_msc=0, time\_expiration=0, type=2, type\_time=0, ...     orders\_get(group="\*GBP\*")=4        ticket          time\_setup  time\_setup\_msc  time\_expiration  type  type\_time  type\_filling  state  magic  volume\_current  price\_open   sl   tp  price\_current  symbol comment external\_id  0  554733548 2020-03-25 16:27:47   1585153667718                0     3          0             2      1      0             0.2     1.25379  0.0  0.0        1.16803  GBPUSD                      1  554733621 2020-03-25 16:27:51   1585153671419                0     2          0             2      1      0             0.2     1.14370  0.0  0.0        1.16815  GBPUSD                      2  554746664 2020-03-25 16:38:14   1585154294401                0     3          0             2      1      0             0.2     0.93851  0.0  0.0        0.92428  EURGBP                      3  554746710 2020-03-25 16:38:17   1585154297022                0     2          0             2      1      0             0.2     0.90527  0.0  0.0        0.92449  EURGBP |

See also

[orders\_total](../orders_total/orders_total.md), [positions\_get](../positions_get/positions_get.md)
