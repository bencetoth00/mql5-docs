# order_calc_profit

order\_calc\_profit

Return profit in the account currency for a specified trading operation.

|  |
| --- |
| order\_calc\_profit(     action,          // order type (ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL)     symbol,          // symbol name     volume,          // volume     price\_open,      // open price     price\_close      // close price     ); |

Parameters

action

[in]  Order type may take one of the two [ORDER\_TYPE](../order_calc_margin/order_calc_margin.md#order_type) enumeration values: ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL. Required unnamed parameter.

symbol

[in]  Financial instrument name. Required unnamed parameter.

volume

[in]  Trading operation volume. Required unnamed parameter.

price\_open

[in]  Open price. Required unnamed parameter.

price\_close

[in]  Close price. Required unnamed parameter.

Return Value

Real value if successful, otherwise None. The error info can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function allows estimating a trading operation result on the current account and in the current trading environment. The function is similar to [OrderCalcProfit](../../Trade-Functions/OrderCalcProfit/OrderCalcProfit.md).

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # get account currency  account\_currency=mt5.account\_info().currency  print("Account currency:",account\_currency)     # arrange the symbol list  symbols = ("EURUSD","GBPUSD","USDJPY")  print("Symbols to check margin:", symbols)  # estimate profit for buying and selling  lot=1.0  distance=300  for symbol in symbols:      symbol\_info=mt5.symbol\_info(symbol)      if symbol\_info is None:          print(symbol,"not found, skipped")          continue      if not symbol\_info.visible:          print(symbol, "is not visible, trying to switch on")          if not mt5.symbol\_select(symbol,True):              print("symbol\_select({}}) failed, skipped",symbol)              continue      point=mt5.symbol\_info(symbol).point      symbol\_tick=mt5.symbol\_info\_tick(symbol)      ask=symbol\_tick.ask      bid=symbol\_tick.bid      buy\_profit=mt5.order\_calc\_profit(mt5.ORDER\_TYPE\_BUY,symbol,lot,ask,ask+distance\*point)      if buy\_profit!=None:          print("   buy {} {} lot: profit on {} points => {} {}".format(symbol,lot,distance,buy\_profit,account\_currency));      else:          print("order\_calc\_profit(ORDER\_TYPE\_BUY) failed, error code =",mt5.last\_error())      sell\_profit=mt5.order\_calc\_profit(mt5.ORDER\_TYPE\_SELL,symbol,lot,bid,bid-distance\*point)      if sell\_profit!=None:          print("   sell {} {} lots: profit on {} points => {} {}".format(symbol,lot,distance,sell\_profit,account\_currency));      else:          print("order\_calc\_profit(ORDER\_TYPE\_SELL) failed, error code =",mt5.last\_error())      print()     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29     Account currency: USD  Symbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY')     buy EURUSD 1.0 lot: profit on 300 points => 300.0 USD     sell EURUSD 1.0 lot: profit on 300 points => 300.0 USD        buy GBPUSD 1.0 lot: profit on 300 points => 300.0 USD     sell GBPUSD 1.0 lot: profit on 300 points => 300.0 USD        buy USDJPY 1.0 lot: profit on 300 points => 276.54 USD     sell USDJPY 1.0 lot: profit on 300 points => 278.09 USD |

See also

[order\_calc\_margin](../order_calc_margin/order_calc_margin.md), [order\_check](../order_check/order_check.md)
