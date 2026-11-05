# Trade Transaction Types


When performing some definite actions on a trade account, its state changes. Such actions include:

- Sending a trade request from any MQL5 application in the client terminal using [OrderSend](../../../Trade-Functions/OrderSend/OrderSend.md) and [OrderSendAsync](../../../Trade-Functions/OrderSendAsync/OrderSendAsync.md) functions and its further execution;
- Sending a trade request via the terminal graphical interface and its further execution;

- Pending orders and stop orders activation on the server;
- Performing operations on a trade server side.

The following trade transactions are performed as a result of these actions:

- handling a trade request;
- changing open orders;
- changing orders history;
- changing deals history;
- changing positions.

For example, when sending a market buy order, it is handled, an appropriate buy order is created for the account, the order is then executed and removed from the list of the open ones, then it is added to the orders history, an appropriate deal is added to the history and a new position is created. All these actions are trade transactions.

To let a programmer to track the actions performed in relation to a trade account, [OnTradeTransaction](../../../Event-Handling/OnTradeTransaction/OnTradeTransaction.md) function has been provided. This handler allows to get trade transactions applied to an account in MQL5 application. Trade transaction description is submitted in OnTradeTransaction first parameter using [MqlTradeTransaction](../../Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) structure.

Trade transaction type is submitted in the type parameter of MqlTradeTransaction structure. Possible types of trade transactions are described by the following enumeration:

ENUM\_TRADE\_TRANSACTION\_TYPE

| Identifier | Description |
| --- | --- |
| TRADE\_TRANSACTION\_ORDER\_ADD | Adding a new open order. |
| TRADE\_TRANSACTION\_ORDER\_UPDATE | Updating an open order. The updates include not only evident changes from the client terminal or a trade server sides but also changes of an order state when setting it (for example, transition from [ORDER\_STATE\_STARTED](../Order-Properties/Order-Properties.md#enum_order_state) to [ORDER\_STATE\_PLACED](../Order-Properties/Order-Properties.md#enum_order_state) or from [ORDER\_STATE\_PLACED](../Order-Properties/Order-Properties.md#enum_order_state) to [ORDER\_STATE\_PARTIAL](../Order-Properties/Order-Properties.md#enum_order_state), etc.). |
| TRADE\_TRANSACTION\_ORDER\_DELETE | Removing an order from the list of the open ones. An order can be deleted from the open ones as a result of setting an appropriate request or execution (filling) and moving to the history. |
| TRADE\_TRANSACTION\_DEAL\_ADD | Adding a deal to the history. The action is performed as a result of an order execution or performing operations with an account balance. |
| TRADE\_TRANSACTION\_DEAL\_UPDATE | Updating a deal in the history. There may be cases when a previously executed deal is changed on a server. For example, a deal has been changed in an external trading system (exchange) where it was previously transferred by a broker. |
| TRADE\_TRANSACTION\_DEAL\_DELETE | Deleting a deal from the history. There may be cases when a previously executed deal is deleted from a server. For example, a deal has been deleted in an external trading system (exchange) where it was previously transferred by a broker. |
| TRADE\_TRANSACTION\_HISTORY\_ADD | Adding an order to the history as a result of execution or cancellation. |
| TRADE\_TRANSACTION\_HISTORY\_UPDATE | Changing an order located in the orders history. This type is provided for enhancing functionality on a trade server side. |
| TRADE\_TRANSACTION\_HISTORY\_DELETE | Deleting an order from the orders history. This type is provided for enhancing functionality on a trade server side. |
| TRADE\_TRANSACTION\_POSITION | Changing a position not related to a deal execution. This type of transaction shows that a position has been changed on a trade server side. Position volume, open price, Stop Loss and Take Profit levels can be changed. Data on changes are submitted in [MqlTradeTransaction](../../Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) structure via OnTradeTransaction handler. Position change (adding, changing or closing), as a result of a deal execution, does not lead to the occurrence of TRADE\_TRANSACTION\_POSITION transaction. |
| TRADE\_TRANSACTION\_REQUEST | Notification of the fact that a trade request has been processed by a server and processing result has been received. Only type field (trade transaction type) must be analyzed for such transactions in [MqlTradeTransaction](../../Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) structure. The second and third parameters of [OnTradeTransaction](../../../Event-Handling/OnTradeTransaction/OnTradeTransaction.md) (request and result) must be analyzed for additional data. |

Depending on a trade transaction type, various parameters are filled in MqlTradeTransaction structure describing it. A detailed description of submitted data is shown in ["Structure of a Trade Transaction"](../../Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md).

See also

[Structure of a Trade Transaction](../../Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md), [OnTradeTransaction](../../../Event-Handling/OnTradeTransaction/OnTradeTransaction.md)
