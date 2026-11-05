# copy_rates_from

copy\_rates\_from

Get bars from the MetaTrader 5 terminal starting from the specified date.

|  |
| --- |
| copy\_rates\_from(     symbol,       // symbol name     timeframe,    // timeframe     date\_from,    // initial bar open date     count         // number of bars     ) |

Parameters

symbol

[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.

timeframe

[in]  Timeframe the bars are requested for. Set by a value from the [TIMEFRAME](copy_rates_from.md#timeframe) enumeration. Required unnamed parameter.

date\_from

[in]  Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

count

[in]  Number of bars to receive. Required unnamed parameter.

Return Value

Returns bars as the numpy array with the named time, open, high, low, close, tick\_volume, spread and real\_volume columns. Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

See the [CopyRates()](../../Timeseries-and-Indicators-Access/CopyRates/CopyRates.md) function for more information.

Only data whose date is less than (earlier) or equal to the date specified will be returned. It means, the open time of any bar is always less or equal to the specified one.

MetaTrader 5 terminal provides bars only within a history available to a user on charts. The number of bars available to users is set in the "[Max. bars in chart](https://www.metatrader5.com/en/terminal/help/startworking/settings#max_bars)" parameter.

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. Data received from the MetaTrader 5 terminal has UTC time.  

TIMEFRAME is an enumeration with possible chart period values

| ID | Description |
| --- | --- |
| TIMEFRAME\_M1 | 1 minute |
| TIMEFRAME\_M2 | 2 minutes |
| TIMEFRAME\_M3 | 3 minutes |
| TIMEFRAME\_M4 | 4 minutes |
| TIMEFRAME\_M5 | 5 minutes |
| TIMEFRAME\_M6 | 6 minutes |
| TIMEFRAME\_M10 | 10 minutes |
| TIMEFRAME\_M12 | 12 minutes |
| TIMEFRAME\_M12 | 15 minutes |
| TIMEFRAME\_M20 | 20 minutes |
| TIMEFRAME\_M30 | 30 minutes |
| TIMEFRAME\_H1 | 1 hour |
| TIMEFRAME\_H2 | 2 hours |
| TIMEFRAME\_H3 | 3 hours |
| TIMEFRAME\_H4 | 4 hours |
| TIMEFRAME\_H6 | 6 hours |
| TIMEFRAME\_H8 | 8 hours |
| TIMEFRAME\_H12 | 12 hours |
| TIMEFRAME\_D1 | 1 day |
| TIMEFRAME\_W1 | 1 week |
| TIMEFRAME\_MN1 | 1 month |

 

Example:

|  |
| --- |
| from datetime import datetime  import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # import the 'pandas' module for displaying data obtained in the tabular form  import pandas as pd  pd.set\_option('display.max\_columns', 500) # number of columns to be displayed  pd.set\_option('display.width', 1500)      # max table width to display  # import pytz module for working with time zone  import pytz     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # set time zone to UTC  timezone = pytz.timezone("Etc/UTC")  # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset  utc\_from = datetime(2020, 1, 10, tzinfo=timezone)  # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone  rates = mt5.copy\_rates\_from("EURUSD", mt5.TIMEFRAME\_H4, utc\_from, 10)     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()  # display each element of obtained data in a new line  print("Display obtained data 'as is'")  for rate in rates:      print(rate)     # create DataFrame out of the obtained data  rates\_frame = pd.DataFrame(rates)  # convert time in seconds into the datetime format  rates\_frame['time']=pd.to\_datetime(rates\_frame['time'], unit='s')                               # display data  print("\nDisplay dataframe with data")  print(rates\_frame)          Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29     Display obtained data 'as is'  (1578484800, 1.11382, 1.11385, 1.1111, 1.11199, 9354, 1, 0)  (1578499200, 1.11199, 1.11308, 1.11086, 1.11179, 10641, 1, 0)  (1578513600, 1.11178, 1.11178, 1.11016, 1.11053, 4806, 1, 0)  (1578528000, 1.11053, 1.11193, 1.11033, 1.11173, 3480, 1, 0)  (1578542400, 1.11173, 1.11189, 1.11126, 1.11182, 2236, 1, 0)  (1578556800, 1.11181, 1.11203, 1.10983, 1.10993, 7984, 1, 0)  (1578571200, 1.10994, 1.11173, 1.10965, 1.11148, 7406, 1, 0)  (1578585600, 1.11149, 1.11149, 1.10923, 1.11046, 7468, 1, 0)  (1578600000, 1.11046, 1.11097, 1.11033, 1.11051, 3450, 1, 0)  (1578614400, 1.11051, 1.11093, 1.11017, 1.11041, 2448, 1, 0)     Display dataframe with data                   time     open     high      low    close  tick\_volume  spread  real\_volume  0 2020-01-08 12:00:00  1.11382  1.11385  1.11110  1.11199         9354       1            0  1 2020-01-08 16:00:00  1.11199  1.11308  1.11086  1.11179        10641       1            0  2 2020-01-08 20:00:00  1.11178  1.11178  1.11016  1.11053         4806       1            0  3 2020-01-09 00:00:00  1.11053  1.11193  1.11033  1.11173         3480       1            0  4 2020-01-09 04:00:00  1.11173  1.11189  1.11126  1.11182         2236       1            0  5 2020-01-09 08:00:00  1.11181  1.11203  1.10983  1.10993         7984       1            0  6 2020-01-09 12:00:00  1.10994  1.11173  1.10965  1.11148         7406       1            0  7 2020-01-09 16:00:00  1.11149  1.11149  1.10923  1.11046         7468       1            0  8 2020-01-09 20:00:00  1.11046  1.11097  1.11033  1.11051         3450       1            0  9 2020-01-10 00:00:00  1.11051  1.11093  1.11017  1.11041         2448       1            0 |

See also

[CopyRates](../../Timeseries-and-Indicators-Access/CopyRates/CopyRates.md), [copy\_rates\_from\_pos](../copy_rates_from_pos/copy_rates_from_pos.md), [copy\_rates\_range](../copy_rates_range/copy_rates_range.md), [copy\_ticks\_from](../copy_ticks_from/copy_ticks_from.md), [copy\_ticks\_range](../copy_ticks_range/copy_ticks_range.md)
