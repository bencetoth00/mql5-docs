# OrderModify


Modifies the pending order parameters.

```cpp
bool  OrderModify(
   ulong                 ticket,         // order ticket
   double                price,          // execution price
   double                sl,             // Stop Loss price
   double                tp,             // Take Profit price
   ENUM_ORDER_TYPE_TIME  type_time,      // type by expiration
   datetime              expiration,     // expiration
   double                stoplimit       // Limit order price
   )
```

Parameters

ticket

[in]  Order ticket.

price

[in] The new price by which the order must be executed (or the previous value, if the change is not necessary).

sl

[in] The new price by which the Stop Loss will trigger (or the previous value, if the change is not necessary).

tp

[in] The new price by which the Take Profit will trigger (or the previous value, if the change is not necessary).

type\_time

[in] The new type of order by expiration from [ENUM\_ORDER\_TYPE\_TIME](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_time) enumeration (or the previous value, if the change is not necessary).

expiration

[in] The new expiration date of pending order (or the previous value, if the change is not necessary).

stoplimit

[in]  New price used for setting a Limit order when the price reaches price value. It is specified only for StopLimit orders.

Return Value

true - successful check of the basic structures, otherwise - false.

Note

Successful completion of the OrderModify(...) method does not always mean successful execution of the trade operation. It is necessary to check the result of trade request (trade server return code) using [ResultRetcode()](../ResultRetcode/ResultRetcode.md).