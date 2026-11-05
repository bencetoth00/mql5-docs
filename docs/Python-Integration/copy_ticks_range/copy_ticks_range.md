# copy_ticks_range

copy\_ticks\_range

Get ticks for the specified date range from the MetaTrader 5 terminal.

|  |
| --- |
| copy\_ticks\_range(     symbol,       // symbol name     date\_from,    // date the ticks are requested from     date\_to,      // date, up to which the ticks are requested     flags         // combination of flags defining the type of requested ticks     ) |

Parameters

symbol

[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.

date\_from

[in]  Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

date\_to

[in]  Date, up to which the ticks are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

flags

[in]  A flag to define the type of the requested ticks. COPY\_TICKS\_INFO – ticks with Bid and/or Ask changes, COPY\_TICKS\_TRADE – ticks with changes in Last and Volume, COPY\_TICKS\_ALL – all ticks. Flag values are described in the [COPY\_TICKS](../copy_ticks_from/copy_ticks_from.md#copy_ticks) enumeration. Required unnamed parameter.

Return Value

Returns ticks as the numpy array with the named time, bid, ask, last and flags columns. The 'flags' value can be a combination of flags from the [TICK\_FLAG](../copy_ticks_from/copy_ticks_from.md#tick_flag) enumeration. Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

See the [CopyTicks](../../Timeseries-and-Indicators-Access/CopyTicks/CopyTicks.md) function for more information.

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. The data obtained from MetaTrader 5 have UTC time, but Python applies the local time shift again when trying to print them. Thus, the obtained data should also be corrected for visual presentation.

Example:

|  |
| --- |
| from datetime import datetime  import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # import the 'pandas' module for displaying data obtained in the tabular form  import pandas as pd  pd.set\_option('display.max\_columns', 500) # number of columns to be displayed  pd.set\_option('display.width', 1500)      # max table width to display  # import pytz module for working with time zone  import pytz     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # set time zone to UTC  timezone = pytz.timezone("Etc/UTC")  # create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset  utc\_from = datetime(2020, 1, 10, tzinfo=timezone)  utc\_to = datetime(2020, 1, 11, tzinfo=timezone)  # request AUDUSD ticks within 11.01.2020 - 11.01.2020  ticks = mt5.copy\_ticks\_range("AUDUSD", utc\_from, utc\_to, mt5.COPY\_TICKS\_ALL)  print("Ticks received:",len(ticks))     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()     # display data on each tick on a new line  print("Display obtained ticks 'as is'")  count = 0  for tick in ticks:      count+=1      print(tick)      if count >= 10:          break     # create DataFrame out of the obtained data  ticks\_frame = pd.DataFrame(ticks)  # convert time in seconds into the datetime format  ticks\_frame['time']=pd.to\_datetime(ticks\_frame['time'], unit='s')     # display data  print("\nDisplay dataframe with ticks")  print(ticks\_frame.head(10))      Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29     Ticks received: 37008  Display obtained ticks 'as is'  (1578614400, 0.68577, 0.68594, 0., 0, 1578614400820, 134, 0.)  (1578614401, 0.68578, 0.68594, 0., 0, 1578614401128, 130, 0.)  (1578614401, 0.68575, 0.68594, 0., 0, 1578614401128, 130, 0.)  (1578614411, 0.68576, 0.68594, 0., 0, 1578614411388, 130, 0.)  (1578614411, 0.68575, 0.68594, 0., 0, 1578614411560, 130, 0.)  (1578614414, 0.68576, 0.68595, 0., 0, 1578614414973, 134, 0.)  (1578614430, 0.68576, 0.68594, 0., 0, 1578614430188, 4, 0.)  (1578614450, 0.68576, 0.68595, 0., 0, 1578614450408, 4, 0.)  (1578614450, 0.68576, 0.68594, 0., 0, 1578614450519, 4, 0.)  (1578614456, 0.68575, 0.68594, 0., 0, 1578614456363, 130, 0.)     Display dataframe with ticks                   time      bid      ask  last  volume       time\_msc  flags  volume\_real  0 2020-01-10 00:00:00  0.68577  0.68594   0.0       0  1578614400820    134          0.0  1 2020-01-10 00:00:01  0.68578  0.68594   0.0       0  1578614401128    130          0.0  2 2020-01-10 00:00:01  0.68575  0.68594   0.0       0  1578614401128    130          0.0  3 2020-01-10 00:00:11  0.68576  0.68594   0.0       0  1578614411388    130          0.0  4 2020-01-10 00:00:11  0.68575  0.68594   0.0       0  1578614411560    130          0.0  5 2020-01-10 00:00:14  0.68576  0.68595   0.0       0  1578614414973    134          0.0  6 2020-01-10 00:00:30  0.68576  0.68594   0.0       0  1578614430188      4          0.0  7 2020-01-10 00:00:50  0.68576  0.68595   0.0       0  1578614450408      4          0.0  8 2020-01-10 00:00:50  0.68576  0.68594   0.0       0  1578614450519      4          0.0  9 2020-01-10 00:00:56  0.68575  0.68594   0.0       0  1578614456363    130          0.0 |

See also

[CopyRates](../../Timeseries-and-Indicators-Access/CopyRates/CopyRates.md), [copy\_rates\_from\_pos](../copy_rates_from_pos/copy_rates_from_pos.md), [copy\_rates\_range](../copy_rates_range/copy_rates_range.md), [copy\_ticks\_from](../copy_ticks_from/copy_ticks_from.md), [copy\_ticks\_range](copy_ticks_range.md)
