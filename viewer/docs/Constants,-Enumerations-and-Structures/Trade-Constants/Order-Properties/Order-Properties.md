# Order Properties


Requests to execute trade operations are formalized as orders. Each order has a variety of properties for reading. Information on them can be obtained using functions OrderGet...() and HistoryOrderGet...().

For functions [OrderGetInteger()](../../../Trade-Functions/OrderGetInteger/OrderGetInteger.md) and [HistoryOrderGetInteger()](../../../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md)

ENUM\_ORDER\_PROPERTY\_INTEGER

| Identifier | Description | Type |
| --- | --- | --- |
| ORDER\_TICKET | Order ticket. Unique number assigned to each order | long |
| ORDER\_TIME\_SETUP | Order setup time | datetime |
| ORDER\_TYPE | Order type | [ENUM\_ORDER\_TYPE](Order-Properties.md#enum_order_type) |
| ORDER\_STATE | Order state | [ENUM\_ORDER\_STATE](Order-Properties.md#enum_order_state) |
| ORDER\_TIME\_EXPIRATION | Order expiration time | datetime |
| ORDER\_TIME\_DONE | Order execution or cancellation time | datetime |
| ORDER\_TIME\_SETUP\_MSC | The time of placing an order for execution in milliseconds since 01.01.1970 | long |
| ORDER\_TIME\_DONE\_MSC | Order execution/cancellation time in milliseconds since 01.01.1970 | long |
| ORDER\_TYPE\_FILLING | Order filling type | [ENUM\_ORDER\_TYPE\_FILLING](Order-Properties.md#enum_order_type_filling) |
| ORDER\_TYPE\_TIME | Order lifetime | [ENUM\_ORDER\_TYPE\_TIME](Order-Properties.md#enum_order_type_time) |
| ORDER\_MAGIC | ID of an Expert Advisor that has placed the order (designed to ensure that each Expert Advisor places its own unique number) | long |
| ORDER\_REASON | The reason or source for placing an order | [ENUM\_ORDER\_REASON](Order-Properties.md#enum_order_reason) |
| ORDER\_POSITION\_ID | [Position identifier](../Position-Properties/Position-Properties.md#enum_position_property_integer) that is set to an order as soon as it is executed. Each executed order results in a [deal](../Deal-Properties/Deal-Properties.md) that opens or modifies an already existing position. The identifier of exactly this position is set to the executed order at this moment. | long |
| ORDER\_POSITION\_BY\_ID | Identifier of an opposite position used for closing by order  ORDER\_TYPE\_CLOSE\_BY | long |

For functions [OrderGetDouble()](../../../Trade-Functions/OrderGetDouble/OrderGetDouble.md) and [HistoryOrderGetDouble()](../../../Trade-Functions/HistoryOrderGetDouble/HistoryOrderGetDouble.md)

ENUM\_ORDER\_PROPERTY\_DOUBLE

| Identifier | Description | Type |
| --- | --- | --- |
| ORDER\_VOLUME\_INITIAL | Order initial volume | double |
| ORDER\_VOLUME\_CURRENT | Order current volume | double |
| ORDER\_PRICE\_OPEN | Price specified in the order | double |
| ORDER\_SL | Stop Loss value | double |
| ORDER\_TP | Take Profit value | double |
| ORDER\_PRICE\_CURRENT | The current price of the order symbol | double |
| ORDER\_PRICE\_STOPLIMIT | The Limit order price for the StopLimit order | double |

For functions [OrderGetString()](../../../Trade-Functions/OrderGetString/OrderGetString.md) and [HistoryOrderGetString()](../../../Trade-Functions/HistoryOrderGetString/HistoryOrderGetString.md)

ENUM\_ORDER\_PROPERTY\_STRING

| Identifier | Description | Type |
| --- | --- | --- |
| ORDER\_SYMBOL | Symbol of the order | string |
| ORDER\_COMMENT | Order comment | string |
| ORDER\_EXTERNAL\_ID | Order identifier in an external trading system (on the Exchange) | string |

 

When sending a trade request using the [OrderSend()](../../../Trade-Functions/OrderSend/OrderSend.md) function, some operations require the indication of the order type. The order type is specified in the type field of the special structure [MqlTradeRequest](../../Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md), and can accept values of the ENUM\_ORDER\_TYPE enumeration.

ENUM\_ORDER\_TYPE

| Identifier | Description |
| --- | --- |
| ORDER\_TYPE\_BUY | Market Buy order |
| ORDER\_TYPE\_SELL | Market Sell order |
| ORDER\_TYPE\_BUY\_LIMIT | Buy Limit pending order |
| ORDER\_TYPE\_SELL\_LIMIT | Sell Limit pending order |
| ORDER\_TYPE\_BUY\_STOP | Buy Stop pending order |
| ORDER\_TYPE\_SELL\_STOP | Sell Stop pending order |
| ORDER\_TYPE\_BUY\_STOP\_LIMIT | Upon reaching the order price, a pending Buy Limit order is placed at the StopLimit price |
| ORDER\_TYPE\_SELL\_STOP\_LIMIT | Upon reaching the order price, a pending Sell Limit order is placed at the StopLimit price |
| ORDER\_TYPE\_CLOSE\_BY | Order to close a position by an opposite one |

 

Each order has a status that describes its state. To obtain information, use [OrderGetInteger()](../../../Trade-Functions/OrderGetInteger/OrderGetInteger.md) or [HistoryOrderGetInteger()](../../../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) with the ORDER\_STATE modifier. Allowed values are stored in the ENUM\_ORDER\_STATE enumeration.

ENUM\_ORDER\_STATE

| Identifier | Description |
| --- | --- |
| ORDER\_STATE\_STARTED | Order checked, but not yet accepted by broker |
| ORDER\_STATE\_PLACED | Order accepted |
| ORDER\_STATE\_CANCELED | Order canceled by client |
| ORDER\_STATE\_PARTIAL | Order partially executed |
| ORDER\_STATE\_FILLED | Order fully executed |
| ORDER\_STATE\_REJECTED | Order rejected |
| ORDER\_STATE\_EXPIRED | Order expired |
| ORDER\_STATE\_REQUEST\_ADD | Order is being registered (placing to the trading system) |
| ORDER\_STATE\_REQUEST\_MODIFY | Order is being modified (changing its parameters) |
| ORDER\_STATE\_REQUEST\_CANCEL | Order is being deleted (deleting from the trading system) |

 

When sending a trade request for execution at the current time (time in force), the price and the required buy/sell volume should be specified. Also, keep in mind that financial markets provide no guarantee that the entire requested volume is available for a certain financial instrument at the desired price. Therefore, trading operations in real time are regulated using the price and volume execution modes. The modes, or execution policies, define the rules for cases when the price has changed or the requested volume cannot be completely fulfilled at the moment.

Price execution mode can be obtained from the [SYMBOL\_TRADE\_EXEMODE](../../Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_trade_execution) symbol property containing the combination of flags from the  [ENUM\_SYMBOL\_TRADE\_EXECUTION](../../Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_trade_execution) enumeration.

| Execution mode | Description | The value in [ENUM\_SYMBOL\_TRADE\_EXECUTION](../../Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_trade_execution) |
| --- | --- | --- |
| Execution mode     (Request Execution) | Executing a market order at the price previously received from the broker.     Prices for a certain market order are requested from the broker before the order is sent. Upon receiving the prices, order execution at the given price can be either confirmed or rejected. | SYMBOL\_TRADE\_EXECUTION\_REQUEST |
| Instant Execution     (Instant Execution) | Executing a market order at the specified price immediately.     When sending a trade request to be executed, the platform automatically adds the current prices to the order.   - If the broker accepts the price, the order is executed. - If the broker does not accept the requested price, a "Requote" is sent — the broker returns prices, at which this order can be executed. | SYMBOL\_TRADE\_EXECUTION\_INSTANT |
| Market Execution     (Market Execution) | A broker makes a decision about the order execution price without any additional discussion with the trader.     Sending the order in such a mode means advance consent to its execution at this price. | SYMBOL\_TRADE\_EXECUTION\_MARKET |
| Exchange Execution     (Exchange Execution) | Trade operations are executed at the prices of the current market offers. | SYMBOL\_TRADE\_EXECUTION\_EXCHANGE |

Volume filling policy is specified in the [ORDER\_TYPE\_FILLING](Order-Properties.md) order property and may contain only the values from the ENUM\_ORDER\_TYPE\_FILLING enumeration

| Fill policy | Description | The value in [ENUM\_ORDER\_TYPE\_FILLING](Order-Properties.md#enum_order_type_filling) |
| --- | --- | --- |
| Fill or Kill | An order can be executed in the specified volume only.     If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed.     The desired volume can be made up of several available offers.     The possibility of using FOK orders is determined at the trade server. | ORDER\_FILLING\_FOK |
| Immediate or Cancel | A trader agrees to execute a deal with the volume maximally available in the market within that indicated in the order.     If the request cannot be filled completely, an order with the available volume will be executed, and the remaining volume will be canceled.     The possibility of using IOC orders is determined at the trade server. | ORDER\_FILLING\_IOC |
| Passive (Book or Cancel) | The BoC order assumes that the order can only be placed in the Depth of Market and cannot be immediately executed. If the order can be executed immediately when placed, then it is canceled.     In fact, the BOC policy guarantees that the price of the placed order will be worse than the current market. BoC orders are used to implement passive trading, so that the order is not executed immediately when placed and does not affect current liquidity.     Only limit and stop limit orders are supported (ORDER\_TYPE\_BUY\_LIMIT, ORDER\_TYPE\_SELL\_LIMIT, ORDER\_TYPE\_BUY\_STOP\_LIMIT, ORDER\_TYPE\_SELL\_STOP\_LIMIT). | ORDER\_FILLING\_BOC |
| Return | In case of partial filling, an order with remaining volume is not canceled but processed further.     Return orders are not allowed in the Market Execution mode (market execution — SYMBOL\_TRADE\_EXECUTION\_MARKET). | ORDER\_FILLING\_RETURN |

When sending a trade request using the [OrderSend()](../../../Trade-Functions/OrderSend/OrderSend.md) function, the necessary volume execution policy can be set in the type\_filling field, namely in the special [MqlTradeRequest](../../Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) structure. The values from the ENUM\_ORDER\_TYPE\_FILLING enumeration are available. To get the property value in a specific active/completed order, use the [OrderGetInteger()](../../../Trade-Functions/OrderGetInteger/OrderGetInteger.md) or [HistoryOrderGetInteger()](../../../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) function with the ORDER\_TYPE\_FILLING modifier.

Before sending an order with the current execution time, for the correct setting of the [ORDER\_TYPE\_FILLING](Order-Properties.md#enum_order_property_integer) value (volume execution type), you can use the [SymbolInfoInteger()](../../../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) function with each financial instrument to get the [SYMBOL\_FILLING\_MODE](../../Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_info_integer) property value, which shows [volume execution types](../../Environment-State/Symbol-Properties/Symbol-Properties.md#symbol_filling_mode) allowed for the symbol as a combination of flags. The ORDER\_FILLING\_RETURN filling type is enabled at all times except for the "Market execution" mode (SYMBOL\_TRADE\_EXECUTION\_MARKET).

The use of filling types depending on the execution mode can be shown as the following table:

| Type of Execution\Fill Policy | Fill or Kill (FOK ORDER\_FILLING\_FOK) | Immediate or Cancel (IOC ORDER\_FILLING\_IOC) | Return (Return ORDER\_FILLING\_RETURN) |
| --- | --- | --- | --- |
| Instant Execution     (SYMBOL\_TRADE\_EXECUTION\_INSTANT) | + (regardless of a symbol setting) | + (regardless of a symbol setting) | + (always) |
| Request Execution     SYMBOL\_TRADE\_EXECUTION\_REQUEST | + (regardless of a symbol setting) | + (regardless of a symbol setting) | + (always) |
| Market Execution     SYMBOL\_TRADE\_EXECUTION\_MARKET | + (set in the symbol settings) | + (set in the symbol settings) | - (disabled regardless of the symbol settings) |
| Exchange Execution     SYMBOL\_TRADE\_EXECUTION\_EXCHANGE | + (set in the symbol settings) | + (set in the symbol settings) | + (always) |

In case of pending orders, the ORDER\_FILLING\_RETURN filling type should be used regardless of an execution type ([SYMBOL\_TRADE\_EXEMODE](../../Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_trade_execution)), since such orders are not meant for execution at the time of sending. When using pending orders, a trader agrees in advance that, when conditions for a deal on this order are met, the broker will use the filling type supported by the exchange.

 

The order validity period can be set in the type\_time field of the special structure [MqlTradeRequest](../../Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) when sending a trade request using the [OrderSend()](../../../Trade-Functions/OrderSend/OrderSend.md) function. Values of the ENUM\_ORDER\_TYPE\_TIME enumeration are allowed. To obtain the value of this property use the function [OrderGetInteger()](../../../Trade-Functions/OrderGetInteger/OrderGetInteger.md) or [HistoryOrderGetInteger()](../../../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) with the ORDER\_TYPE\_TIME modifier.

ENUM\_ORDER\_TYPE\_TIME

| Identifier | Description |
| --- | --- |
| ORDER\_TIME\_GTC | Good till cancel order |
| ORDER\_TIME\_DAY | Good till current trade day order |
| ORDER\_TIME\_SPECIFIED | Good till expired order |
| ORDER\_TIME\_SPECIFIED\_DAY | The order will be effective till 23:59:59 of the specified day. If this time is outside a trading session, the order expires in the nearest trading time. |

 

The reason for order placing is contained in the ORDER\_REASON property. An order can be placed by an MQL5 program, from a mobile application, as a result of StopOut, etc. Possible values of ORDER\_REASON are described in the ENUM\_ORDER\_REASON enumeration.

ENUM\_ORDER\_REASON

| Identifier | Description |
| --- | --- |
| ORDER\_REASON\_CLIENT | The order was placed from a desktop terminal |
| ORDER\_REASON\_MOBILE | The order was placed from a mobile application |
| ORDER\_REASON\_WEB | The order was placed from a web platform |
| ORDER\_REASON\_EXPERT | The order was placed from an MQL5-program, i.e. by an Expert Advisor or a script |
| ORDER\_REASON\_SL | The order was placed as a result of Stop Loss activation |
| ORDER\_REASON\_TP | The order was placed as a result of Take Profit activation |
| ORDER\_REASON\_SO | The order was placed as a result of the Stop Out event |
