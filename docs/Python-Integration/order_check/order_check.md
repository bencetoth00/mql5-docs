# order_check

order\_check

Check funds sufficiency for performing a required [trading operation](../../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md). Check result are returned as the [MqlTradeCheckResult](../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) structure.

|  |
| --- |
| order\_check(     request      // request structure     ); |

Parameters

request

[in] [MqlTradeRequest](../order_send/order_send.md#traderequest) type structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below.

Return Value

Check result as the [MqlTradeCheckResult](../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) structure. The request field in the answer contains the structure of a trading request passed to order\_check().

Note

Successful sending of a request does not entail that the requested trading operation will be executed successfully. The order\_check function is similar to [OrderCheck](../../Trade-Functions/OrderCheck/OrderCheck.md).

TRADE\_REQUEST\_ACTIONS

| ID | Description |
| --- | --- |
| TRADE\_ACTION\_DEAL | Place an order for an instant deal with the specified parameters (set a market order) |
| TRADE\_ACTION\_PENDING | Place an order for performing a deal at specified conditions (pending order) |
| TRADE\_ACTION\_SLTP | Change open position Stop Loss and Take Profit |
| TRADE\_ACTION\_MODIFY | Change parameters of the previously placed trading order |
| TRADE\_ACTION\_REMOVE | Remove previously placed pending order |
| TRADE\_ACTION\_CLOSE\_BY | Close a position by an opposite one |

ORDER\_TYPE\_FILLING

| ID | Description |
| --- | --- |
| ORDER\_FILLING\_FOK | This execution policy means that an order can be executed only in the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The desired volume can be made up of several available offers. |
| ORDER\_FILLING\_IOC | An agreement to execute a deal at the maximum volume available in the market within the volume specified in the order. If the request cannot be filled completely, an order with the available volume will be executed, and the remaining volume will be canceled. |
| ORDER\_FILLING\_RETURN | This policy is used only for market (ORDER\_TYPE\_BUY and ORDER\_TYPE\_SELL), limit and stop limit orders (ORDER\_TYPE\_BUY\_LIMIT, ORDER\_TYPE\_SELL\_LIMIT, ORDER\_TYPE\_BUY\_STOP\_LIMIT and ORDER\_TYPE\_SELL\_STOP\_LIMIT) and only for the symbols with Market or Exchange execution [modes](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_trade_execution). If filled partially, a market or limit order with the remaining volume is not canceled, and is processed further.  During activation of the ORDER\_TYPE\_BUY\_STOP\_LIMIT and ORDER\_TYPE\_SELL\_STOP\_LIMIT orders, an appropriate limit order ORDER\_TYPE\_BUY\_LIMIT/ORDER\_TYPE\_SELL\_LIMIT with the ORDER\_FILLING\_RETURN type is created. |

ORDER\_TYPE\_TIME

| ID | Description |
| --- | --- |
| ORDER\_TIME\_GTC | The order stays in the queue until it is manually canceled |
| ORDER\_TIME\_DAY | The order is active only during the current trading day |
| ORDER\_TIME\_SPECIFIED | The order is active until the specified date |
| ORDER\_TIME\_SPECIFIED\_DAY | The order is active until 23:59:59 of the specified day. If this time appears to be out of a trading session, the expiration is processed at the nearest trading time. |

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # get account currency  account\_currency=mt5.account\_info().currency  print("Account currency:",account\_currency)     # prepare the request structure  symbol="USDJPY"  symbol\_info = mt5.symbol\_info(symbol)  if symbol\_info is None:      print(symbol, "not found, can not call order\_check()")      mt5.shutdown()      quit()     # if the symbol is unavailable in MarketWatch, add it  if not symbol\_info.visible:      print(symbol, "is not visible, trying to switch on")      if not mt5.symbol\_select(symbol,True):          print("symbol\_select({}}) failed, exit",symbol)          mt5.shutdown()          quit()     # prepare the request  point=mt5.symbol\_info(symbol).point  request = {      "action": mt5.TRADE\_ACTION\_DEAL,      "symbol": symbol,      "volume": 1.0,      "type": mt5.ORDER\_TYPE\_BUY,      "price": mt5.symbol\_info\_tick(symbol).ask,      "sl": mt5.symbol\_info\_tick(symbol).ask-100\*point,      "tp": mt5.symbol\_info\_tick(symbol).ask+100\*point,      "deviation": 10,      "magic": 234000,      "comment": "python script",      "type\_time": mt5.ORDER\_TIME\_GTC,      "type\_filling": mt5.ORDER\_FILLING\_RETURN,  }     # perform the check and display the result 'as is'  result = mt5.order\_check(request)  print(result);  # request the result as a dictionary and display it element by element  result\_dict=result.\_asdict()  for field in result\_dict.keys():      print("   {}={}".format(field,result\_dict[field]))      # if this is a trading request structure, display it element by element as well      if field=="request":          traderequest\_dict=result\_dict[field].\_asdict()          for tradereq\_filed in traderequest\_dict:              print("       traderequest: {}={}".format(tradereq\_filed,traderequest\_dict[tradereq\_filed]))     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29     Account currecy: USD     retcode=0     balance=101300.53     equity=68319.53     profit=-32981.0     margin=51193.67     margin\_free=17125.86     margin\_level=133.45308121101692     comment=Done     request=TradeRequest(action=1, magic=234000, order=0, symbol='USDJPY', volume=1.0, ...         traderequest: action=1         traderequest: magic=234000         traderequest: order=0         traderequest: symbol=USDJPY         traderequest: volume=1.0         traderequest: price=108.081         traderequest: stoplimit=0.0         traderequest: sl=107.98100000000001         traderequest: tp=108.181         traderequest: deviation=10         traderequest: type=0         traderequest: type\_filling=2         traderequest: type\_time=0         traderequest: expiration=0         traderequest: comment=python script         traderequest: position=0         traderequest: position\_by=0 |

See also

[order\_send](../order_send/order_send.md), [OrderCheck](../../Trade-Functions/OrderCheck/OrderCheck.md), [Trading operation types](../../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md), [Trading request structure](../../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md), [Structure of the trading request check results](../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md), [Structure of the trading request result](../../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md)
