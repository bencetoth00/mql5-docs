# symbol_info_tick

symbol\_info\_tick

Get the last tick for the specified financial instrument.

|  |
| --- |
| symbol\_info\_tick(     symbol      // financial instrument name  ) |

symbol

[in]  Financial instrument name. Required unnamed parameter.

Return Value

Return info in the form of a tuple. Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function is similar to [SymbolInfoTick](../../Market-Info/SymbolInfoTick/SymbolInfoTick.md).

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # attempt to enable the display of the GBPUSD in MarketWatch  selected=mt5.symbol\_select("GBPUSD",True)  if not selected:      print("Failed to select GBPUSD")      mt5.shutdown()      quit()     # display the last GBPUSD tick  lasttick=mt5.symbol\_info\_tick("GBPUSD")  print(lasttick)  # display tick field values in the form of a list  print("Show symbol\_info\_tick(\"GBPUSD\").\_asdict():")  symbol\_info\_tick\_dict = mt5.symbol\_info\_tick("GBPUSD").\_asdict()  for prop in symbol\_info\_tick\_dict:      print("  {}={}".format(prop, symbol\_info\_tick\_dict[prop]))     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29  Tick(time=1585070338, bid=1.17264, ask=1.17279, last=0.0, volume=0, time\_msc=1585070338728, flags=2, volume\_real=0.0)  Show symbol\_info\_tick.\_asdict():    time=1585070338    bid=1.17264    ask=1.17279    last=0.0    volume=0    time\_msc=1585070338728    flags=2    volume\_real=0.0 |

See also

[symbol\_info](../symbol_info/symbol_info.md), [symbol\_info](../symbol_info/symbol_info.md)
