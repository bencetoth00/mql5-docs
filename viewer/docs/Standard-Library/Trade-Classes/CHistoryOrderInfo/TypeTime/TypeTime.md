# TypeTime


Gets the type of order at the time of the expiration.

```cpp
ENUM_ORDER_TYPE_TIME  TypeTime() const
```

Return Value

Type of order at the time of the expiration from [ENUM\_ORDER\_TYPE\_TIME](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_time) enumeration.

Note

The historical order should be selected using the [Ticket](../Ticket/Ticket.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.