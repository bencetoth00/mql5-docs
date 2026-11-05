# MarginCheck


Gets the amount of margin, required for trade operation.

```cpp
double  MarginCheck(
   const string        symbol,              // symbol
   ENUM_ORDER_TYPE     trade_operation,     // order type (ORDER_TYPE_BUY or ORDER_TYPE_SELL)
   double              volume,              // volume
   double              price                // price
   ) const
```

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

Amount of margin required for trade operation.