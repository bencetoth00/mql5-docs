# shutdown

shutdown

Close the previously established connection to the MetaTrader 5 terminal.

|  |
| --- |
| shutdown() |

Return Value

None.

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed")      quit()     # display data on connection status, server name and trading account  print(mt5.terminal\_info())  # display data on MetaTrader 5 version  print(mt5.version())     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown() |

See also

[initialize](../initialize/initialize.md), [login\_py](../login/login.md), [terminal\_info](../terminal_info/terminal_info.md), [version](../version/version.md)
