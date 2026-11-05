# history_orders_get

history\_orders\_get

Get orders from trading history with the ability to filter by ticket or position. There are three call options.

Call specifying a time interval. Return all orders falling within the specified interval.

|  |
| --- |
| history\_orders\_get(     date\_from,                // date the orders are requested from     date\_to,                  // date, up to which the orders are requested     group="GROUP"        // filter for selecting orders by symbols     ) |

Call specifying the order ticket. Return an order with the specified ticket.

|  |
| --- |
| history\_orders\_get(     ticket=TICKET        // order ticket  ) |

Call specifying the position ticket. Return all orders with a position ticket specified in the [ORDER\_POSITION\_ID](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_integer) property.

|  |
| --- |
| history\_orders\_get(     position=POSITION    // position ticket  ) |

Parameters

date\_from

[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first.

date\_to

[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second.

group="GROUP"

[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only orders meeting a specified criteria for a symbol name.

ticket=TICKET

[in]  Order ticket that should be received. Optional parameter. If not specified, the filter is not applied.

position=POSITION

[in]  Ticket of a position (stored in [ORDER\_POSITION\_ID](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_integer)) all orders should be received for. Optional parameter. If not specified, the filter is not applied.

Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function allows receiving all history orders within a specified period in a single call similar to the [HistoryOrdersTotal](../../Trade-Functions/HistoryOrdersTotal/HistoryOrdersTotal.md) and [HistoryOrderSelect](../../Trade-Functions/HistoryOrderSelect/HistoryOrderSelect.md) tandem.

The group parameter may contain several comma separated conditions. A condition can be set as a mask using '\*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="\*, !EUR" means that deals for all symbols should be selected first and the ones containing "EUR" in symbol names should be excluded afterwards.

Example:

|  |
| --- |
| from datetime import datetime  import MetaTrader5 as mt5  import pandas as pd  pd.set\_option('display.max\_columns', 500) # number of columns to be displayed  pd.set\_option('display.width', 1500)      # max table width to display  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)  print()  # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # get the number of orders in history  from\_date=datetime(2020,1,1)  to\_date=datetime.now()  history\_orders=mt5.history\_orders\_get(from\_date, to\_date, group="\*GBP\*")  if history\_orders==None:      print("No history orders with group=\"\*GBP\*\", error code={}".format(mt5.last\_error()))  elif len(history\_orders)>0:      print("history\_orders\_get({}, {}, group=\"\*GBP\*\")={}".format(from\_date,to\_date,len(history\_orders)))  print()     # display all historical orders by a position ticket  position\_id=530218319  position\_history\_orders=mt5.history\_orders\_get(position=position\_id)  if position\_history\_orders==None:      print("No orders with position #{}".format(position\_id))      print("error code =",mt5.last\_error())  elif len(position\_history\_orders)>0:      print("Total history orders on position #{}: {}".format(position\_id,len(position\_history\_orders)))      # display all historical orders having a specified position ticket      for position\_order in position\_history\_orders:                  print(position\_order)      print()      # display these orders as a table using pandas.DataFrame      df=pd.DataFrame(list(position\_history\_orders),columns=position\_history\_orders[0].\_asdict().keys())      df.drop(['time\_expiration','type\_time','state','position\_by\_id','reason','volume\_current','price\_stoplimit','sl','tp'], axis=1, inplace=True)      df['time\_setup'] = pd.to\_datetime(df['time\_setup'], unit='s')      df['time\_done'] = pd.to\_datetime(df['time\_done'], unit='s')      print(df)     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()     Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29     history\_orders\_get(2020-01-01 00:00:00, 2020-03-25 17:17:32.058795, group="\*GBP\*")=14     Total history orders on position #530218319: 2  TradeOrder(ticket=530218319, time\_setup=1582282114, time\_setup\_msc=1582282114681, time\_done=1582303777, time\_done\_msc=1582303777582, time\_expiration=0, ...  TradeOrder(ticket=535548147, time\_setup=1583176242, time\_setup\_msc=1583176242265, time\_done=1583176242, time\_done\_msc=1583176242265, time\_expiration=0, ...           ticket          time\_setup  time\_setup\_msc           time\_done  time\_done\_msc  type  type\_filling  magic  position\_id  volume\_initial  price\_open  price\_current  symbol comment external\_id  0  530218319 2020-02-21 10:48:34   1582282114681 2020-02-21 16:49:37  1582303777582     2             2      0    530218319            0.01     0.97898        0.97863  USDCHF                      1  535548147 2020-03-02 19:10:42   1583176242265 2020-03-02 19:10:42  1583176242265     1             0      0    530218319            0.01     0.95758        0.95758  USDCHF |

See also

[history\_deals\_total](../history_deals_total/history_deals_total.md), [history\_deals\_get](../history_deals_get/history_deals_get.md)
