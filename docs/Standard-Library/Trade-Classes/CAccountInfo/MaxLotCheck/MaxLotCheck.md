# MaxLotCheck

MaxLotCheck

Gets the maximum possible volume of trade operation.

|  |
| --- |
| double  MaxLotCheck(     const string        symbol,              // symbol     ENUM\_ORDER\_TYPE     trade\_operation,     // order type (ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL)     double              price,               // price     double              percent=100          // percent of available margin (default is 100%)     ) const |

Parameters

symbol

[in]  Symbol for trade operation.

trade\_operation

[in]  Type of trade operation from [ENUM\_ORDER\_TYPE](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type) enumeration.

price

[in]  Price of trade operation.

percent=100

[in]  Percent of available margin (in %) to be used for trade operation.

Return Value

Maximum possible volume of trade operation.
