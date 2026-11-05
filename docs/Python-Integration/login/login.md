# login

login

Connect to a trading account using specified parameters.

|  |
| --- |
| login(     login,                    // account number     password="PASSWORD",      // password     server="SERVER",          // server name as it is specified in the terminal     timeout=TIMEOUT           // timeout     ) |

Parameters

login

[in]  Trading account number. Required unnamed parameter.

password

[in]  Trading account password. Optional named parameter. If the password is not set, the password saved in the terminal database is applied automatically.

server

[in]  Trade server name. Optional named parameter. If no server is set, the last used server is applied automatically.

timeout=TIMEOUT

[in]  Connection timeout in milliseconds. Optional named parameter. If not specified, the value of 60 000 (60 seconds) is applied. If the connection is not established within the specified time, the call is forcibly terminated and the exception is generated.

Return Value

True in case of a successful connection to the trade account, otherwise – False.

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # display data on MetaTrader 5 version  print(mt5.version())  # connect to the trade account without specifying a password and a server  account=17221085  authorized=mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered  if authorized:      print("connected to account #{}".format(account))  else:      print("failed to connect at account #{}, error code: {}".format(account, mt5.last\_error()))     # now connect to another trading account specifying the password  account=25115284  authorized=mt5.login(account, password="gqrtz0lbdm")  if authorized:      # display trading account data 'as is'      print(mt5.account\_info())      # display trading account data in the form of a list      print("Show account\_info().\_asdict():")      account\_info\_dict = mt5.account\_info().\_asdict()      for prop in account\_info\_dict:          print("  {}={}".format(prop, account\_info\_dict[prop]))  else:      print("failed to connect at account #{}, error code: {}".format(account, mt5.last\_error()))     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29  [500, 2367, '23 Mar 2020']     connected to account #17221085     connected to account #25115284  AccountInfo(login=25115284, trade\_mode=0, leverage=100, limit\_orders=200, margin\_so\_mode=0, ...  account properties:     login=25115284     trade\_mode=0     leverage=100     limit\_orders=200     margin\_so\_mode=0     trade\_allowed=True     trade\_expert=True     margin\_mode=2     currency\_digits=2     fifo\_close=False     balance=99588.33     credit=0.0     profit=-45.23     equity=99543.1     margin=54.37     margin\_free=99488.73     margin\_level=183084.6054809638     margin\_so\_call=50.0     margin\_so\_so=30.0     margin\_initial=0.0     margin\_maintenance=0.0     assets=0.0     liabilities=0.0     commission\_blocked=0.0     name=James Smith     server=MetaQuotes-Demo     currency=USD     company=MetaQuotes Software Corp. |

See also

[initialize](../initialize/initialize.md), [shutdown](../shutdown/shutdown.md)
