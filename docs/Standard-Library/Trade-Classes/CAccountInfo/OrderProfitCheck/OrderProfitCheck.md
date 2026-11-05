# OrderProfitCheck

OrderProfitCheck

The function calculates the profit for the current account, based on the parameters passed. The function is used for pre-evaluation of the result of a trade operation. The value is returned in the account currency.

|  |
| --- |
| double  OrderProfitCheck(     const string        symbol,              // symbol     ENUM\_ORDER\_TYPE     trade\_operation,     // order type (ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL)     double              volume,              // volume     double              price\_open,          // position open price     double              price\_close          // position close price     ) const |

Parameters

symbol

[in]  Symbol for trade operation.

trade\_operation

[in] Type of trade operation from [ENUM\_ORDER\_TYPE](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type) enumeration.

volume

[in]  Volume of trade operation.

price\_open

[in]  Open price.

price\_close

[in]  Close price.

Return Value

If successful, it returns amount of profit or [EMPTY\_VALUE](../../../../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) in the case of error.
