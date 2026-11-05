# history_deals_get

history\_deals\_get

Get deals from trading history within the specified interval with the ability to filter by ticket or position.

Call specifying a time interval. Return all deals falling within the specified interval.

|  |
| --- |
| history\_deals\_get(     date\_from,                // date the deals are requested from     date\_to,                  // date, up to which the deals are requested     group="GROUP"        // filter for selecting deals for symbols     ) |

Call specifying the order ticket. Return all deals having the specified order ticket in the [DEAL\_ORDER](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_integer) property.

|  |
| --- |
| history\_deals\_get(     ticket=TICKET        // order ticket  ) |

Call specifying the position ticket. Return all deals having the specified position ticket in the [DEAL\_POSITION\_ID](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_integer) property.

|  |
| --- |
| history\_deals\_get(     position=POSITION    // position ticket  ) |

Parameters

date\_from

[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first.

date\_to

[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second.

group="GROUP"

[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only deals meeting a specified criteria for a symbol name.

ticket=TICKET

[in]  Ticket of an order (stored in [DEAL\_ORDER](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_integer)) all deals should be received for. Optional parameter. If not specified, the filter is not applied.

position=POSITION

[in]  Ticket of a position (stored in [DEAL\_POSITION\_ID](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_integer)) all deals should be received for. Optional parameter. If not specified, the filter is not applied.

Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function allows receiving all history deals within a specified period in a single call similar to the [HistoryDealsTotal](../../Trade-Functions/HistoryDealsTotal/HistoryDealsTotal.md) and [HistoryDealSelect](../../Trade-Functions/HistoryDealSelect/HistoryDealSelect.md) tandem.

The group parameter allows sorting out deals by symbols. '\*' can be used at the beginning and the end of a string.

The group parameter may contain several comma separated conditions. A condition can be set as a mask using '\*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="\*, !EUR" means that deals for all symbols should be selected first and the ones containing "EUR" in symbol names should be excluded afterwards.

Example:

|  |
| --- |
| import MetaTrader5 as mt5  from datetime import datetime  import pandas as pd  pd.set\_option('display.max\_columns', 500) # number of columns to be displayed  pd.set\_option('display.width', 1500)      # max table width to display  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)  print()  # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # get the number of deals in history  from\_date=datetime(2020,1,1)  to\_date=datetime.now()  # get deals for symbols whose names contain "GBP" within a specified interval  deals=mt5.history\_deals\_get(from\_date, to\_date, group="\*GBP\*")  if deals==None:      print("No deals with group=\"\*USD\*\", error code={}".format(mt5.last\_error()))  elif len(deals)> 0:      print("history\_deals\_get({}, {}, group=\"\*GBP\*\")={}".format(from\_date,to\_date,len(deals)))     # get deals for symbols whose names contain neither "EUR" nor "GBP"  deals = mt5.history\_deals\_get(from\_date, to\_date, group="\*,!\*EUR\*,!\*GBP\*")  if deals == None:      print("No deals, error code={}".format(mt5.last\_error()))  elif len(deals) > 0:      print("history\_deals\_get(from\_date, to\_date, group=\"\*,!\*EUR\*,!\*GBP\*\") =", len(deals))      # display all obtained deals 'as is'      for deal in deals:          print("  ",deal)      print()      # display these deals as a table using pandas.DataFrame      df=pd.DataFrame(list(deals),columns=deals[0].\_asdict().keys())      df['time'] = pd.to\_datetime(df['time'], unit='s')      print(df)  print("")     # get all deals related to the position #530218319  position\_id=530218319  position\_deals = mt5.history\_deals\_get(position=position\_id)  if position\_deals == None:      print("No deals with position #{}".format(position\_id))      print("error code =", mt5.last\_error())  elif len(position\_deals) > 0:      print("Deals with position id #{}: {}".format(position\_id, len(position\_deals)))      # display these deals as a table using pandas.DataFrame      df=pd.DataFrame(list(position\_deals),columns=position\_deals[0].\_asdict().keys())      df['time'] = pd.to\_datetime(df['time'], unit='s')      print(df)     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()     Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29     history\_deals\_get(from\_date, to\_date, group="\*GBP\*") = 14     history\_deals\_get(from\_date, to\_date, group="\*,!\*EUR\*,!\*GBP\*") = 7     TradeDeal(ticket=506966741, order=0, time=1582202125, time\_msc=1582202125419, type=2, entry=0, magic=0, position\_id=0, reason=0, volume=0.0, pri ...     TradeDeal(ticket=507962919, order=530218319, time=1582303777, time\_msc=1582303777582, type=0, entry=0, magic=0, position\_id=530218319, reason=0, ...     TradeDeal(ticket=513149059, order=535548147, time=1583176242, time\_msc=1583176242265, type=1, entry=1, magic=0, position\_id=530218319, reason=0, ...     TradeDeal(ticket=516943494, order=539349382, time=1583510003, time\_msc=1583510003895, type=1, entry=0, magic=0, position\_id=539349382, reason=0, ...     TradeDeal(ticket=516943915, order=539349802, time=1583510025, time\_msc=1583510025054, type=0, entry=0, magic=0, position\_id=539349802, reason=0, ...     TradeDeal(ticket=517139682, order=539557870, time=1583520201, time\_msc=1583520201227, type=0, entry=1, magic=0, position\_id=539349382, reason=0, ...     TradeDeal(ticket=517139716, order=539557909, time=1583520202, time\_msc=1583520202971, type=1, entry=1, magic=0, position\_id=539349802, reason=0, ...           ticket      order                time       time\_msc  type  entry  magic  position\_id  reason  volume    price  commission  swap     profit  fee  symbol comment external\_id  0  506966741          0 2020-02-20 12:35:25  1582202125419     2      0      0            0       0    0.00  0.00000         0.0   0.0  100000.00  0.0                              1  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0       0.00  0.0  USDCHF                      2  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0     -22.35  0.0  USDCHF                      3  516943494  539349382 2020-03-06 15:53:23  1583510003895     1      0      0    539349382       0    0.10  0.93475         0.0   0.0       0.00  0.0  USDCHF                      4  516943915  539349802 2020-03-06 15:53:45  1583510025054     0      0      0    539349802       0    0.10  0.66336         0.0   0.0       0.00  0.0  AUDUSD                      5  517139682  539557870 2020-03-06 18:43:21  1583520201227     0      1      0    539349382       0    0.10  0.93751         0.0   0.0     -29.44  0.0  USDCHF                      6  517139716  539557909 2020-03-06 18:43:22  1583520202971     1      1      0    539349802       0    0.10  0.66327         0.0   0.0      -0.90  0.0  AUDUSD                         Deals with position id #530218319: 2        ticket      order                time       time\_msc  type  entry  magic  position\_id  reason  volume    price  commission  swap  profit  fee  symbol comment external\_id  0  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0    0.00  0.0  USDCHF                      1  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0  -22.35  0.0  USDCHF |

See also

[history\_deals\_total](../history_deals_total/history_deals_total.md), [history\_orders\_get](../history_orders_get/history_orders_get.md)
