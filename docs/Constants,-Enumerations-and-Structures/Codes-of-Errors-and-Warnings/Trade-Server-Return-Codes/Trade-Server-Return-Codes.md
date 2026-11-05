# Trade Server Return Codes

Return Codes of the Trade Server

All requests to execute trade operations are sent as a structure of a trade request [MqlTradeRequest](../../Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) using function [OrderSend()](../../../Trade-Functions/OrderSend/OrderSend.md). The function execution result is placed to structure [MqlTradeResult](../../Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md), whose retcode field contains the trade server return code.

| Code | Constant | Description |
| --- | --- | --- |
| 10004 | TRADE\_RETCODE\_REQUOTE | Requote |
| 10006 | TRADE\_RETCODE\_REJECT | Request rejected |
| 10007 | TRADE\_RETCODE\_CANCEL | Request canceled by trader |
| 10008 | TRADE\_RETCODE\_PLACED | Order placed |
| 10009 | TRADE\_RETCODE\_DONE | Request completed |
| 10010 | TRADE\_RETCODE\_DONE\_PARTIAL | Only part of the request was completed |
| 10011 | TRADE\_RETCODE\_ERROR | Request processing error |
| 10012 | TRADE\_RETCODE\_TIMEOUT | Request canceled by timeout |
| 10013 | TRADE\_RETCODE\_INVALID | Invalid request |
| 10014 | TRADE\_RETCODE\_INVALID\_VOLUME | Invalid volume in the request |
| 10015 | TRADE\_RETCODE\_INVALID\_PRICE | Invalid price in the request |
| 10016 | TRADE\_RETCODE\_INVALID\_STOPS | Invalid stops in the request |
| 10017 | TRADE\_RETCODE\_TRADE\_DISABLED | Trade is disabled |
| 10018 | TRADE\_RETCODE\_MARKET\_CLOSED | Market is closed |
| 10019 | TRADE\_RETCODE\_NO\_MONEY | There is not enough money to complete the request |
| 10020 | TRADE\_RETCODE\_PRICE\_CHANGED | Prices changed |
| 10021 | TRADE\_RETCODE\_PRICE\_OFF | There are no quotes to process the request |
| 10022 | TRADE\_RETCODE\_INVALID\_EXPIRATION | Invalid order expiration date in the request |
| 10023 | TRADE\_RETCODE\_ORDER\_CHANGED | Order state changed |
| 10024 | TRADE\_RETCODE\_TOO\_MANY\_REQUESTS | Too frequent requests |
| 10025 | TRADE\_RETCODE\_NO\_CHANGES | No changes in request |
| 10026 | TRADE\_RETCODE\_SERVER\_DISABLES\_AT | Autotrading disabled by server |
| 10027 | TRADE\_RETCODE\_CLIENT\_DISABLES\_AT | Autotrading disabled by client terminal |
| 10028 | TRADE\_RETCODE\_LOCKED | Request locked for processing |
| 10029 | TRADE\_RETCODE\_FROZEN | Order or position frozen |
| 10030 | TRADE\_RETCODE\_INVALID\_FILL | Invalid [order filling type](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) |
| 10031 | TRADE\_RETCODE\_CONNECTION | No connection with the trade server |
| 10032 | TRADE\_RETCODE\_ONLY\_REAL | Operation is allowed only for live accounts |
| 10033 | TRADE\_RETCODE\_LIMIT\_ORDERS | The number of pending orders has reached the limit |
| 10034 | TRADE\_RETCODE\_LIMIT\_VOLUME | The volume of orders and positions for the symbol has reached the limit |
| 10035 | TRADE\_RETCODE\_INVALID\_ORDER | Incorrect or prohibited [order type](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type) |
| 10036 | TRADE\_RETCODE\_POSITION\_CLOSED | Position with the specified [POSITION\_IDENTIFIER](../../Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_integer) has already been closed |
| 10038 | TRADE\_RETCODE\_INVALID\_CLOSE\_VOLUME | A close volume exceeds the current position volume |
| 10039 | TRADE\_RETCODE\_CLOSE\_ORDER\_EXIST | A close order already exists for a specified position. This may happen when working in the hedging system:   - when attempting to close a position with an opposite one, while close orders for the position already exist - when attempting to fully or partially close a position if the total volume of the already present close orders and the newly placed one exceeds the current position volume |
| 10040 | TRADE\_RETCODE\_LIMIT\_POSITIONS | The number of open positions simultaneously present on an account can be limited by the server settings. After a limit is reached, the server returns the TRADE\_RETCODE\_LIMIT\_POSITIONS error when attempting to place an order. The limitation operates differently depending on the position accounting type:   - Netting — number of open positions is considered. When a limit is reached, the platform does not let placing new orders whose execution may increase the number of open positions. In fact, the platform allows placing orders only for the symbols that already have open positions. The current pending orders are not considered since their execution may lead to changes in the current positions but it cannot increase their number. - Hedging — pending orders are considered together with open positions, since a pending order activation always leads to opening a new position. When a limit is reached, the platform does not allow placing both new market orders for opening positions and pending orders. |
| 10041 | TRADE\_RETCODE\_REJECT\_CANCEL | The pending order activation request is rejected, the order is canceled |
| 10042 | TRADE\_RETCODE\_LONG\_ONLY | The request is rejected, because the "Only long positions are allowed" rule is set for the symbol ([POSITION\_TYPE\_BUY](../../Trade-Constants/Position-Properties/Position-Properties.md#enum_position_type)) |
| 10043 | TRADE\_RETCODE\_SHORT\_ONLY | The request is rejected, because the "Only short positions are allowed" rule is set for the symbol ([POSITION\_TYPE\_SELL](../../Trade-Constants/Position-Properties/Position-Properties.md#enum_position_type)) |
| 10044 | TRADE\_RETCODE\_CLOSE\_ONLY | The request is rejected, because the "Only position closing is allowed" rule is set for the symbol |
| 10045 | TRADE\_RETCODE\_FIFO\_CLOSE | The request is rejected, because "Position closing is allowed only by FIFO rule" flag is set for the trading account ([ACCOUNT\_FIFO\_CLOSE](../../Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)=true) |
| 10046 | TRADE\_RETCODE\_HEDGE\_PROHIBITED | The request is rejected, because the "Opposite positions on a single symbol are disabled" rule is set for the trading account. For example, if the account has a Buy position, then a user cannot open a Sell position or place a pending sell order. The rule is only applied to accounts with hedging accounting system ([ACCOUNT\_MARGIN\_MODE](../../Environment-State/Account-Properties/Account-Properties.md#enum_account_margin_mode)=ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING). |
