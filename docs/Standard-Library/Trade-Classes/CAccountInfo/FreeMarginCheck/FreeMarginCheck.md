# FreeMarginCheck

FreeMarginCheck

Gets the amount of free margin left after trade operation.

|  |
| --- |
| double  FreeMarginCheck(     const string        symbol,              // symbol     ENUM\_ORDER\_TYPE     trade\_operation,     // order type (ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL)     double              volume,              // volume     double              price                // price     ) const |

Parameters

symbol

[in]  Symbol for trade operation.

trade\_operation

[in]  Type of trade operation from [ENUM\_ORDER\_TYPE](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type) enumeration.

volume

[in]  Volume of trade operation.

price

[in]  Price of trade operation.

Return Value

Amount of free margin left after trade operation.
