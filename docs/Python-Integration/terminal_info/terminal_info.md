# terminal_info

terminal\_info

Get the connected MetaTrader 5 client terminal status and settings.

|  |
| --- |
| terminal\_info() |

Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function returns all data that can be obtained using [TerminalInfoInteger](../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md), [TerminalInfoDouble](../../Checkup/TerminalInfoDouble/TerminalInfoDouble.md) and [TerminalInfoDouble](../../Checkup/TerminalInfoDouble/TerminalInfoDouble.md) in one call.

Example:

|  |
| --- |
| import MetaTrader5 as mt5  import pandas as pd  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # display data on MetaTrader 5 version  print(mt5.version())  # display info on the terminal settings and status  terminal\_info=mt5.terminal\_info()  if terminal\_info!=None:      # display the terminal data 'as is'      print(terminal\_info)      # display data in the form of a list      print("Show terminal\_info().\_asdict():")      terminal\_info\_dict = mt5.terminal\_info().\_asdict()      for prop in terminal\_info\_dict:          print("  {}={}".format(prop, terminal\_info\_dict[prop]))      print()     # convert the dictionary into DataFrame and print      df=pd.DataFrame(list(terminal\_info\_dict.items()),columns=['property','value'])      print("terminal\_info() as dataframe:")      print(df)     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29  [500, 2366, '20 Mar 2020']  TerminalInfo(community\_account=True, community\_connection=True, connected=True,....  Show terminal\_info().\_asdict():    community\_account=True    community\_connection=True    connected=True    dlls\_allowed=False    trade\_allowed=False    tradeapi\_disabled=False    email\_enabled=False    ftp\_enabled=False    notifications\_enabled=False    mqid=False    build=2366    maxbars=5000    codepage=1251    ping\_last=77850    community\_balance=707.10668201585    retransmission=0.0    company=MetaQuotes Software Corp.    name=MetaTrader 5    language=Russian    path=E:\ProgramFiles\MetaTrader 5    data\_path=E:\ProgramFiles\MetaTrader 5    commondata\_path=C:\Users\Rosh\AppData\Roaming\MetaQuotes\Terminal\Common     terminal\_info() as dataframe:                   property                      value  0       community\_account                       True  1    community\_connection                       True  2               connected                       True  3            dlls\_allowed                      False  4           trade\_allowed                      False  5       tradeapi\_disabled                      False  6           email\_enabled                      False  7             ftp\_enabled                      False  8   notifications\_enabled                      False  9                    mqid                      False  10                  build                       2367  11                maxbars                       5000  12               codepage                       1251  13              ping\_last                      80953  14      community\_balance                    707.107  15         retransmission                   0.063593  16                company  MetaQuotes Software Corp.  17                   name               MetaTrader 5  18               language                    Russian |

See also

[initialize](../initialize/initialize.md), [shutdown](../shutdown/shutdown.md), [version](../version/version.md)
