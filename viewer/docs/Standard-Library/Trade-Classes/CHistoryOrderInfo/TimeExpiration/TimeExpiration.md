# TimeExpiration


Gets the time of order expiration.

```cpp
datetime  TimeExpiration() const
```

Return Value

Time of order expiration, set on its placement.

Note

The historical order should be selected using the [Ticket](../Ticket/Ticket.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.