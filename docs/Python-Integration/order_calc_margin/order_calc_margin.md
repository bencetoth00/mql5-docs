# order_calc_margin

order\_calc\_margin

Return margin in the account currency to perform a specified trading operation.

|  |
| --- |
| order\_calc\_margin(     action,      // order type (ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL)     symbol,      // symbol name     volume,      // volume     price        // open price     ) |

Parameters

action

[in]  Order type taking values from the [ORDER\_TYPE](order_calc_margin.md#order_type) enumeration. Required unnamed parameter.

symbol

[in]  Financial instrument name. Required unnamed parameter.

volume

[in]  Trading operation volume. Required unnamed parameter.

price

[in]  Open price. Required unnamed parameter.

Return Value

Real value if successful, otherwise None. The error info can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function allows estimating the margin necessary for a specified order type on the current account and in the current market environment without considering the current pending orders and open positions. The function is similar to [OrderCalcMargin](../../Trade-Functions/OrderCalcMargin/OrderCalcMargin.md).

ORDER\_TYPE

| ID | Description |
| --- | --- |
| ORDER\_TYPE\_BUY | Market buy order |
| ORDER\_TYPE\_SELL | Market sell order |
| ORDER\_TYPE\_BUY\_LIMIT | Buy Limit pending order |
| ORDER\_TYPE\_SELL\_LIMIT | Sell Limit pending order |
| ORDER\_TYPE\_BUY\_STOP | Buy Stop pending order |
| ORDER\_TYPE\_SELL\_STOP | Sell Stop pending order |
| ORDER\_TYPE\_BUY\_STOP\_LIMIT | Upon reaching the order price, Buy Limit pending order is placed at StopLimit price |
| ORDER\_TYPE\_SELL\_STOP\_LIMIT | Upon reaching the order price, Sell Limit pending order is placed at StopLimit price |
| ORDER\_TYPE\_CLOSE\_BY | Order for closing a position by an opposite one |

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # get account currency  account\_currency=mt5.account\_info().currency  print("Account currency:",account\_currency)     # arrange the symbol list  symbols=("EURUSD","GBPUSD","USDJPY", "USDCHF","EURJPY","GBPJPY")  print("Symbols to check margin:", symbols)  action=mt5.ORDER\_TYPE\_BUY  lot=0.1  for symbol in symbols:      symbol\_info=mt5.symbol\_info(symbol)      if symbol\_info is None:          print(symbol,"not found, skipped")          continue      if not symbol\_info.visible:          print(symbol, "is not visible, trying to switch on")          if not mt5.symbol\_select(symbol,True):              print("symbol\_select({}}) failed, skipped",symbol)              continue      ask=mt5.symbol\_info\_tick(symbol).ask      margin=mt5.order\_calc\_margin(action,symbol,lot,ask)      if margin != None:          print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account\_currency));      else:          print("order\_calc\_margin failed: , error code =", mt5.last\_error())     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29     Account currency: USD     Symbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'EURJPY', 'GBPJPY')     EURUSD buy 0.1 lot margin: 109.91 USD     GBPUSD buy 0.1 lot margin: 122.73 USD     USDJPY buy 0.1 lot margin: 100.0 USD     USDCHF buy 0.1 lot margin: 100.0 USD     EURJPY buy 0.1 lot margin: 109.91 USD     GBPJPY buy 0.1 lot margin: 122.73 USD |

See also

[order\_calc\_profit](../order_calc_profit/order_calc_profit.md), [order\_check](../order_check/order_check.md)
