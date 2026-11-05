# version

version

Return the MetaTrader 5 terminal version.

|  |
| --- |
| version() |

Return Value

Return the MetaTrader 5 terminal version, build and release date. Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The version() function returns the terminal version, build and release date as a tuple of three values:

| Type | Description | Sample value |
| --- | --- | --- |
| integer | MetaTrader 5 terminal version | 500 |
| integer | Build | 2007 |
| string | Build release date | '25 Feb 2019' |

Example:

|  |
| --- |
| import MetaTrader5 as mt5  import pandas as pd  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # display data on MetaTrader 5 version  print(mt5.version())     # display data on connection status, server name and trading account 'as is'  print(mt5.terminal\_info())  print()     # get properties in the form of a dictionary  terminal\_info\_dict=mt5.terminal\_info().\_asdict()  # convert the dictionary into DataFrame and print  df=pd.DataFrame(list(terminal\_info\_dict.items()),columns=['property','value'])  print("terminal\_info() as dataframe:")  print(df[:-1])     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29  [500, 2367, '23 Mar 2020']  TerminalInfo(community\_account=True, community\_connection=True, connected=True, dlls\_allowed=False, trade\_allowed=False, ...     terminal\_info() as dataframe:                   property                         value  0       community\_account                          True  1    community\_connection                          True  2               connected                          True  3            dlls\_allowed                         False  4           trade\_allowed                         False  5       tradeapi\_disabled                         False  6           email\_enabled                         False  7             ftp\_enabled                         False  8   notifications\_enabled                         False  9                    mqid                         False  10                  build                          2367  11                maxbars                          5000  12               codepage                          1251  13              ping\_last                         77881  14      community\_balance                       707.107  15         retransmission                             0  16                company     MetaQuotes Software Corp.  17                   name                  MetaTrader 5  18               language                       Russian  19                   path  E:\ProgramFiles\MetaTrader 5  20              data\_path  E:\ProgramFiles\MetaTrader 5 |

See also

[initialize](../initialize/initialize.md), [shutdown](../shutdown/shutdown.md), [terminal\_info](../terminal_info/terminal_info.md)
