# symbols_total

symbols\_total

Get the number of all financial instruments in the MetaTrader 5 terminal.

|  |
| --- |
| symbols\_total() |

Return Value

Integer value.

Note

The function is similar to [SymbolsTotal()](../../Market-Info/SymbolsTotal/SymbolsTotal.md). However, it returns the number of all symbols including [custom](../../Custom-Symbols/Custom-Symbols.md) ones and the ones disabled in [MarketWatch](https://www.metatrader5.com/en/terminal/help/trading/market_watch).

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # get the number of financial instruments  symbols=mt5.symbols\_total()  if symbols>0:      print("Total symbols =",symbols)  else:      print("symbols not found")     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown() |

See also

[symbols\_get](../symbols_get/symbols_get.md), [symbol\_select](../symbol_select/symbol_select.md), [symbol\_info](../symbol_info/symbol_info.md)
