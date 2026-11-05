# Position Properties


Execution of [trade operations](../Trade-Operation-Types/Trade-Operation-Types.md) results in the opening of a position, changing of its volume and/or direction, or its disappearance. Trade operations are conducted based on [orders](../Order-Properties/Order-Properties.md), sent by the [OrderSend()](../../../Trade-Functions/OrderSend/OrderSend.md) function in the form of [trade requests](../../Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md). For each financial [security](../../Environment-State/Symbol-Properties/Symbol-Properties.md) (symbol) only one open position is possible. A position has a set of properties available for reading by the PositionGet...() functions.

For the function [PositionGetInteger()](../../../Trade-Functions/PositionGetInteger/PositionGetInteger.md)

ENUM\_POSITION\_PROPERTY\_INTEGER

| Identifier | Description | Type |
| --- | --- | --- |
| POSITION\_TICKET | Position ticket. Unique number assigned to each newly opened position. It usually matches the ticket of an order used to open the position except when the ticket is changed as a result of service operations on the server, for example, when charging swaps with position re-opening. To find an order used to open a position, apply the POSITION\_IDENTIFIER property.     POSITION\_TICKET value corresponds to [MqlTradeRequest::position](../../Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md). | long |
| POSITION\_TIME | Position open time | datetime |
| POSITION\_TIME\_MSC | Position opening time in milliseconds since 01.01.1970 | long |
| POSITION\_TIME\_UPDATE | Position changing time | datetime |
| POSITION\_TIME\_UPDATE\_MSC | Position changing time in milliseconds since 01.01.1970 | long |
| POSITION\_TYPE | Position type | [ENUM\_POSITION\_TYPE](Position-Properties.md#enum_position_type) |
| POSITION\_MAGIC | Position magic number (see [ORDER\_MAGIC](../Order-Properties/Order-Properties.md)) | long |
| POSITION\_IDENTIFIER | Position identifier is a unique number assigned to each re-opened position. It does not change throughout its life cycle and corresponds to the ticket of an order used to open a position.     Position identifier is specified in each order (ORDER\_POSITION\_ID) and deal (DEAL\_POSITION\_ID) used to open, modify, or close it. Use this property to search for orders and deals related to the position.     When reversing a position in netting mode (using a single in/out trade), POSITION\_IDENTIFIER does not change. However, POSITION\_TICKET is replaced with the ticket of the order that led to the reversal. Position reversal is not provided in hedging mode. | long |
| POSITION\_REASON | The reason for opening a position | [ENUM\_POSITION\_REASON](Position-Properties.md#enum_position_reason) |

For the function [PositionGetDouble()](../../../Trade-Functions/PositionGetDouble/PositionGetDouble.md)

ENUM\_POSITION\_PROPERTY\_DOUBLE

| Identifier | Description | Type |
| --- | --- | --- |
| POSITION\_VOLUME | Position volume | double |
| POSITION\_PRICE\_OPEN | Position open price | double |
| POSITION\_SL | Stop Loss level of opened position | double |
| POSITION\_TP | Take Profit level of opened position | double |
| POSITION\_PRICE\_CURRENT | Current price of the position symbol | double |
| POSITION\_SWAP | Cumulative swap | double |
| POSITION\_PROFIT | Current profit | double |

For the function [PositionGetString()](../../../Trade-Functions/PositionGetString/PositionGetString.md)

ENUM\_POSITION\_PROPERTY\_STRING

| Identifier | Description | Type |
| --- | --- | --- |
| POSITION\_SYMBOL | Symbol of the position | string |
| POSITION\_COMMENT | Position comment | string |
| POSITION\_EXTERNAL\_ID | Position identifier in an external trading system (on the Exchange) | string |

 

Direction of an open position (buy or sell) is defined by the value from the ENUM\_POSITION\_TYPE enumeration. In order to obtain the type of an open position use the [PositionGetInteger()](../../../Trade-Functions/PositionGetInteger/PositionGetInteger.md) function with the POSITION\_TYPE modifier.

ENUM\_POSITION\_TYPE

| Identifier | Description |
| --- | --- |
| POSITION\_TYPE\_BUY | Buy |
| POSITION\_TYPE\_SELL | Sell |

 

The reason for opening a position is contained in the POSITION\_REASON property. A position can be opened as a result of activation of an order placed from a desktop terminal, a mobile application, by an Expert Advisor, etc. Possible values of POSITION\_REASON are described in the ENUM\_POSITION\_REASON enumeration.

ENUM\_POSITION\_REASON

| Identifier | Description |
| --- | --- |
| POSITION\_REASON\_CLIENT | The position was opened as a result of activation of an order placed from a desktop terminal |
| POSITION\_REASON\_MOBILE | The position was opened as a result of activation of an order placed from a mobile application |
| POSITION\_REASON\_WEB | The position was opened as a result of activation of an order placed from the web platform |
| POSITION\_REASON\_EXPERT | The position was opened as a result of activation of an order placed from an MQL5 program, i.e. an Expert Advisor or a script |
