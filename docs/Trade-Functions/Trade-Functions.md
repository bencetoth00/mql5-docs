# Trade Functions

Trade Functions

This is the group of functions intended for managing trading activities.

Before you proceed to study the trade functions of the platform, you must have a clear understanding of the basic terms: order, deal and position:

- An order is an instruction given to a broker to buy or sell a financial instrument. There are two main types of orders: Market and Pending. In addition, there are special Take Profit and Stop Loss levels.
- A deal is the commercial exchange (buying or selling) of a financial security. Buying is executed at the demand price (Ask), and Sell is performed at the supply price (Bid). A deal can be opened as a result of market order execution or pending order triggering. Note that in some cases, execution of an order can result in several deals.
- A position is a trade obligation, i.e. the number of bought or sold contracts of a financial instrument. A long position is financial security bought expecting the security price go higher. A short position is an obligation to supply a security expecting the price will fall in future.

General information about trading operations is available in the [client terminal help](https://www.metatrader5.com/en/terminal/help/trading/general_concept "MetaTrader 5 Help").

Trading functions can be used in Expert Advisors and scripts. Trading functions can be called only if in the properties of the Expert Advisor or script the "Allow live trading" checkbox is enabled.

Trading can be allowed or prohibited depending on various factors described in the [Trade Permission](../MQL5-programs/Trade-Permission/Trade-Permission.md) section.

| Function | Action |
| --- | --- |
| [OrderCalcMargin](OrderCalcMargin/OrderCalcMargin.md) | Calculates the margin required for the specified order type, in the deposit currency |
| [OrderCalcProfit](OrderCalcProfit/OrderCalcProfit.md) | Calculates the profit based on the parameters passed, in the deposit currency |
| [OrderCheck](OrderCheck/OrderCheck.md) | Checks if there are enough funds to execute the required [trade operation](../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md). |
| [OrderSend](OrderSend/OrderSend.md) | Sends [trade requests](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) to a server |
| [OrderSendAsync](OrderSendAsync/OrderSendAsync.md) | Asynchronously sends [trade requests](../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md) without waiting for the trade response of the trade server |
| [PositionsTotal](PositionsTotal/PositionsTotal.md) | Returns the number of open positions |
| [PositionGetSymbol](PositionGetSymbol/PositionGetSymbol.md) | Returns the symbol corresponding to the open position |
| [PositionSelect](PositionSelect/PositionSelect.md) | Chooses an open position for further working with it |
| [PositionSelectByTicket](PositionSelectByTicket/PositionSelectByTicket.md) | Selects a position to work with by the ticket number specified in it |
| [PositionGetDouble](PositionGetDouble/PositionGetDouble.md) | Returns the requested property of an open position (double) |
| [PositionGetInteger](PositionGetInteger/PositionGetInteger.md) | Returns the requested property of an open position (datetime or int) |
| [PositionGetString](PositionGetString/PositionGetString.md) | Returns the requested property of an open position (string) |
| [PositionGetTicket](PositionGetTicket/PositionGetTicket.md) | Returns the ticket of the position with the specified index in the list of open positions |
| [OrdersTotal](OrdersTotal/OrdersTotal.md) | Returns the number of orders |
| [OrderGetTicket](OrderGetTicket/OrderGetTicket.md) | Return the ticket of a corresponding order |
| [OrderSelect](OrderSelect/OrderSelect.md) | Selects a order for further working with it |
| [OrderGetDouble](OrderGetDouble/OrderGetDouble.md) | Returns the requested property of the order (double) |
| [OrderGetInteger](OrderGetInteger/OrderGetInteger.md) | Returns the requested property of the order (datetime or int) |
| [OrderGetString](OrderGetString/OrderGetString.md) | Returns the requested property of the order (string) |
| [HistorySelect](HistorySelect/HistorySelect.md) | Retrieves the history of transactions and orders for the specified period of the server time |
| [HistorySelectByPosition](HistorySelectByPosition/HistorySelectByPosition.md) | Requests the history of deals with a specified [position identifier](../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_integer). |
| [HistoryOrderSelect](HistoryOrderSelect/HistoryOrderSelect.md) | Selects an order in the history for further working with it |
| [HistoryOrdersTotal](HistoryOrdersTotal/HistoryOrdersTotal.md) | Returns the number of orders in the history |
| [HistoryOrderGetTicket](HistoryOrderGetTicket/HistoryOrderGetTicket.md) | Return order ticket of a corresponding order in the history |
| [HistoryOrderGetDouble](HistoryOrderGetDouble/HistoryOrderGetDouble.md) | Returns the requested property of an order in the history (double) |
| [HistoryOrderGetInteger](HistoryOrderGetInteger/HistoryOrderGetInteger.md) | Returns the requested property of an order in the history (datetime or int) |
| [HistoryOrderGetString](HistoryOrderGetString/HistoryOrderGetString.md) | Returns the requested property of an order in the history (string) |
| [HistoryDealSelect](HistoryDealSelect/HistoryDealSelect.md) | Selects a deal in the history for further calling it through appropriate functions |
| [HistoryDealsTotal](HistoryDealsTotal/HistoryDealsTotal.md) | Returns the number of deals in the history |
| [HistoryDealGetTicket](HistoryDealGetTicket/HistoryDealGetTicket.md) | Returns a ticket of a corresponding deal in the history |
| [HistoryDealGetDouble](HistoryDealGetDouble/HistoryDealGetDouble.md) | Returns the requested property of a deal in the history (double) |
| [HistoryDealGetInteger](HistoryDealGetInteger/HistoryDealGetInteger.md) | Returns the requested property of a deal in the history (datetime or int) |
| [HistoryDealGetString](HistoryDealGetString/HistoryDealGetString.md) | Returns the requested property of a deal in the history (string) |
