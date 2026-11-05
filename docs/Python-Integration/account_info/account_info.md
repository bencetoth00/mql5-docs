# account_info

account\_info

Get info on the current trading account.

|  |
| --- |
| account\_info() |

Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function returns all data that can be obtained using [AccountInfoInteger](../../Account-Information/AccountInfoInteger/AccountInfoInteger.md), [AccountInfoDouble](../../Account-Information/AccountInfoDouble/AccountInfoDouble.md) and [AccountInfoString](../../Account-Information/AccountInfoString/AccountInfoString.md) in one call.

Example:

|  |
| --- |
| import MetaTrader5 as mt5  import pandas as pd  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # connect to the trade account specifying a password and a server  authorized=mt5.login(25115284, password="gqz0343lbdm")  if authorized:      account\_info=mt5.account\_info()      if account\_info!=None:          # display trading account data 'as is'          print(account\_info)          # display trading account data in the form of a dictionary          print("Show account\_info().\_asdict():")          account\_info\_dict = mt5.account\_info().\_asdict()          for prop in account\_info\_dict:              print("  {}={}".format(prop, account\_info\_dict[prop]))          print()             # convert the dictionary into DataFrame and print          df=pd.DataFrame(list(account\_info\_dict.items()),columns=['property','value'])          print("account\_info() as dataframe:")          print(df)  else:      print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last\_error())     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29  AccountInfo(login=25115284, trade\_mode=0, leverage=100, limit\_orders=200, margin\_so\_mode=0, ....  Show account\_info().\_asdict():    login=25115284    trade\_mode=0    leverage=100    limit\_orders=200    margin\_so\_mode=0    trade\_allowed=True    trade\_expert=True    margin\_mode=2    currency\_digits=2    fifo\_close=False    balance=99511.4    credit=0.0    profit=41.82    equity=99553.22    margin=98.18    margin\_free=99455.04    margin\_level=101398.67590140559    margin\_so\_call=50.0    margin\_so\_so=30.0    margin\_initial=0.0    margin\_maintenance=0.0    assets=0.0    liabilities=0.0    commission\_blocked=0.0    server=MetaQuotes-Demo    currency=USD    company=MetaQuotes Software Corp.     account\_info() as dataframe                property                      value  0                login                   25115284  1           trade\_mode                          0  2             leverage                        100  3         limit\_orders                        200  4       margin\_so\_mode                          0  5        trade\_allowed                       True  6         trade\_expert                       True  7          margin\_mode                          2  8      currency\_digits                          2  9           fifo\_close                      False  10             balance                    99588.3  11              credit                          0  12              profit                     -45.13  13              equity                    99543.2  14              margin                      54.37  15         margin\_free                    99488.8  16        margin\_level                     183085  17      margin\_so\_call                         50  18        margin\_so\_so                         30  19      margin\_initial                          0  20  margin\_maintenance                          0  21              assets                          0  22         liabilities                          0  23  commission\_blocked                          0  24                name                James Smith  25              server            MetaQuotes-Demo  26            currency                        USD  27             company  MetaQuotes Software Corp. |

See also

[initialize](../initialize/initialize.md), [shutdown](../shutdown/shutdown.md), [login](../login/login.md)
