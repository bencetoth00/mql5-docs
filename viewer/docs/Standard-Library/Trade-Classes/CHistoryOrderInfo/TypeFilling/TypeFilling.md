# TypeFilling


Gets the type of order execution by remainder.

```cpp
ENUM_ORDER_TYPE_FILLING  TypeFilling() const
```

Return Value

Type of order execution by remainder from [ENUM\_ORDER\_TYPE\_FILLING](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) enumeration.

Note

The historical order should be selected using the [Ticket](../Ticket/Ticket.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.