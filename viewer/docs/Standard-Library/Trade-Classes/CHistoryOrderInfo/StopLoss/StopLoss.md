# StopLoss


Gets the Stop Loss price of the order.

```cpp
double  StopLoss() const
```

Return Value

Stop Loss price of the order.

Note

The historical order should be selected using the [Ticket](../Ticket/Ticket.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.