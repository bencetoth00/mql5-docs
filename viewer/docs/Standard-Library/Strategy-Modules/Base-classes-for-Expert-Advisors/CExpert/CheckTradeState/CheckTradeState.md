# CheckTradeState


Compares the current state with the saved one and calls the corresponding event handler.

```cpp
bool  CheckTradeState()
```

Return Value

true - event has been handled, otherwise - false.

Note

It checks the number of positions, orders, deals, and historical orders by comparing with the values saved by [HistoryPoint()](../HistoryPoint/HistoryPoint.md) method. If trade history has changed, it calls the corresponding virtual event handler.